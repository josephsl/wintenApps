# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2019-2023 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Originally copyright 2016-2021 Joseph Lee, released under GPL

# Several hacks related to Settings app, some of which are part of NVDA Core.
# Settings app is a UIA world, hence no instance checks.

from typing import Callable
# Extends NVDA Core's System Settings app module.
from nvdaBuiltin.appModules.systemsettings import AppModule
import winVersion
import speech
from NVDAObjects.UIA import UIA
from NVDAObjects import NVDAObject


# App module class comes from built-in System Settings app module but Mypy doesn't know that.
class AppModule(AppModule):  # type: ignore[no-redef]

	def event_liveRegionChange(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# Workarounds for Windows 10
		if winVersion.getWinVer() < winVersion.WIN11 and isinstance(obj, UIA):
			automationId = obj.UIAAutomationId
			# Except for specific cases, announce all live regions.
			# Announce individual update progress (preferably only once per update stage).
			if "ApplicableUpdate" in automationId:
				# Do not announce status text itself.
				if automationId.endswith("_ContextDescriptionTextBlock"):
					return
				# Update title repeats while the update is downloaded and installed.
				if automationId.endswith("_DescriptionTextBlock"):
					# #71: NVDA is told to announce live regions to the end by default,
					# which results in screen content and speech getting out of sync.
					# However do not cut off other live regions when action button appears next to updates list
					# which is the sibling of the grandparent object (actual updates list element).
					# Update action button appears if the system is up to date or an action is required.
					# However attribute error may result if "update action" button is not a UIA element.
					try:
						if "UpdateActionButton" not in obj.parent.parent.next.UIAAutomationId:
							speech.cancelSpeech()
					except AttributeError:
						pass
		nextHandler()

	def event_nameChange(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# Applies to Windows 11
		if isinstance(obj, UIA):
			if "ApplicableUpdate" in obj.UIAAutomationId:
				import ui
				try:
					# Announce updated screen content as long as update action control is not shown.
					# Simple previous object must be used as previous object returns an unusable button.
					if "UpdateActionButton" not in obj.parent.parent.parent.simplePrevious.UIAAutomationId:
						speech.cancelSpeech()
					ui.message(" ".join([element.name for element in obj.parent.children]))
				except AttributeError:
					pass
		nextHandler()

	def event_focusEntered(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# Applies to Windows 11
		if isinstance(obj, UIA):
			if obj.UIAAutomationId in (
				"SystemSettings_MusUpdate_AvailableUpdatesList2_ListView",  # Windows 11 22H2/23H2
			):
				import UIAHandler
				for updateEntry in obj.children:
					updateStatus = updateEntry.simpleFirstChild.simpleLastChild
					try:
						UIAHandler.handler.removeEventHandlerGroup(
							updateStatus.UIAElement, UIAHandler.handler.localEventHandlerGroup
						)
						UIAHandler.handler.addEventHandlerGroup(
							updateStatus.UIAElement, UIAHandler.handler.localEventHandlerGroup
						)
					except NotImplementedError:
						pass
		nextHandler()
