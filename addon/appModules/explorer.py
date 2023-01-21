# -*- coding: UTF-8 -*-
# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2023 NV Access Limited, Joseph Lee, Łukasz Golonka, Julien Cochuyt
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for Windows Explorer (aka Windows shell and renamed to File Explorer in Windows 8).
Provides workarounds for controls such as identifying Start button, notification area and others.
"""

from nvdaBuiltin.appModules.explorer import AppModule
from comtypes import COMError
import time
import appModuleHandler
import controlTypes
import winUser
import winVersion
import api
import speech
import eventHandler
import mouseHandler
from NVDAObjects.IAccessible import IAccessible, List
from NVDAObjects.UIA import UIA
from NVDAObjects.behaviors import ToolTip
from NVDAObjects.window.edit import RichEdit50, EditTextInfo
import config
from winAPI.types import HWNDValT
import scriptHandler
import wx
import addonHandler
addonHandler.initTranslation()


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


class AppModule(AppModule):

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
		# #9204: shell raises window open event for emoji panel in build 18305 and later.
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
				"TopLevelWindowForOverflowXamlIsland",  # Redesigned systray overflow in 22H2
			)
			# NVDA Core issue 13717: on some systems, Windows 11 shell elements are reported as IAccessible,
			# notably Start button, causing IAccessible handler to report attribute error when handling events.
			and winUser.getClassName(hwnd) != "Start"
		):
			return True
		return False
