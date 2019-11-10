# Windows 10 controls repository
# Copyright 2015-2019 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10.

import globalPluginHandler
import appModuleHandler
import controlTypes
import ui
from NVDAObjects.UIA import UIA, SearchField, Dialog
from NVDAObjects.behaviors import EditableTextWithSuggestions, ToolTip
import api
import nvwave
import config
import queueHandler
import globalVars
import UIAHandler
from logHandler import log
import winVersion
import addonHandler
addonHandler.initTranslation()

# #52: forget everything if the current release is not a supported version of Windows 10.
# NVDA 2019.2 includes a handy Windows 10 version check function.
W10AddonSupported = winVersion.isWin10(version=1809)

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


# Some context menu items expose position info, which is quite anoying.
class MenuItemNoPosInfo(UIA):

	def _get_states(self):
		# Borrowed from NVDA Core issue 5178 code (fixed provided by the same author).
		states = super(MenuItemNoPosInfo, self).states
		# Add proper state for submenus.
		if self.UIAElement.cachedClassName == "MenuFlyoutSubItem":
			states.add(controlTypes.STATE_HASPOPUP)
		return states

	def _get_positionInfo(self):
		return {}


# For tool tips from universal apps and Edge.
class ToolTip(ToolTip, UIA):

	event_UIA_toolTipOpened=ToolTip.event_show


# Various XAML headings (Settings app, for example) introduced in Version 1803.
class XAMLHeading(UIA):

	def _get_role(self):
		# Heading levels are 8005x, control types heading levels are 4x, therefore the below object role formula.
		return self._getUIACacheablePropertyValue(UIAHandler.UIA_HeadingLevelPropertyId) - 80010


# Patch base app module class so the "real" product name and version can be returned.
# This affects Calculator and many apps, as without this, it returns Windows version or nonsense.
def _setProductInfo(self):
	"""Set productName and productVersion attributes.
	"""
	# Sometimes (I.E. when NVDA starts) handle is 0, so stop if it is the case
	if not self.processHandle:
		raise RuntimeError("processHandle is 0")
	import ctypes
	from fileUtils import getFileVersionInfo
	# Use an internal function for obtaining file name and version for the executable.
	# This is needed in case immersive app package returns an error, dealing with a native app, or a converted desktop app.
	def _getExecutableFileInfo():
		# Create the buffer to get the executable name
		exeFileName = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
		length = ctypes.wintypes.DWORD(ctypes.wintypes.MAX_PATH)
		if not ctypes.windll.Kernel32.QueryFullProcessImageNameW(self.processHandle, 0, exeFileName, ctypes.byref(length)):
			raise ctypes.WinError()
		fileName = exeFileName.value
		fileinfo = getFileVersionInfo(fileName, "ProductName", "ProductVersion")
		return (fileinfo["ProductName"], fileinfo["ProductVersion"])
	# NVDA Core issue 10108: use different paths depending on whether this is an immersive process or not.
	# No need to check for Windows version as this is Windows 10, which guarantees presence of user32.dll::IsImmersiveProcess function.
	# Some apps such as File Explorer says it is an immersive process but error 15700 (no container) is returned, therefore resort to old behavior.
	# Others such as Store version of Office are not truly hosted apps, yet returns an internal version number anyway.
	# For immersive apps, default implementation is too generic - returns Windows version information.
	# Therefore, probe package full name and parse the serialized representation of package info structure.
	length = ctypes.c_uint()
	buf = ctypes.windll.kernel32.GetPackageFullName(self.processHandle, ctypes.byref(length), None)
	packageFullName = ctypes.create_unicode_buffer(buf)
	if ctypes.windll.kernel32.GetPackageFullName(self.processHandle, ctypes.byref(length), packageFullName) == 0:
		# Product name is of the form publisher.name for a hosted app.
		productInfo = packageFullName.value.split("_")
	else:
		# File Explorer and friends which are really native aps.
		productInfo = _getExecutableFileInfo()
	self.productName = productInfo[0]
	self.productVersion = productInfo[1]


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# Don't do anything unless this is Windows 10.
		# #52: and this is a supported build.
		if not W10AddonSupported: return
		# #20: don't even think about proceeding in secure screens.
		# #40: skip over the rest if appx is in effect.
		if globalVars.appArgs.secure or config.isAppX: return
		# Patch base app module so correct product name and version canbe returned for immersive processes.
		# But only do this if this is 2019.2 or earlier.
		if not hasattr(appModuleHandler.AppModule, "_getExecutableFileInfo"):
			log.debug("W10: patching base app module to support obtaining product name and version of hosted apps")
			appModuleHandler.AppModule._setProductInfo = _setProductInfo
		# Add a series of events instead of doing it one at a time.
		# Some events are only available in a specific build range and/or while a specific version of IUIAutomation interface is in use.
		log.debug("W10: adding additional events")
		for event, name in W10Events.items():
			if event not in UIAHandler.UIAEventIdsToNVDAEventNames:
				UIAHandler.UIAEventIdsToNVDAEventNames[event] = name
				UIAHandler.handler.clientObject.addAutomationEventHandler(event,UIAHandler.handler.rootElement,UIAHandler.TreeScope_Subtree,UIAHandler.handler.baseCacheRequest,UIAHandler.handler)
				log.debug("W10: added event ID %s, assigned to %s"%(event, name))
		# Allow NVDA to recognize more dialogs, especially ones that are not advertising themselves as such.
		for dialogClassName in UIAAdditionalDialogClassNames:
			if dialogClassName not in UIAHandler.UIADialogClassNames:
				log.debug("W10: adding class name %s to known dialog class names"%dialogClassName)
				UIAHandler.UIADialogClassNames.append(dialogClassName)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# There's no point looking at non-UIA objects.
		# Also because this add-on might be turned on "accidentally" in earlier Windows releases, including unsupported Windows 10 builds...
		if not (isinstance(obj, UIA) and W10AddonSupported):
			return
		# Windows that are really dialogs.
		# NVDA Core issue 8405: in build 17682 and later, IsDialog property has been added, making comparisons easier.
		# However, don't forget that many users are still using old Windows 10 releases.
		# The most notable case is app uninstall confirmation dialog from Start menu in build 17134 and earlier.
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
		# Menu items should never expose position info (seen in various context menus such as in Edge).
		# Also take care of recognizing submenus across apps.
		elif obj.UIAElement.cachedClassName in ("MenuFlyoutItem", "MenuFlyoutSubItem"):
			clsList.insert(0, MenuItemNoPosInfo)
			return
		# #44: Recognize XAML/UWP tool tips.
		elif obj.UIAElement.cachedClassName == "ToolTip" and obj.UIAElement.cachedFrameworkID == "XAML":
			# Just in case XAML tool tip support is part of NVDA...
			import NVDAObjects.UIA
			if not hasattr(NVDAObjects.UIA, "ToolTip"):
				clsList.insert(0, ToolTip)
				return
		# Recognize headings as reported by XAML (build 17134 and later).
		elif obj._getUIACacheablePropertyValue(UIAHandler.UIA_HeadingLevelPropertyId) > UIAHandler.HeadingLevel_None:
			clsList.insert(0, XAMLHeading)

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
			info = ["object: %s"%repr(obj)]
			info.append("name: %s"%obj.name)
			if not event:
				event = "no event specified"
			info.append("event: %s"%event)
			info.append("app module: %s"%obj.appModule)
			element = obj.UIAElement
			info.append("automation Id: %s"%element.cachedAutomationID)
			info.append("class name: %s"%element.cachedClassName)
			if event == "controllerFor":
				info.append("controller for count: %s"%len(obj.controllerFor))
			elif event == "tooltipOpened":
				info.append("framework Id: %s"%element.cachedFrameworkId)
			elif event == "itemStatus":
				info.append("item status: %s"%element.currentItemStatus)
			if globalVars.appArgs.debugLogging:
				log.debug(u"W10: UIA {debuginfo}".format(debuginfo = ", ".join(info)))
			else:
				log.info(u"W10: UIA {debuginfo}".format(debuginfo = ", ".join(info)))

	def event_nameChange(self, obj, nextHandler):
		# NVDA Core issue 5641: try catching virtual desktop switch event, which will result in name change for the desktop object.
		# To be taken care of by NVDA Core, and for older releases, let the add-on handle it for a time.
		# This may degrade performance and/or cause NVDA to become verbose in situations other than virtual desktop switch, so exercise discretion.
		if obj.windowClassName == "#32769":
			if globalVars.appArgs.debugLogging:
				import tones
				tones.beep(512, 50)
				log.debug("W10: possible desktop name change from %s, app module: %s"%(obj,obj.appModule))
			# CSRSS: Client/Server Runtime Subsystem (Windows subsystem process/desktop object)
			if obj.appModule.appName == "csrss":
				import wx, eventHandler
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
			log.debug("W10: automation ID for currently opened modern keyboard feature is %s"%obj.firstChild.UIAElement.cachedAutomationID)
		nextHandler()

	def event_UIA_notification(self, obj, nextHandler, notificationKind=None, notificationProcessing=None, displayString=None, activityId=None):
		# Introduced in Version 1709, to be treated as a notification event.
		self.uiaDebugLogging(obj, "notification")
		if isinstance(obj, UIA) and globalVars.appArgs.debugLogging:
			log.debug("W10: UIA notification: sender: %s, notification kind: %s, notification processing: %s, display string: %s, activity ID: %s"%(obj.UIAElement,notificationKind,notificationProcessing,displayString,activityId))
			# Play a debug tone if and only if notifications come from somewhere other than the active app.
			if obj.appModule != api.getFocusObject().appModule:
				import tones
				# For debugging purposes.
				tones.beep(500, 100)
		nextHandler()

	def event_UIA_dragStart(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragStart")
		nextHandler()

	def event_UIA_dragCancel(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragCancel")
		nextHandler()

	def event_UIA_dragComplete(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragComplete")
		nextHandler()

	def event_UIA_dragEnter(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragEnter")
		nextHandler()

	def event_UIA_dragLeave(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragLeave")
		nextHandler()

	def event_UIA_dragDropped(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragDropped")
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
