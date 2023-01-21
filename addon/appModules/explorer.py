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


# Suppress incorrect Win 10 Task switching window focus
class MultitaskingViewFrameWindow(UIA):
	shouldAllowUIAFocusEvent=False


# Suppress focus ancestry for task switching list items if alt is held down (alt+tab)
class MultitaskingViewFrameListItem(UIA):

	def _get_container(self):
		if winUser.getAsyncKeyState(winUser.VK_MENU)&32768:
			return api.getDesktopObject()
		else:
			return super(MultitaskingViewFrameListItem,self).container


# Support for Win8 start screen search suggestions.
class SuggestionListItem(UIA):

	def event_UIA_elementSelected(self):
		speech.cancelSpeech()
		if api.setNavigatorObject(self, isFocus=True):
			self.reportFocus()
			super().event_UIA_elementSelected()


# Windows 8 hack: Class to disable incorrect focus on windows 8 search box (containing the already correctly focused edit field)
class SearchBoxClient(IAccessible):
	shouldAllowIAccessibleFocusEvent=False


# Class for menu items  for Windows Places and Frequently used Programs (in start menu)
# Also used for desktop items
class SysListView32EmittingDuplicateFocusEvents(IAccessible):

	# #474: When focus moves to these items, an extra focus is fired on the parent
	# However NVDA redirects it to the real focus.
	# But this means double focus events on the item, so filter the second one out
	# #2988: Also seen when coming back to the Windows 7 desktop from different applications.
	def _get_shouldAllowIAccessibleFocusEvent(self):
		res = super().shouldAllowIAccessibleFocusEvent
		if not res:
			return False
		focus = eventHandler.lastQueuedFocusObject
		if type(focus)!=type(self) or (self.event_windowHandle,self.event_objectID,self.event_childID)!=(focus.event_windowHandle,focus.event_objectID,focus.event_childID):
			return True
		return False

class NotificationArea(IAccessible):
	"""The Windows notification area, a.k.a. system tray.
	"""
	lastKnownLocation = None

	def event_gainFocus(self):
		NotificationArea.lastKnownLocation = self.location
		if mouseHandler.lastMouseEventTime < time.time() - 0.2:
			# This focus change was not caused by a mouse event.
			# If the mouse is on another systray control, the notification area toolbar will rudely
			# bounce the focus back to the object under the mouse after a brief pause.
			# Moving the mouse to the focus object isn't a good solution because
			# sometimes, the focus can't be moved away from the object under the mouse.
			# Therefore, move the mouse out of the way.
			if self.location:
				systrayLeft, systrayTop, systrayWidth, systrayHeight = self.location
				mouseLeft, mouseTop = winUser.getCursorPos()
				if (
					systrayLeft <= mouseLeft <= systrayLeft + systrayWidth
					and systrayTop <= mouseTop <= systrayTop + systrayHeight
				):
					winUser.setCursorPos(0, 0)

		if self.role == controlTypes.Role.TOOLBAR:
			# Sometimes, the toolbar itself receives the focus instead of the focused child.
			# However, the focused child still has the focused state.
			for child in self.children:
				if child.hasFocus:
					# Redirect the focus to the focused child.
					eventHandler.executeEvent("gainFocus", child)
					return
			# We've really landed on the toolbar itself.
			# This was probably caused by moving the mouse out of the way in a previous focus event.
			# This previous focus event is no longer useful, so cancel speech.
			speech.cancelSpeech()

		if eventHandler.isPendingEvents("gainFocus"):
			return
		super(NotificationArea, self).event_gainFocus()


class ExplorerToolTip(ToolTip):

	def shouldReport(self):
		# Avoid reporting systray tool-tips if their text equals the focused systray icon name (#6656)

		# Don't bother checking if reporting of tool-tips is disabled
		if not config.conf["presentation"]["reportTooltips"]:
			return False

		focus = api.getFocusObject()

		# Report if either
		#  - the mouse has just moved
		#  - the focus is not in the systray
		#  - we do not know (yet) where the systray is located
		if (
			mouseHandler.lastMouseEventTime >= time.time() - 0.2
			or not isinstance(focus, NotificationArea)
			or NotificationArea.lastKnownLocation is None
		):
			return True

		# Report if the mouse is indeed located in the systray
		systrayLeft, systrayTop, systrayWidth, systrayHeight = NotificationArea.lastKnownLocation
		mouseLeft, mouseTop = winUser.getCursorPos()
		if (
			systrayLeft <= mouseLeft <= systrayLeft + systrayWidth
			and systrayTop <= mouseTop <= systrayTop + systrayHeight
		):
			return True

		# Report is the next are different
		if focus.name != self.name:
			return True

		# Do not report otherwise
		return False

	def event_show(self):
		if self.shouldReport():
			super().event_show()


class GridTileElement(UIA):

	role=controlTypes.Role.TABLECELL

	def _get_description(self):
		name=self.name
		descriptionStrings=[]
		for child in self.children:
			description=child.basicText
			if not description or description==name: continue
			descriptionStrings.append(description)
		return " ".join(descriptionStrings)
		return description


class GridListTileElement(UIA):
	role=controlTypes.Role.TABLECELL
	description=None


class GridGroup(UIA):
	"""A group in the Windows 8 Start Menu.
	"""
	presentationType=UIA.presType_content

	# Normally the name is the first tile which is rather redundant
	# However some groups have custom header text which should be read instead
	def _get_name(self):
		child = self.firstChild
		if isinstance(child, UIA):
			if child.UIAAutomationId == "GridListGroupHeader":
				return child.name


class ImmersiveLauncher(UIA):
	# When the Windows 8 start screen opens, focus correctly goes to the first tile, but then incorrectly back to the root of the window.
	# Ignore focus events on this object.
	shouldAllowUIAFocusEvent=False


class StartButton(IAccessible):
	"""For Windows 8.1 and 10 Start buttons to be recognized as proper buttons and to suppress selection announcement."""

	role = controlTypes.Role.BUTTON

	def _get_states(self):
		# #5178: Selection announcement should be suppressed.
		# Borrowed from Mozilla objects in NVDAObjects/IAccessible/Mozilla.py.
		states = super(StartButton, self).states
		states.discard(controlTypes.State.SELECTED)
		return states
		
CHAR_LTR_MARK = u'\u200E'
CHAR_RTL_MARK = u'\u200F'
class UIProperty(UIA):
	#Used for columns in Windows Explorer Details view.
	#These can contain dates that include unwanted left-to-right and right-to-left indicator characters.
	
	def _get_value(self):
		value = super(UIProperty, self).value
		if value is None:
			return value
		return value.replace(CHAR_LTR_MARK,'').replace(CHAR_RTL_MARK,'')

class ReadOnlyEditBox(IAccessible):
#Used for read-only edit boxes in a properties window.
#These can contain dates that include unwanted left-to-right and right-to-left indicator characters.

	def _get_windowText(self):
		windowText = super(ReadOnlyEditBox, self).windowText
		if windowText is not None:
			return windowText.replace(CHAR_LTR_MARK,'').replace(CHAR_RTL_MARK,'')
		return windowText


class MetadataEditField(RichEdit50):
	""" Used for metadata edit fields in Windows Explorer in Windows 7.
	By default these fields would use ITextDocumentTextInfo ,
	but to avoid Windows Explorer crashes we need to use EditTextInfo here. """
	@classmethod
	def _get_TextInfo(cls):
		if winVersion.getWinVer() <= winVersion.WIN7_SP1:
			cls.TextInfo = EditTextInfo
		else:
			cls.TextInfo = super().TextInfo
		return cls.TextInfo


class WorkerW(IAccessible):
	def event_gainFocus(self):
		# #6671: Normally we do not allow WorkerW thread to send gain focus event,
		# as it causes 'pane" to be announced when minimizing windows or moving to desktop.
		# However when closing Windows 7 Start Menu in some  cases
		# focus lands  on it instead of the focused desktop item.
		# Simply ignore the event if running on anything other than Win 7.
		if winVersion.getWinVer() > winVersion.WIN7_SP1:
			return
		if eventHandler.isPendingEvents("gainFocus"):
			return
		if self.simpleFirstChild:
			# If focus is not going to be moved autotically
			# we need to forcefully move it to the focused desktop item.
			# As we are interested in the first focusable object below the pane use simpleFirstChild.
			self.simpleFirstChild.setFocus()
			return
		super().event_gainFocus()


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
