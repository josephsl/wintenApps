# -*- coding: UTF-8 -*-
# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2023 NV Access Limited, Joseph Lee, Łukasz Golonka, Julien Cochuyt
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Provides additional routines on top of the built-in File Explorer app module.

# Needed in overlay class chooser because just importing typing.List will cause type error to be raised.
import typing
from typing import Dict, Callable
# Flake8 F403: detect other add-ons that overrode File Explorer app module.
from nvdaBuiltin.appModules.explorer import *  # NOQA: F403
import winVersion
import controlTypes
import ui
from NVDAObjects.UIA import UIA
from NVDAObjects import NVDAObject
import scriptHandler
import core
import addonHandler
addonHandler.initTranslation()


class TaskbarItem(NVDAObject):

	def _get_itemName(self) -> str:
		# Icon name contains open window count if windows are open after a hyphen (-).
		return self.name.rpartition(" - ")[0] if " -" in self.name else self.name

	def _get_positionInfo(self) -> Dict[str, int]:
		# Position info is included in build 25281.
		positionInfo = super().positionInfo
		if not positionInfo:
			taskbarItems = [item for item in self.parent.children if isinstance(item, TaskbarItem)]
			# Sometimes an XAML control sits in the middle of the taskbar, making position info meaningless
			# since the taskbar UIA tree will not reveal all of its children including this item.
			# This is noticeable if using input devices other than the keyboard.
			if self in taskbarItems:
				positionInfo = {
					"indexInGroup": taskbarItems.index(self) + 1, "similarItemsInGroup": len(taskbarItems)
				}
		return positionInfo

	def announceDragPosition(self) -> None:
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
	def script_moveRight(self, gesture) -> None:
		announcePosition = winVersion.getWinVer() >= winVersion.WIN11 and isinstance(self.next, TaskbarItem)
		gesture.send()
		if announcePosition:
			core.callLater(1, self.announceDragPosition)

	@scriptHandler.script(gesture="kb:alt+shift+leftArrow")
	def script_moveLeft(self, gesture) -> None:
		announcePosition = winVersion.getWinVer() >= winVersion.WIN11 and isinstance(self.previous, TaskbarItem)
		gesture.send()
		if announcePosition:
			core.callLater(1, self.announceDragPosition)


# App module class comes from built-in File Explorer app module but Mypy doesn't know that.
# Also tell Flake8 that the base AppModule class comes from NVDA Core.
class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: typing.List[NVDAObject]) -> None:
		# Taskbar item enhancements.
		# Windows 10 and 11: taskbar item position.
		# Windows 11 (excluding 25267 to 25346): announced rearranged item position.
		if obj.role == controlTypes.Role.BUTTON and (
			(
				# Windows 10
				obj.windowClassName == "MSTaskListWClass"
				and all(obj.location)
			) or (
				# Windows 11
				isinstance(obj, UIA)
				and obj.UIAElement.cachedClassName == "Taskbar.TaskListButtonAutomationPeer"
				and winVersion.getWinVer().build < 25267
			)
		):
			clsList.insert(0, TaskbarItem)
			return
		# NVDA Core takes care of the rest.
		super().chooseNVDAObjectOverlayClasses(obj, clsList)

	def event_UIA_elementSelected(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# NVDA Core issue 14388: announce File Explorer tab switches (Windows 11 22H2 and later).
		# Resolved in NVDA 2023.2 (remove this method completely).
		import speech
		import braille
		import eventHandler
		# Element selected event fires multiple times due to state changes.
		if (
			obj.role == controlTypes.Role.TAB
			and controlTypes.State.SELECTED in obj.states
			and obj.parent.UIAAutomationId == "TabListView"
			# this is done because 2 selection events are sent for the same object, so to prevent double speaking.
			and not eventHandler.isPendingEvents(eventName="UIA_elementSelected")
		):
			speech.speakObject(obj, reason=controlTypes.OutputReason.FOCUS)
			braille.handler.message(
				braille.getPropertiesBraille(
					name=obj.name,
					role=obj.role,
					states=obj.states,
					positionInfo=obj.positionInfo
				)
			)
		nextHandler()
