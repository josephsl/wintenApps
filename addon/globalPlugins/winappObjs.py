# Windows app controls repository
# Copyright 2015-2021 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.

# Help Mypy and other static checkers for a time by using annotations from future Python releases.
from __future__ import annotations
from typing import Optional, Any
from comtypes import COMError
import globalPluginHandler
import controlTypes
import ui
from NVDAObjects.UIA import UIA, SearchField, Dialog
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
# NVDA 2019.2 includes a handy Windows 10 version check function.
# Changed in NVDA 2021.1 to include Windows release constants.
W10AddonSupported = winVersion.getWinVer() >= winVersion.WIN10_20H2


# Extra UIA constants
# None at this time

# For convenience.
W10Events: dict[int, str] = {
	UIAHandler.UIA_Drag_DragStartEventId: "UIA_dragStart",
	UIAHandler.UIA_Drag_DragCancelEventId: "UIA_dragCancel",
	UIAHandler.UIA_Drag_DragCompleteEventId: "UIA_dragComplete",
	UIAHandler.UIA_DropTarget_DragEnterEventId: "UIA_dropTargetDragEnter",
	UIAHandler.UIA_DropTarget_DragLeaveEventId: "UIA_dropTargetDragLeave",
	UIAHandler.UIA_DropTarget_DroppedEventId: "UIA_dropTargetDropped",
	UIAHandler.UIA_LayoutInvalidatedEventId: "UIA_layoutInvalidated",
}

# Additional dialogs not recognized by NVDA itself.
UIAAdditionalDialogClassNames: list[str] = []

# Object states constants for use when tracking events.
# Copied from NVDA Core's default navigator object dev info's state retriever (credit: NV Access).
# State constants in control types were rearranged in control types refactor (enumeration) in NVDA.
# Support control types refactor (both before (2021.1) and after (2021.2) for a time).
if hasattr(controlTypes, "State"):
	stateConsts: dict[int, str] = dict(
		(state.value, state.name) for state in controlTypes.State
	)
else:
	stateConsts: dict[int, str] = dict(
		(const, name) for name, const in controlTypes.__dict__.items() if name.startswith("STATE_")
	)


# Search fields.
# Unlike the Core implementation, this class announces suggestion count, to be incorporated into NVDA later.
class W10SearchField(SearchField):

	def event_suggestionsOpened(self):
		super(W10SearchField, self).event_suggestionsOpened()
		# #59: use an internal function to announce suggestions count.
		self._layoutInvalidatedReportSuggestionsCount()

	def _layoutInvalidatedReportSuggestionsCount(self):
		# Announce number of items found
		# (except in Start search box where the suggestions are selected as user types).
		# Because inaccurate count could be announced (when users type, suggestion count changes),
		# thus announce this if position info reporting is enabled.
		if config.conf["presentation"]["reportObjectPositionInformation"]:
			# Item count must be the last one spoken.
			suggestionsCount: int = self.controllerFor[0].childCount
			suggestionsMessage = (
				# Translators: part of the suggestions count message (for example: 2 suggestions).
				_("1 suggestion")
				# Translators: part of the suggestions count message (for example: 2 suggestions).
				if suggestionsCount == 1 else _("{} suggestions").format(suggestionsCount)
			)
			ui.message(suggestionsMessage)


# Various XAML headings (Settings app, for example) introduced in Version 1803.
class XAMLHeading(UIA):

	def _get_role(self) -> int:
		# Heading levels are 8005x, control types heading levels are 4x, therefore the below object role formula.
		return self._getUIACacheablePropertyValue(UIAHandler.UIA_HeadingLevelPropertyId) - 80010


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# Don't do anything unless this is Windows 10 or later.
		# #52: and this is a supported build.
		if not W10AddonSupported:
			return
		# #20: don't even think about proceeding in secure screens.
		# #40: skip over the rest if appx is in effect.
		if globalVars.appArgs.secure or config.isAppX:
			return
		# Detect Windows 11.
		WIN11 = winVersion.WinVersion(major=10, minor=0, build=22000)
		if winVersion.getWinVer() >= WIN11:
			log.info("W10: Windows 11 detected")
		# Try adding additional events in the constructor.
		# If it fails, try again after NVDA is fully initialized.
		try:
			log.debug("W10: adding additional events")
			self._addAdditionalUIAEvents()
		except AttributeError:
			log.debug("W10: UIA handler not ready, delaying until NVDA is fully initialized")
			queueHandler.queueFunction(queueHandler.eventQueue, self._addAdditionalUIAEvents, delay=True)
		# Allow NVDA to recognize more dialogs, especially ones that are not advertising themselves as such.
		for dialogClassName in UIAAdditionalDialogClassNames:
			if dialogClassName not in UIAHandler.UIADialogClassNames:
				log.debug(f"W10: adding class name {dialogClassName} to known dialog class names")
				UIAHandler.UIADialogClassNames.append(dialogClassName)

	# Manually add events after root element is located.
	def _addAdditionalUIAEvents(self, delay: bool = False) -> None:
		# Add a series of events instead of doing it one at a time.
		# Some events are only available in a specific build range
		# and/or while a specific version of IUIAutomation interface is in use.
		if delay:
			log.debug("W10: adding additional events after a delay")
		# Use event handler group facility to add more events (properly introduced in NVDA 2020.3).
		# Use IUIAutomation6 interface directly (Version 1809 or later).
		addonGlobalEventHandlerGroup = UIAHandler.handler.clientObject.CreateEventHandlerGroup()
		for event, name in W10Events.items():
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
				log.debug(f"W10: added event ID {event}, assigned to {name}")
		UIAHandler.handler.addEventHandlerGroup(UIAHandler.handler.rootElement, addonGlobalEventHandlerGroup)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# There's no point looking at non-UIA objects.
		# Also because this add-on might be turned on "accidentally" in earlier Windows releases,
		# including unsupported Windows builds...
		if not (isinstance(obj, UIA) and W10AddonSupported):
			return
		# Windows that are really dialogs.
		# Some dialogs, although listed as a dialog thanks to UIA class name,
		# does not advertise the proper role of dialog.
		if obj.UIAElement.cachedClassName in UIAHandler.UIADialogClassNames and Dialog not in clsList:
			clsList.insert(0, Dialog)
			return
		# Search field that does raise controller for event.
		# Although basic functionality is included in NVDA 2017.3,
		# added enhancements such as announcing suggestion count.
		if obj.UIAAutomationId in ("SearchTextBox", "TextBox"):
			# NVDA 2017.3 includes a dedicated search box overlay class in searchui
			# to deal with search term announcement problem.
			# Because the add-on version deals with focus comparison,
			# let all search fields go through this check as much as possible except for specific apps.
			if obj.appModule.appName not in ("searchui", "searchapp", "searchhost"):
				clsList.insert(0, W10SearchField)
				return
		# Recognize headings as reported by XAML (Version 1803 or later).
		# Some apps may cause COM to throw timeout error.
		try:
			# NvDA does not recognize heading levels 7, 8, and 9, therefore use a chained comparison.
			if (
				UIAHandler.HeadingLevel1 <= obj._getUIACacheablePropertyValue(
					UIAHandler.UIA_HeadingLevelPropertyId
				) <= UIAHandler.HeadingLevel6
				# But not for apps such as Calculator where doing so results in confusing user experience.
				and obj.appModule.appName != "calculator"
			):
				clsList.insert(0, XAMLHeading)
		except COMError:
			pass

	# Find out if log recording is possible.
	# This will work if debug logging is on and/or tracing apps and/or events is specified.
	trackedEvents: set[str] = set()
	trackedApps: set[str] = set()

	def recordLog(self, obj: Any, event: Optional[str]) -> bool:
		if not isinstance(obj, UIA):
			return False
		eventsTracked = len(self.trackedEvents) > 0
		appsTracked = len(self.trackedApps) > 0
		# Log properties based on the following truth table/conditional statements.
		if not eventsTracked and not appsTracked:
			return log.isEnabledFor(log.DEBUG)
		elif eventsTracked and not appsTracked:
			return event in self.trackedEvents
		elif not eventsTracked and appsTracked:
			return obj.appModule.appName in self.trackedApps
		# Just in case an event/app combo is specified.
		else:
			return event in self.trackedEvents and obj.appModule.appName in self.trackedApps

	# Record UIA property info about an object if told to do so.
	def uiaDebugLogging(self, obj: Any, event: Optional[str] = None) -> None:
		if self.recordLog(obj, event):
			info: list[str] = [f"object: {repr(obj)}"]
			info.append(f"name: {obj.name}")
			if not event:
				event = "no event specified"
			info.append(f"event: {event}")
			if event == "valueChange":
				info.append(f"value: {obj.value}")
			elif event == "stateChange":
				# Parts copied from NVDA Core's default navigator object dev info's state retriever (credit: NV Access).
				try:
					ret = ", ".join(
						stateConsts.get(state) or str(state)
						for state in obj.states)
				except Exception as e:
					ret = "exception: %s" % e
				info.append(f"states: {ret}")
			info.append(f"app module: {obj.appModule}")
			element = obj.UIAElement
			# Sometimes due to timing errors, COM error is thrown
			# when trying to obtain Automation Id from the underlying UIA element.
			# To keep an eye on this, use cached Automation Id
			# rather than fetching UIAAutomationId property directly.
			try:
				info.append(f"Automation Id: {element.cachedAutomationId}")
			except COMError:
				info.append("Automation Id: not found")
			info.append(f"class name: {element.cachedClassName}")
			if log.isEnabledFor(log.DEBUG):
				logger = log.debug
			else:
				logger = log.info
			logger(u"W10: UIA {debuginfo}".format(debuginfo=", ".join(info)))

	def event_nameChange(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "nameChange")
		# NVDA Core issue 5641: try catching virtual desktop switch event,
		# which will result in name change for the desktop object.
		# To be taken care of by NVDA Core, and for older releases, let the add-on handle it for a time.
		# This may degrade performance and/or cause NVDA to become verbose in situations other than
		# virtual desktop switch, so exercise discretion.
		if obj.windowClassName == "#32769":
			if log.isEnabledFor(log.DEBUG):
				log.debug(f"W10: possible desktop name change from {obj}, app module: {obj.appModule}")
			# CSRSS: Client/Server Runtime Subsystem (Windows subsystem process/desktop object)
			if obj.appModule.appName == "csrss":
				import wx
				# Even with desktop name change handler added,
				# older Windows releases won't support this properly.
				# Properly supported in Windows 10 1909.
				if not hasattr(eventHandler, "handlePossibleDesktopNameChange"):
					wx.CallLater(500, ui.message, obj.name)
		nextHandler()

	def event_valueChange(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "valueChange")
		nextHandler()

	def event_stateChange(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "stateChange")
		nextHandler()

	def event_descriptionChange(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "descriptionChange")
		nextHandler()

	def event_UIA_controllerFor(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "controllerFor")
		nextHandler()

	def event_liveRegionChange(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "liveRegionChange")
		# No, do not let Start menu size be announced.
		# Moved from Shell Experience Host in 2018 as a different app hosts this control in build 18282.
		if isinstance(obj, UIA) and obj.UIAAutomationId == "FrameSizeAccessibilityField":
			return
		nextHandler()

	def event_UIA_elementSelected(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "elementSelected")
		nextHandler()

	def event_UIA_systemAlert(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "systemAlert")
		nextHandler()

	def event_UIA_window_windowOpen(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "windowOpen")
		nextHandler()

	def event_UIA_notification(
			self, obj, nextHandler,
			notificationKind=None, notificationProcessing=None, displayString=None, activityId=None
	):
		# Introduced in Version 1709, to be treated as a notification event.
		self.uiaDebugLogging(obj, "notification")
		if isinstance(obj, UIA) and log.isEnabledFor(log.DEBUG):
			log.debug(
				"W10: UIA notification: "
				f"sender: {obj.UIAElement}, "
				f"notification kind: {notificationKind}, "
				f"notification processing: {notificationProcessing}, "
				f"display string: {displayString}, "
				f"activity Id: {activityId}"
			)
			# Play a debug tone if and only if notifications come from somewhere other than the active app
			# and NVDA was restarted with debug logging mode.
			if obj.appModule != api.getFocusObject().appModule and globalVars.appArgs.debugLogging:
				import tones
				# For debugging purposes.
				tones.beep(500, 100)
		# In recent versions of Word 365, notification event is used to announce editing functions,
		# some of them being quite anoying.
		if obj.appModule.appName == "winword" and activityId in ("AccSN1", "AccSN2"):
			return
		# Do not allow notification to be announced if "report notifications" is off.
		if not config.conf["presentation"]["reportHelpBalloons"]:
			return
		nextHandler()

	def event_UIA_dragStart(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragStart")
		nextHandler()

	def event_UIA_dragCancel(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragCancel")
		nextHandler()

	def event_UIA_dragComplete(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragComplete")
		# Announce the new drop location by faking a gain focus event.
		eventHandler.queueEvent("gainFocus", obj)
		nextHandler()

	def event_UIA_dropTargetDragEnter(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dropTargetDragEnter")
		nextHandler()

	def event_UIA_dropTargetDragLeave(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dropTargetDragLeave")
		nextHandler()

	def event_UIA_dropTargetDropped(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dropTargetDropped")
		# Unlike drag complete event, it is something else that raises this event
		# but NVDA records the correct focused element, so fake a gain focus event.
		eventHandler.queueEvent("gainFocus", api.getFocusObject())
		nextHandler()

	def event_UIA_toolTipOpened(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "tooltipOpened")
		nextHandler()

	def event_UIA_itemStatus(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "itemStatus")
		nextHandler()

	def event_textChange(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "textChange")
		nextHandler()

	def event_UIA_layoutInvalidated(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "layoutInvalidated")
		if log.isEnabledFor(log.DEBUG):
			log.debug(f"W10: list item count: {obj.childCount}")
		# Forget it if no suggestions are present.
		# This may happen if this event is fired prior to controller for event.
		if obj.childCount == 0:
			return
		# Limit this event handler to proper suggestions list view.
		if obj.UIAAutomationId != "SuggestionsList":
			return
		focus = api.getFocusObject()
		focusControllerFor = focus.controllerFor
		# In some cases, suggestions list fires layout invalidated event repeatedly.
		# This is the case with Microsoft Store's search field.
		import speech
		speech.cancelSpeech()
		if len(focusControllerFor) and focusControllerFor[0].appModule is obj.appModule and obj.firstChild.name:
			focus._layoutInvalidatedReportSuggestionsCount()
		nextHandler()
