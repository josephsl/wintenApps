# Windows app controls repository
# Copyright 2015-2022 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.

# Help Mypy and other static checkers for a time by using annotations from future Python releases.
from __future__ import annotations
import globalPluginHandler
import ui
from NVDAObjects.UIA import UIA, Dialog
import api
import config
import queueHandler
import eventHandler
import globalVars
import UIAHandler
from logHandler import log
import addonHandler
addonHandler.initTranslation()


# Add additional UIA events not included in NVDA Core.
additionalEvents: dict[int, str] = {
	# Specifically to support drag and drop operations.
	# Resolved in NVDA 2022.4.
	UIAHandler.UIA_Drag_DragStartEventId: "stateChange",
	UIAHandler.UIA_Drag_DragCancelEventId: "stateChange",
	UIAHandler.UIA_Drag_DragCompleteEventId: "stateChange",
}


# Add additional property events not included in NVDA Core.
additionalPropertyEvents: dict[int, str] = {}
# #69: specifically to support drag drop effect property when Windows 10 Start menu tiles are rearranged.
# Resolved in NVDA 2022.4.
if not hasattr(UIA, "event_UIA_dragDropEffect"):
	additionalPropertyEvents[UIAHandler.UIA_DragDropEffectPropertyId] = "UIA_dragDropEffect"
# Add drop target effect property so it can be announced when reordering Action center/quick settings items.
# Resolved in NVDA 2022.4.
if not hasattr(UIA, "event_UIA_dropTargetEffect"):
	additionalPropertyEvents[UIAHandler.UIA_DropTargetDropTargetEffectPropertyId] = "UIA_dropTargetEffect"


# #20: don't even think about proceeding in secure screens.
def disableInSecureMode(cls):
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super().__init__()
		# Try adding additional events and properties in the constructor.
		# If it fails, try again after NVDA is fully initialized.
		try:
			log.debug("winapps: adding additional events and properties")
			self._addAdditionalUIAEvents()
		except AttributeError:
			log.debug("winapps: UIA handler not ready, delaying until NVDA is fully initialized")
			queueHandler.queueFunction(queueHandler.eventQueue, self._addAdditionalUIAEvents, delay=True)

	# Manually add events after root element is located.
	def _addAdditionalUIAEvents(self, delay: bool = False) -> None:
		# Add a series of events and properties instead of doing it one at a time.
		# Some events and properties are only available in a specific build range
		# and/or while a specific version of IUIAutomation interface is in use.
		if delay:
			log.debug("winapps: adding additional events and properties after a delay")
		# Use event handler group facility to add more events.
		# Internally powered by IUIAutomation6 interface introduced in Windows 10 1809.
		addonGlobalEventHandlerGroup = UIAHandler.handler.clientObject.CreateEventHandlerGroup()
		for event, name in additionalEvents.items():
			if event not in UIAHandler.UIAEventIdsToNVDAEventNames:
				UIAHandler.UIAEventIdsToNVDAEventNames[event] = name
				# Global event handler group set must be updated, too.
				UIAHandler.globalEventHandlerGroupUIAEventIds.add(event)
				addonGlobalEventHandlerGroup.addAutomationEventHandler(
					event,
					UIAHandler.TreeScope_Subtree,
					UIAHandler.handler.baseCacheRequest,
					UIAHandler.handler
				)
				log.debug(f"winapps: added event ID {event}, assigned to {name}")
		for event, name in additionalPropertyEvents.items():
			if event not in UIAHandler.UIAPropertyIdsToNVDAEventNames:
				UIAHandler.UIAPropertyIdsToNVDAEventNames[event] = name
				log.debug(f"winapps: added property event ID {event}, assigned to {name}")
				# Global property event handler group set must be updated, too.
				UIAHandler.globalEventHandlerGroupUIAPropertyIds.add(event)
		addonGlobalEventHandlerGroup.AddPropertyChangedEventHandler(
			UIAHandler.TreeScope_Subtree,
			UIAHandler.handler.baseCacheRequest,
			UIAHandler.handler,
			*UIAHandler.handler.clientObject.IntSafeArrayToNativeArray(additionalPropertyEvents)
		)
		UIAHandler.handler.addEventHandlerGroup(UIAHandler.handler.rootElement, addonGlobalEventHandlerGroup)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if not isinstance(obj, UIA):
			return
		# Windows that are really dialogs.
		# Some dialogs, although listed as a dialog thanks to UIA class name,
		# does not advertise the proper role of dialog.
		# This is still the case with some dialogs such as restart to install updates dialog in Windows 11.
		if obj.UIAElement.cachedClassName in UIAHandler.UIADialogClassNames and Dialog not in clsList:
			clsList.insert(0, Dialog)

	# Events defined in NVDA.

	def event_nameChange(self, obj, nextHandler):
		# NVDA Core issue 5641: try catching virtual desktop switch event,
		# which will result in name change for the desktop object.
		# To be taken care of by NVDA Core, and for older releases, let the add-on handle it for a time.
		# This may degrade performance and/or cause NVDA to become verbose in situations other than
		# virtual desktop switch, so exercise discretion.
		# CSRSS: Client/Server Runtime Subsystem (Windows subsystem process/desktop object)
		if obj.windowClassName == "#32769" and obj.appModule.appName == "csrss":
			import wx
			# Even with desktop name change handler added,
			# older Windows releases won't support this properly.
			# Properly supported in Windows 10 1909.
			if not hasattr(eventHandler, "handlePossibleDesktopNameChange"):
				wx.CallLater(500, ui.message, obj.name)
		nextHandler()

	def event_UIA_notification(self, obj, nextHandler, displayString=None, activityId=None, **kwargs):
		# Introduced in Windows 10 1709, to be treated as a notification event.
		# Do not allow notification to be announced if "report notifications" is off.
		if not config.conf["presentation"]["reportHelpBalloons"]:
			return
		# In recent versions of Word 365, notification event is used to announce editing functions,
		# some of them being quite anoying.
		if obj.appModule.appName == "winword" and activityId == "AccSN1":
			return
		# Announce microphone mute status from anywhere in Windows 11 22H2 and later.
		if obj.appModule.appName == "explorer" and activityId == "Windows.Shell.CallMuteAnnouncement":
			if api.getFocusObject().appModule != obj.appModule:
				ui.message(displayString)
				return
		nextHandler()

	def event_stateChange(self, obj, nextHandler):
		# Specifically designed to detect drag start and UIA "is grabbed" state changes.
		# Resolved in NVDA 2022.4.
		import controlTypes
		if isinstance(obj, UIA) and obj._getUIACacheablePropertyValue(UIAHandler.UIA_DragIsGrabbedPropertyId):
			obj.states.add(controlTypes.State.DRAGGING)
		nextHandler()

	# Events defined in this add-on.

	def event_UIA_dragDropEffect(self, obj, nextHandler):
		# Report drag and drop effect as communicated by UIA.
		# Resolved in NVDA 2022.4.
		if not hasattr(obj, "event_UIA_dragDropEffect"):
			dragDropEffect = obj._getUIACacheablePropertyValue(UIAHandler.UIA_DragDropEffectPropertyId)
			ui.message(dragDropEffect)
		nextHandler()

	def event_UIA_dropTargetEffect(self, obj, nextHandler):
		# Announce drop target effect such as item placement in Start menu and Action center if present.
		# Resolved in NVDA 2022.4.
		if not hasattr(obj, "event_UIA_dropTargetEffect"):
			dropTargetEffect = obj._getUIACacheablePropertyValue(
				UIAHandler.UIA_DropTargetDropTargetEffectPropertyId
			)
			# Sometimes drop target effect text is empty as it comes from a different object.
			if not dropTargetEffect:
				for element in reversed(api.getFocusAncestors()):
					if isinstance(element, UIA):
						dropTargetEffect = element._getUIACacheablePropertyValue(
							UIAHandler.UIA_DropTargetDropTargetEffectPropertyId
						)
						if dropTargetEffect:
							break
			ui.message(dropTargetEffect)
		nextHandler()
