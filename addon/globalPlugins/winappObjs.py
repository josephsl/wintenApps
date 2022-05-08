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
import winUser
import addonHandler
addonHandler.initTranslation()

# #52: forget everything if the current release is not a supported version of Windows.
# #66: Version 21H2 is divided into three releases: Windows 10, Server 2022, and Windows 11.
# Do not allow running on build 21000 series (Windows 10/11 Insider Preview).
currentWinVer = winVersion.getWinVer()
isAddonSupported = (
	currentWinVer >= winVersion.WIN11 if currentWinVer > winVersion.WINSERVER_2022
	else currentWinVer >= winVersion.WIN10_21H1
)


# Add additional UIA events not included in NVDA Core.
# Specifically to support drag and drop operations.
additionalEvents: dict[int, str] = {
	UIAHandler.UIA_Drag_DragCompleteEventId: "UIA_dragComplete",
	UIAHandler.UIA_DropTarget_DroppedEventId: "UIA_dropTargetDropped",
}


# Add additional property events not included in NVDA Core.
# #69: specifically to support drag drop effect property when Windows 10 Start menu tiles are rearranged.
additionalPropertyEvents: dict[int, str] = {
	UIAHandler.UIA_DragDropEffectPropertyId: "UIA_dragDropEffect"
}


# #72: the following window classes should be recognized as good UIA windows in Windows 11.
w11GoodUIAWindowClassNames: list[str] = [
	"Shell_TrayWnd",  # File Explorer/bottom left (Start, Search, Widgets)/Windows 11 shell UI root
	"MSTaskSwWClass",  # File Explorer/bottom center (Taskbar icons)
	"ReBarWindow32",  # File Explorer/bottom center (Taskbar icons)
	"Button",  # File Explorer/bottom right (notification chevron button)
	"TIPBand",  # File Explorer/bottom right (touch keyboard button)
	"VirtualTouchpad",  # File Explorer/bottom right (virtual touchpad)
	"Shell_InputSwitchTopLevelWindow",  # File Explorer/bottom right (language switcher)
	"TrayNotifyWnd",  # File Explorer/bottom right (system tray)
	"XamlExplorerHostIslandWindow",  # File Explorer/Task View and Snap Layouts
	"CabinetWClass"  # File Explorer/Menu bar
]


# #72/alternate: patch File Explorer module to add more good UIA window class names.
def isGoodUIAWindow(self, hwnd):
	currentWinVer = winVersion.getWinVer()
	# NVDA Core issue 9204: shell raises window open event for emoji panel in build 18305 and later.
	if (
		currentWinVer >= winVersion.WIN10_1903
		and winUser.getClassName(hwnd) == "ApplicationFrameWindow"
	):
		return True
	# NVDA Core issue 13506: Windows 11 Taskbar and other items with the name of "DesktopWindowXamlSource"
	# should be reclassified as UIA windows, not IAccessible, letting NVDA announce shell elements.
	if (
		currentWinVer >= winVersion.WIN11
		and winUser.getClassName(hwnd) in (
			"Shell_TrayWnd",  # File Explorer/bottom left (Start, Search, Widgets)/Windows 11 shell UI root
			"MSTaskSwWClass",  # File Explorer/bottom center (Taskbar icons)
			"ReBarWindow32",  # File Explorer/bottom center (Taskbar icons)
			"Button",  # File Explorer/bottom right (notification chevron button)
			"TIPBand",  # File Explorer/bottom right (touch keyboard button)
			"VirtualTouchpad",  # File Explorer/bottom right (virtual touchpad)
			"Shell_InputSwitchTopLevelWindow",  # File Explorer/bottom right (language switcher)
			"TrayNotifyWnd",  # File Explorer/bottom right (system tray)
			"XamlExplorerHostIslandWindow",  # File Explorer/Task View and Snap Layouts
			"CabinetWClass"  # File Explorer/Menu bar
		)
	):
		return True
	return False


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super().__init__()
		# Don't do anything unless this is Windows 10 or later.
		# #52: and this is a supported build.
		if not isAddonSupported:
			return
		# #20: don't even think about proceeding in secure screens.
		if globalVars.appArgs.secure:
			return
		# Try adding additional events and properties in the constructor.
		# If it fails, try again after NVDA is fully initialized.
		try:
			log.debug("winapps: adding additional events and properties")
			self._addAdditionalUIAEvents()
		except AttributeError:
			log.debug("winapps: UIA handler not ready, delaying until NVDA is fully initialized")
			queueHandler.queueFunction(queueHandler.eventQueue, self._addAdditionalUIAEvents, delay=True)
		# #72: add additional good UIA window class names on Windows 11.
		if winVersion.getWinVer() >= winVersion.WIN11:
			# There are two ways of doing this: globally or at the ap module level.
			# Since the affected elements are shel objects, app module level solution should be part of Explorer.
			patchAppModule = True
			if not patchAppModule:
				# Method 1: add good UIA window class names globally.
				# NVDA Core window class names is a tuple, therefore convert to a list and back.
				log.debug("winapps: adding additional good UIA window class names")
				goodUIAWindowClassNames = list(UIAHandler.goodUIAWindowClassNames) + w11GoodUIAWindowClassNames
				UIAHandler.goodUIAWindowClassNames = tuple(goodUIAWindowClassNames)
				log.debug("winapps: good UIA window class names: {}".format(", ".join(w11GoodUIAWindowClassNames)))
			else:
				# Method 2: patch appModules.explorer.AppModule.isGoodUIAWindow method.
				# Patch the app module method with the one defined in this global plugin.
				log.debug("winapps: patching File Explorer app module to add additional good uIA windows")
				import appModules.explorer
				appModules.explorer.AppModule.isGoodUIAWindow = isGoodUIAWindow

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

	def event_UIA_notification(self, obj, nextHandler, displayString=None, activityId=None, **kwargs):
		# Introduced in Windows 10 1709, to be treated as a notification event.
		# Do not allow notification to be announced if "report notifications" is off.
		if not config.conf["presentation"]["reportHelpBalloons"]:
			return
		# In recent versions of Word 365, notification event is used to announce editing functions,
		# some of them being quite anoying.
		if obj.appModule.appName == "winword" and activityId == "AccSN1":
			return
		# Announce microphone mute status from anywhere in Windows 11.
		if obj.appModule.appName == "explorer" and activityId == "Windows.Shell.CallMuteAnnouncement":
			if api.getFocusObject().appModule != obj.appModule:
				ui.message(displayString)
				return
		# Windows Terminal 1.12.10733 uses notification event for text output, resulting in repetitions.
		# Resolved in NVDA 2022.1, so check for 2021.3.x with a nonexistent attribute in add-on handler
		# as UIA WinConsole object in NVDA 2022.1 will veto this event anyway.
		if obj.appModule.appName == "windowsterminal" and not hasattr(addonHandler, "isCLIParamKnown"):
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
		# Announce drop target effect such as item placement in Start menu and Action center if present.
		dropTargetEffect = obj._getUIACacheablePropertyValue(UIAHandler.UIA_DropTargetDropTargetEffectPropertyId)
		if dropTargetEffect:
			ui.message(dropTargetEffect)
		# Unlike drag complete event, it is something else that raises this event
		# but NVDA records the correct focused element, so fake a gain focus event.
		eventHandler.queueEvent("gainFocus", api.getFocusObject())
		nextHandler()

	def event_UIA_dragDropEffect(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragDropEffect")
		# Report drag and drop effect as communicated by UIA.
		dragDropEffect = obj._getUIACacheablePropertyValue(UIAHandler.UIA_DragDropEffectPropertyId)
		ui.message(dragDropEffect)
		log.debug(f"Winapps: drag drop effect: {dragDropEffect}")
		nextHandler()
