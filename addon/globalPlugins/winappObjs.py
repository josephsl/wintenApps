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
import addonHandler
addonHandler.initTranslation()


# Ideally this should be part of File Explorer app module but to avoid conflicts with other add-ons...
class TaskbarItem(UIA):

	def _get_itemName(self):
		# Icon name contains open window count if windows are open after a hyphen (-).
		return self.name.rpartition(" - ")[0] if " -" in self.name else self.name

	def _get_positionInfo(self):
		# Position info is included in build 25281.
		positionInfo = super().positionInfo
		if not positionInfo:
			taskbarItems = [item for item in self.parent.children if isinstance(item, TaskbarItem)]
			positionInfo = {
				"indexInGroup": taskbarItems.index(self) + 1, "similarItemsInGroup": len(taskbarItems)
			}
		return positionInfo

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


# #20: don't even think about proceeding in secure screens.
def disableInSecureMode(cls):
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super().__init__()
		from logHandler import log
		import versionInfo
		# Report processor architecture at startup.
		# Resolved in NVDA 2023.1.
		if not hasattr(winVersion.getWinVer(), "processorArchitecture"):
			import platform
			log.info(f"winapps: processor architecture: {platform.machine()}")
		# Is this a Windows 11 22H2 beta build (2262x)?
		if winVersion.getWinVer().build in (22622, 22623):
			log.info("winapps: Windows 11 22H2 beta detected")
		# #82: Windows 11 22H2 Moment 2 introduces a redesigned taskbar and systray powered by Win32.
		# NVDA Core issue 14539: touch and mouse interaction does not work when systray overflow window is open.
		# Therefore reclassify the new systray overflow window class name as a good UIA window class.
		# A better solution is patching File Explorer app module but the below workaround will suffice.
		# Resolved in NVDA 2023.1.
		if (
			winVersion.getWinVer() >= winVersion.WIN11_22H2
			and (versionInfo.version_year, versionInfo.version_major) < (2023, 1)
		):
			log.debug("winapps: adding TopLevelWindowForOverflowXamlIsland to good UIA windows list")
			goodUIAWindowClassNames = list(UIAHandler.goodUIAWindowClassNames)
			goodUIAWindowClassNames.append("TopLevelWindowForOverflowXamlIsland")
			UIAHandler.goodUIAWindowClassNames = tuple(goodUIAWindowClassNames)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if not isinstance(obj, UIA):
			return
		# Windows that are really dialogs.
		# Some dialogs, although listed as a dialog thanks to UIA class name,
		# does not advertise the proper role of dialog.
		# This is still the case with some dialogs such as restart to install updates dialog in Windows 11.
		if obj.UIAElement.cachedClassName in UIAHandler.UIADialogClassNames and Dialog not in clsList:
			clsList.insert(0, Dialog)
			return
		# Announce rearranged taskbar icons in Windows 11 builds earlier than 25267.
		if (
			obj.appModule.appName == "explorer"
			and obj.UIAElement.cachedClassName == "Taskbar.TaskListButtonAutomationPeer"
			and obj.parent.UIAAutomationId == "TaskbarFrameRepeater"
			and winVersion.getWinVer().build < 25267
		):
			clsList.insert(0, TaskbarItem)

	def _detectEmptyFolder(self, obj):
		import controlTypes
		import ui
		clientObject = UIAHandler.handler.clientObject
		condition = clientObject.CreatePropertyCondition(UIAHandler.UIA_ClassNamePropertyId, "UIItemsView")
		uiItemWindow = clientObject.ElementFromHandleBuildCache(
			obj.windowHandle, UIAHandler.handler.baseCacheRequest
		)
		# Instantiate UIA object directly.
		# In order for this to work, a valid UIA pointer must be returned.
		try:
			uiItems = UIA(
				UIAElement=uiItemWindow.FindFirstBuildCache(
					UIAHandler.TreeScope_Descendants, condition, UIAHandler.handler.baseCacheRequest
				)
			)
		except ValueError:
			return
		lastUIItem = uiItems.lastChild
		if isinstance(lastUIItem, UIA) and lastUIItem.role == controlTypes.Role.STATICTEXT and lastUIItem.UIAElement.currentClassName == "Element":
			ui.message(lastUIItem.name)

	def event_nameChange(self, obj, nextHandler):
		# Originally written by Javi Dominguez as part of Explorer Enhancements add-on.
		# Ideally this should be part of File Explorer app module but to avoid conflicts with other add-ons...
		if obj.appModule.appName == "explorer" and obj.windowClassName == "ShellTabWindowClass":
			self._detectEmptyFolder(obj)
		nextHandler()

	def event_focusEntered(self, obj, nextHandler):
		# Originally written by Javi Dominguez as part of Explorer Enhancements add-on.
		# Ideally this should be part of File Explorer app module but to avoid conflicts with other add-ons...
		import controlTypes
		if obj.appModule.appName == "explorer" and isinstance(obj, UIA) and obj.role == controlTypes.Role.LIST and obj.UIAElement.currentClassName == "UIItemsView":
			self._detectEmptyFolder(obj.parent.parent)
		nextHandler()
