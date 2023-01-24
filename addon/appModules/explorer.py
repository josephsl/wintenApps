# -*- coding: UTF-8 -*-
# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2023 NV Access Limited, Joseph Lee, Łukasz Golonka, Julien Cochuyt
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Provides additional routines on top of the built-in File Explorer app module.

# Flake8 F403: detect other add-ons that overrode File Explorer app module.
from nvdaBuiltin.appModules.explorer import *  # NOQA: F403
import winUser
import winVersion
import controlTypes
import ui
from NVDAObjects.UIA import UIA
import NVDAObjects
from winAPI.types import HWNDValT
import scriptHandler
import wx
import addonHandler
addonHandler.initTranslation()


class TaskbarItem(NVDAObjects.NVDAObject):

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
		announcePosition = winVersion.getWinVer() >= winVersion.WIN11 and isinstance(self.next, TaskbarItem)
		gesture.send()
		if announcePosition:
			wx.CallAfter(self.announceDragPosition)

	@scriptHandler.script(gesture="kb:alt+shift+leftArrow")
	def script_moveLeft(self, gesture):
		announcePosition = winVersion.getWinVer() >= winVersion.WIN11 and isinstance(self.previous, TaskbarItem)
		gesture.send()
		if announcePosition:
			wx.CallAfter(self.announceDragPosition)


# App module class comes from built-in File Explorer app module but Mypy doesn't know that.
# Also tell Flake8 that the base AppModule class comes from NVDA Core.
class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Announce rearranged taskbar icons in Windows 11 builds earlier than 25267.
		if (
			isinstance(obj, UIA)
			and obj.UIAElement.cachedClassName == "Taskbar.TaskListButtonAutomationPeer"
			and obj.parent.UIAAutomationId == "TaskbarFrameRepeater"
			and winVersion.getWinVer().build < 25267
		):
			clsList.insert(0, TaskbarItem)
			return
		# NVDA Core takes care of the rest.
		super().chooseNVDAObjectOverlayClasses(obj, clsList)

	def isGoodUIAWindow(self, hwnd: HWNDValT) -> bool:
		# #82: Windows 11 22H2 Moment 2 introduces a redesigned taskbar and systray powered by Win32.
		# NVDA Core issue 14539: touch and mouse interaction does not work when systray overflow window is open.
		# Therefore reclassify the new systray overflow window class name as a good UIA window class.
		# Resolved in NVDA 2023.1.
		currentWinVer = winVersion.getWinVer()
		if (
			currentWinVer >= winVersion.WIN11_22H2
			# Redesigned systray overflow in 22H2
			and winUser.getClassName(hwnd) == "TopLevelWindowForOverflowXamlIsland"
		):
			return True
		# NVDA Core takes care of the rest.
		return super().isGoodUIAWindow(hwnd)

	def _detectEmptyFolder(self, obj):
		import UIAHandler
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
		# NVDA Core issue 5759: announce empty folder text.
		if (
			isinstance(lastUIItem, UIA)
			and lastUIItem.role == controlTypes.Role.STATICTEXT
			and lastUIItem.UIAElement.currentClassName == "Element"
		):
			ui.message(lastUIItem.name)

	def event_nameChange(self, obj, nextHandler):
		# Originally written by Javi Dominguez as part of Explorer Enhancements add-on.
		if obj.windowClassName == "ShellTabWindowClass":
			self._detectEmptyFolder(obj)
		nextHandler()

	def event_focusEntered(self, obj, nextHandler):
		# Originally written by Javi Dominguez as part of Explorer Enhancements add-on.
		if (
			isinstance(obj, UIA)
			and obj.role == controlTypes.Role.LIST
			and obj.UIAElement.currentClassName == "UIItemsView"
		):
			self._detectEmptyFolder(obj.parent.parent)
		nextHandler()
