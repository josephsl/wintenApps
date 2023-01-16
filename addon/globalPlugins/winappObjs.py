# Windows app controls repository
# Copyright 2015-2023 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.

import globalPluginHandler
from NVDAObjects.UIA import UIA, Dialog
import globalVars
import UIAHandler
import winVersion
import scriptHandler
import wx
from winAPI.types import HWNDValT
import addonHandler
addonHandler.initTranslation()


# Ideally this should be part of File Explorer app module but to avoid conflicts with other add-ons...
class TaskbarItem(UIA):

	def _get_itemName(self):
		# Icon name contains open window count if windows are open after a hyphen (-).
		return self.name.rpartition(" - ")[0] if " -" in self.name else self.name

	def announceDragPosition(self):
		import ui
		left = self.previous if isinstance(self.previous, TaskbarItem) else None
		right = self.next if isinstance(self.next, TaskbarItem) else None
		if left and right:
			# Translators: announced when rearranging taskbar icons in Windows 11.
			ui.message(_("{appName} moved between {previousAppName} and {nextAppName}").format(
				appName=self.itemName, previousAppName=left.itemName, nextAppName=right.itemName
			))
		elif left and not right:
			# Translators: announced when rearranging taskbar icons in Windows 11.
			ui.message(_("{appName} moved to end of the apps list").format(appName=self.itemName))
		elif right and not left:
			# Translators: announced when rearranging taskbar icons in Windows 11.
			ui.message(_("{appName} moved to beginning of the apps list").format(appName=self.itemName))

	@scriptHandler.script(gesture="kb:alt+shift+rightArrow")
	def script_moveRight(self, gesture):
		announcePosition = isinstance(self.next, TaskbarItem)
		gesture.send()
		if announcePosition:
			wx.CallAfter(self.announceDragPosition)

	@scriptHandler.script(gesture="kb:alt+shift+leftArrow")
	def script_moveLeft(self, gesture):
		announcePosition = isinstance(self.previous, TaskbarItem)
		gesture.send()
		if announcePosition:
			wx.CallAfter(self.announceDragPosition)


# #82: patch File Explorer app module to add more good UIA window class names in Windows 11 22H2 Moment 2.
# Resolved in NVDA 2023.1.
def isGoodUIAWindow(self, hwnd: HWNDValT) -> bool:
	import winUser
	currentWinVer = winVersion.getWinVer()
	# NVDA Core issue 9204: shell raises window open event for emoji panel in build 18305 and later.
	if (
		currentWinVer >= winVersion.WIN10_1903
		and winUser.getClassName(hwnd) == "ApplicationFrameWindow"
	):
		return True
	# NVDA Core issue 13506: Windows 11 UI elements such as Taskbar should be reclassified as UIA windows,
	# letting NVDA announce shell elements when navigating with mouse and/or touch,
	# notably when interacting with windows labeled "DesktopWindowXamlSource".
	# WORKAROUND UNTIL A PERMANENT FIX IS FOUND ACROSS APPS
	if (
		currentWinVer >= winVersion.WIN11
		# Traverse parents until arriving at the top-level window with the below class names.
		# This is more so for the shell root (first class name), and for others, class name check would work
		# since they are top-level windows for windows shown on screen such as Task View.
		# However, look for the ancestor for consistency.
		and winUser.getClassName(winUser.getAncestor(hwnd, winUser.GA_ROOT)) in (
			# Windows 11 shell UI root, housing various shell elements shown on screen if enabled.
			"Shell_TrayWnd",  # Start, Search, Widgets, other shell elements
			# Top-level window class names from Windows 11 shell features
			"Shell_InputSwitchTopLevelWindow",  # Language switcher
			"XamlExplorerHostIslandWindow",  # Task View and Snap Layouts
			# NVDA Core issue 14539
			# Resolved in NVDA 2023.1.
			"TopLevelWindowForOverflowXamlIsland",  # Redesigned systray overflow in 22H2 Moment 2
		)
		# NVDA Core issue 13717: on some systems, Windows 11 shell elements are reported as IAccessible,
		# notably Start button, causing IAccessible handler to report attribute error when handling events.
		and winUser.getClassName(hwnd) != "Start"
	):
		return True
	return False


# #20: don't even think about proceeding in secure screens.
def disableInSecureMode(cls):
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super().__init__()
		from logHandler import log
		import versionInfo
		currentWinVer = winVersion.getWinVer()
		# Report processor architecture at startup.
		# Resolved in NVDA 2023.1.
		if not hasattr(currentWinVer, "processorArchitecture"):
			import platform
			log.info(f"winapps: processor architecture: {platform.machine()}")
		# Is this a Windows 11 22H2 beta build (2262x)?
		if currentWinVer.build in (22622, 22623):
			log.info("winapps: Windows 11 22H2 beta detected")
		# #82: Windows 11 22H2 Moment 2 introduces a redesigned taskbar and systray powered by Win32.
		# NVDA Core issue 14539: touch and mouse interaction does not work when systray overflow window is open.
		# Therefore reclassify the new systray overflow window class name as a good UIA window class.
		# Patch appModules.explorer.AppModule.isGoodUIAWindow with the one defined in this global plugin.
		# Resolved in NVDA 2023.1.
		if (
			currentWinVer >= winVersion.WIN11_22H2
			and (versionInfo.version_year, versionInfo.version_major) < (2023, 1)
		):
			log.debug("winapps: patching File Explorer app module to add additional good uIA windows")
			import appModules.explorer
			appModules.explorer.AppModule.isGoodUIAWindow = isGoodUIAWindow

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		try:
			UIAClassName = obj.UIAElement.cachedClassName
		except AttributeError:
			return
		# Windows that are really dialogs.
		# Some dialogs, although listed as a dialog thanks to UIA class name,
		# does not advertise the proper role of dialog.
		# This is still the case with some dialogs such as restart to install updates dialog in Windows 11.
		if UIAClassName in UIAHandler.UIADialogClassNames and Dialog not in clsList:
			clsList.insert(0, Dialog)
			return
		# Announce rearranged taskbar icons in Windows 11 builds earlier than 25267.
		if (
			obj.appModule.appName == "explorer"
			and UIAClassName == "Taskbar.TaskListButtonAutomationPeer"
			and obj.parent.UIAAutomationId == "TaskbarFrameRepeater"
			and winVersion.getWinVer().build < 25267
		):
			clsList.insert(0, TaskbarItem)
