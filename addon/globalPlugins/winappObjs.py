# Windows app controls repository
# Copyright 2015-2022 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.

# Help Mypy and other static checkers for a time by using annotations from future Python releases.
from __future__ import annotations
from typing import Optional, Any
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
import winVersion
import addonHandler
addonHandler.initTranslation()

# #52: forget everything if the current release is not a supported version of Windows.
isAddonSupported = winVersion.getWinVer() >= winVersion.WIN10_21H1


# For convenience.
additionalEvents: dict[int, str] = {
	UIAHandler.UIA_Drag_DragCompleteEventId: "UIA_dragComplete",
	UIAHandler.UIA_DropTarget_DroppedEventId: "UIA_dropTargetDropped",
}


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super().__init__()
		# Don't do anything unless this is Windows 10 or later.
		# #52: and this is a supported build.
		if not isAddonSupported:
			return
		# #20: don't even think about proceeding in secure screens.
		# #40: skip over the rest if appx is in effect.
		if globalVars.appArgs.secure or config.isAppX:
			return
		# Try adding additional events in the constructor.
		# If it fails, try again after NVDA is fully initialized.
		try:
			log.debug("winapps: adding additional events")
			self._addAdditionalUIAEvents()
		except AttributeError:
			log.debug("winapps: UIA handler not ready, delaying until NVDA is fully initialized")
			queueHandler.queueFunction(queueHandler.eventQueue, self._addAdditionalUIAEvents, delay=True)

	# Manually add events after root element is located.
	def _addAdditionalUIAEvents(self, delay: bool = False) -> None:
		# Add a series of events instead of doing it one at a time.
		# Some events are only available in a specific build range
		# and/or while a specific version of IUIAutomation interface is in use.
		if delay:
			log.debug("winapps: adding additional events after a delay")
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

	# Record UIA property info about an object if told to do so.
	# An add-on named Event Tracker (deriving from this add-on) will log event information for most events.
	# However, because this add-on adds additional events, log them here.
	def uiaDebugLogging(self, obj: Any, event: Optional[str] = None) -> None:
		if isinstance(obj, UIA) and log.isEnabledFor(log.DEBUG):
			info: list[str] = [f"object: {repr(obj)}"]
			info.append(f"name: {obj.name}")
			if not event:
				event = "no event specified"
			info.append(f"event: {event}")
			info.append(f"app module: {obj.appModule}")
			element = obj.UIAElement
			info.append(f"Automation Id: {obj.UIAAutomationId}")
			info.append(f"class name: {element.cachedClassName}")
			log.debug("winapps: UIA {debuginfo}".format(debuginfo=", ".join(info)))

	# Events defined in NVDA.

	def event_nameChange(self, obj, nextHandler):
		# NVDA Core issue 5641: try catching virtual desktop switch event,
		# which will result in name change for the desktop object.
		# To be taken care of by NVDA Core, and for older releases, let the add-on handle it for a time.
		# This may degrade performance and/or cause NVDA to become verbose in situations other than
		# virtual desktop switch, so exercise discretion.
		if obj.windowClassName == "#32769":
			if log.isEnabledFor(log.DEBUG):
				log.debug(f"winapps: possible desktop name change from {obj}, app module: {obj.appModule}")
			# CSRSS: Client/Server Runtime Subsystem (Windows subsystem process/desktop object)
			if obj.appModule.appName == "csrss":
				import wx
				# Even with desktop name change handler added,
				# older Windows releases won't support this properly.
				# Properly supported in Windows 10 1909.
				if not hasattr(eventHandler, "handlePossibleDesktopNameChange"):
					wx.CallLater(500, ui.message, obj.name)
		nextHandler()

	def event_UIA_notification(self, obj, nextHandler, activityId=None, **kwargs):
		# Introduced in Windows 10 1709, to be treated as a notification event.
		# Bulk of this transferred to Event Tracker add-on in 2021.
		# Play a debug tone if and only if notifications come from somewhere other than the active app
		# and NVDA was restarted with debug logging mode.
		if (
			isinstance(obj, UIA)
			and obj.appModule != api.getFocusObject().appModule
			and globalVars.appArgs.debugLogging
		):
			import tones
			# For debugging purposes.
			tones.beep(500, 100)
		# Do not allow notification to be announced if "report notifications" is off.
		if not config.conf["presentation"]["reportHelpBalloons"]:
			return
		# In recent versions of Word 365, notification event is used to announce editing functions,
		# some of them being quite anoying.
		if obj.appModule.appName == "winword" and activityId == "AccSN1":
			return
		nextHandler()

	# Events defined in this add-on.

	def event_UIA_dragComplete(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragComplete")
		# Announce the new drop location by faking a gain focus event.
		eventHandler.queueEvent("gainFocus", obj)
		nextHandler()

	def event_UIA_dropTargetDropped(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dropTargetDropped")
		# Unlike drag complete event, it is something else that raises this event
		# but NVDA records the correct focused element, so fake a gain focus event.
		eventHandler.queueEvent("gainFocus", api.getFocusObject())
		nextHandler()
