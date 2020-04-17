# Windows 10 controls repository
# Copyright 2015-2020 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10.

import globalPluginHandler
import controlTypes
import ui
from NVDAObjects.UIA import UIA, SearchField, Dialog
from NVDAObjects.behaviors import EditableTextWithSuggestions
import api
import nvwave
import config
import queueHandler
import eventHandler
import globalVars
import UIAHandler
from logHandler import log
import winVersion
import addonHandler
addonHandler.initTranslation()

# #52: forget everything if the current release is not a supported version of Windows 10.
# NVDA 2019.2 includes a handy Windows 10 version check function.
W10AddonSupported = winVersion.isWin10(version=1903)

# Extra UIA constants
UIA_Drag_DragStartEventId = 20026
UIA_Drag_DragCancelEventId = 20027
UIA_Drag_DragCompleteEventId = 20028
UIA_DropTarget_DragEnterEventId = 20029
UIA_DropTarget_DragLeaveEventId = 20030
UIA_DropTarget_DroppedEventId = 20031
UIA_Text_TextChangedEventId = 20015

# For convenience.
W10Events = {
	UIA_Drag_DragStartEventId: "UIA_dragStart",
	UIA_Drag_DragCancelEventId: "UIA_dragCancel",
	UIA_Drag_DragCompleteEventId: "UIA_dragComplete",
	UIA_DropTarget_DragEnterEventId: "UIA_dragEnter",
	UIA_DropTarget_DragLeaveEventId: "UIA_dragLeave",
	UIA_DropTarget_DroppedEventId: "UIA_dragDropped",
	UIA_Text_TextChangedEventId: "textChange"
}

# Additional dialogs not recognized by NVDA itself.
UIAAdditionalDialogClassNames = ["Popup"]

# General UIA controller for edit field.
# Used as a base class for controls such as Mail's composition window, search fields and such.
class UIAEditableTextWithSuggestions(EditableTextWithSuggestions, UIA):

	def event_UIA_controllerFor(self):
		# Obtain controller for property directly instead of relying on focused control.
		if len(self.controllerFor)>0:
			self.event_suggestionsOpened()
		else:
			self.event_suggestionsClosed()

# Search fields.
# Unlike the Core implementation, this class announces suggestion count, to be incorporated into NVDA later.
class SearchField(SearchField):

	def event_suggestionsOpened(self):
		super(SearchField, self).event_suggestionsOpened()
		# Announce number of items found (except in Start search box where the suggestions are selected as user types).
		# Oddly, Edge's address omnibar returns 0 for suggestion count when there are clearly suggestions (implementation differences).
		# Because inaccurate count could be announced (when users type, suggestion count changes), thus announce this if position info reporting is enabled.
		if config.conf["presentation"]["reportObjectPositionInformation"]:
			if self.UIAElement.cachedAutomationID == "TextBox" or self.UIAElement.cachedAutomationID == "SearchTextBox" and self.appModule.appName not in ("searchui", "searchapp"):
				# Item count must be the last one spoken.
				suggestionsCount = self.controllerFor[0].childCount
				suggestionsMessage = "1 suggestion" if suggestionsCount == 1 else "%s suggestions"%suggestionsCount
				queueHandler.queueFunction(queueHandler.eventQueue, ui.message, suggestionsMessage)


# Various XAML headings (Settings app, for example) introduced in Version 1803.
class XAMLHeading(UIA):

	def _get_role(self):
		# Heading levels are 8005x, control types heading levels are 4x, therefore the below object role formula.
		return self._getUIACacheablePropertyValue(UIAHandler.UIA_HeadingLevelPropertyId) - 80010


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# Don't do anything unless this is Windows 10.
		# #52: and this is a supported build.
		if not W10AddonSupported: return
		# #20: don't even think about proceeding in secure screens.
		# #40: skip over the rest if appx is in effect.
		if globalVars.appArgs.secure or config.isAppX: return
		# Add a series of events instead of doing it one at a time.
		# Some events are only available in a specific build range and/or while a specific version of IUIAutomation interface is in use.
		log.debug("W10: adding additional events")
		for event, name in W10Events.items():
			if event not in UIAHandler.UIAEventIdsToNVDAEventNames:
				UIAHandler.UIAEventIdsToNVDAEventNames[event] = name
				UIAHandler.handler.clientObject.addAutomationEventHandler(event,UIAHandler.handler.rootElement,UIAHandler.TreeScope_Subtree,UIAHandler.handler.baseCacheRequest,UIAHandler.handler)
				log.debug(f"W10: added event ID {event}, assigned to {name}")
		# Allow NVDA to recognize more dialogs, especially ones that are not advertising themselves as such.
		for dialogClassName in UIAAdditionalDialogClassNames:
			if dialogClassName not in UIAHandler.UIADialogClassNames:
				log.debug(f"W10: adding class name {dialogClassName} to known dialog class names")
				UIAHandler.UIADialogClassNames.append(dialogClassName)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# There's no point looking at non-UIA objects.
		# Also because this add-on might be turned on "accidentally" in earlier Windows releases, including unsupported Windows 10 builds...
		if not (isinstance(obj, UIA) and W10AddonSupported):
			return
		# Somehow, search field finder raises COM error, so put the bulk of this method inside a try block.
		try:
			# Windows that are really dialogs.
			# Some dialogs, although listed as a dialog thanks to UIA class name, does not advertise the proper role of dialog.
			if obj.UIAElement.cachedClassName in UIAHandler.UIADialogClassNames and Dialog not in clsList:
				clsList.insert(0, Dialog)
				return
			# Search field that does raise controller for event.
			# Although basic functionality is included in NVDA 2017.3, added enhancements such as announcing suggestion count.
			if obj.UIAElement.cachedAutomationID in ("SearchTextBox", "TextBox"):
				# NVDA 2017.3 includes a dedicated search box over class in searchui to deal with search term announcement problem.
				# Because the add-on version deals with focus comparison, let all search fields go through this check as much as possible except for specific apps.
				if obj.appModule.appName not in ("searchui", "searchapp"):
					clsList.insert(0, SearchField)
					return
			# A dedicated version for Mail app's address/mention suggestions.
			elif obj.UIAElement.cachedAutomationID == "RootFocusControl":
				clsList.insert(0, UIAEditableTextWithSuggestions)
				return
			# Recognize headings as reported by XAML (build 17134 and later).
			elif obj._getUIACacheablePropertyValue(UIAHandler.UIA_HeadingLevelPropertyId) > UIAHandler.HeadingLevel_None:
				clsList.insert(0, XAMLHeading)
		except:
			pass

	# Find out if log recording is possible.
	# This will work if debug logging is on and/or tracing apps and/or events is specified.
	trackedEvents = set()
	trackedApps = set()

	def recordLog(self, obj, event):
		if not isinstance(obj, UIA):
			return False
		eventsTracked = len(self.trackedEvents) > 0
		appsTracked = len(self.trackedApps) > 0
		# Log properties based on the following truth table/conditional statements.
		if not eventsTracked and not appsTracked:
			return globalVars.appArgs.debugLogging
		elif eventsTracked and not appsTracked:
			return event in self.trackedEvents
		elif not eventsTracked and appsTracked:
			return obj.appModule.appName in self.trackedApps
		# Just in case an event/app combo is specified.
		else:
			return event in self.trackedEvents and obj.appModule.appName in self.trackedApps

	# Record UIA property info about an object if told to do so.
	def uiaDebugLogging(self, obj, event=None):
		if self.recordLog(obj, event):
			info = [f"object: {repr(obj)}"]
			info.append(f"name: {obj.name}")
			if not event:
				event = "no event specified"
			info.append(f"event: {event}")
			info.append(f"app module: {obj.appModule}")
			element = obj.UIAElement
			info.append(f"automation Id: {element.cachedAutomationID}")
			info.append(f"class name: {element.cachedClassName}")
			if event == "controllerFor":
				info.append(f"controller for count: {len(obj.controllerFor)}")
			elif event == "tooltipOpened":
				info.append(f"framework Id: {element.cachedFrameworkId}")
			elif event == "itemStatus":
				info.append(f"item status: {element.currentItemStatus}")
			if globalVars.appArgs.debugLogging: logger = log.debug
			else: logger = log.info
			logger(u"W10: UIA {debuginfo}".format(debuginfo = ", ".join(info)))

	def event_nameChange(self, obj, nextHandler):
		# NVDA Core issue 5641: try catching virtual desktop switch event, which will result in name change for the desktop object.
		# To be taken care of by NVDA Core, and for older releases, let the add-on handle it for a time.
		# This may degrade performance and/or cause NVDA to become verbose in situations other than virtual desktop switch, so exercise discretion.
		if obj.windowClassName == "#32769":
			if globalVars.appArgs.debugLogging:
				import tones
				tones.beep(512, 50)
				log.debug(f"W10: possible desktop name change from {obj}, app module: {obj.appModule}")
			# CSRSS: Client/Server Runtime Subsystem (Windows subsystem process/desktop object)
			if obj.appModule.appName == "csrss":
				import wx
				# Even with desktop name change handler added, older Windows 10 releases won't support this properly.
				if (not hasattr(eventHandler, "handlePossibleDesktopNameChange") or (hasattr(eventHandler, "handlePossibleDesktopNameChange") and not winVersion.isWin10(version=1903))):
					wx.CallLater(500, ui.message, obj.name)
		self.uiaDebugLogging(obj, "nameChange")
		nextHandler()

	def event_valueChange(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "valueChange")
		nextHandler()

	def event_UIA_controllerFor(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "controllerFor")
		nextHandler()

	def event_liveRegionChange(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "liveRegionChange")
		if isinstance(obj, UIA):
			# No, do not let Start menu size be announced.
			# Moved from Shell Experience Host in 2018 as a different app hosts this control in build 18282.
			if obj.UIAElement.cachedAutomationID == "FrameSizeAccessibilityField": return
			# #50 (NVDA Core issue 8466): certain aria-alert messages.
			if obj.role == controlTypes.ROLE_ALERT:
				if not obj.name and obj.treeInterceptor is not None:
					ui.message(obj.treeInterceptor.makeTextInfo(obj).text)
		nextHandler()

	def event_UIA_elementSelected(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "elementSelected")
		nextHandler()

	def event_UIA_systemAlert(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "systemAlert")
		# NVDA Core issue 8557: for some alerts, text is scattered across its children, so take care of this too.
		if isinstance(obj, UIA):
			if obj.role == controlTypes.ROLE_ALERT:
				if not obj.name and obj.treeInterceptor is not None:
					ui.message(obj.treeInterceptor.makeTextInfo(obj).text)
		nextHandler()

	def event_UIA_window_windowOpen(self, obj, nextHandler):
		# Specifically in order to debug multiple toast announcements.
		self.uiaDebugLogging(obj, "windowOpen")
		# Log which modern keyboard header is active.
		# Although this can be done from modern keyboard app module, that module is destined for NVDA Core, hence do it here.
		if obj.appModule.appName in ("windowsinternal_composableshell_experiences_textinput_inputapp", "textinputhost") and obj.firstChild is not None and globalVars.appArgs.debugLogging:
			log.debug(f"W10: automation ID for currently opened modern keyboard feature is {obj.firstChild.UIAElement.cachedAutomationID}")
		nextHandler()

	def event_UIA_notification(self, obj, nextHandler, notificationKind=None, notificationProcessing=None, displayString=None, activityId=None):
		# Introduced in Version 1709, to be treated as a notification event.
		self.uiaDebugLogging(obj, "notification")
		if isinstance(obj, UIA) and globalVars.appArgs.debugLogging:
			log.debug(f"W10: UIA notification: sender: {obj.UIAElement}, notification kind: {notificationKind}, notification processing: {notificationProcessing}, display string: {displayString}, activity ID: {activityId}")
			# Play a debug tone if and only if notifications come from somewhere other than the active app.
			if obj.appModule != api.getFocusObject().appModule:
				import tones
				# For debugging purposes.
				tones.beep(500, 100)
		# In recent versions of Word 365, notification event is used to announce editing functions, some of them being quite anoying.
		if obj.appModule.appName == "winword" and activityId in ("AccSN1", "AccSN2"):
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
		eventHandler.executeEvent("gainFocus", api.getFocusObject())
		nextHandler()

	def event_UIA_dragEnter(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragEnter")
		nextHandler()

	def event_UIA_dragLeave(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragLeave")
		nextHandler()

	def event_UIA_dragDropped(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragDropped")
		# Announce the new drop location by faking a gain focus event.
		eventHandler.executeEvent("gainFocus", api.getFocusObject())
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
