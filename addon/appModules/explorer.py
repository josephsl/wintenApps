# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2026 NV Access Limited, Joseph Lee, Łukasz Golonka, Julien Cochuyt
# This file may be used under the terms of the GNU General Public License, version 2 or later, as modified by the NVDA license.
# For full terms and any additional permissions, see the NVDA license file: https://github.com/nvaccess/nvda/blob/master/copying.txt

# Provides additional routines on top of the built-in File Explorer app module.

from collections.abc import Callable
# Flake8 F403: detect other add-ons that overrode File Explorer app module.
from nvdaBuiltin.appModules.explorer import *  # NOQA: F403
from nvdaBuiltin.appModules.explorer import AppModule as CoreAppModule
import ui
from NVDAObjects import NVDAObject
import UIAHandler
import versionInfo


# Let NVDA work with its own File Explorer app module in 2025.2.
# Don't worry about "cls" type.
def nvda251applicable(cls):  # type: ignore
	return CoreAppModule if (versionInfo.version_year, versionInfo.version_major) >= (2025, 2) else cls


@nvda251applicable
class AppModule(CoreAppModule):
	def shouldProcessUIANotificationEvent(
		self,
		sender: UIAHandler.UIA.IUIAutomationElement,
		notificationKind: int | None = None,
		notificationProcessing: int | None = None,
		displayString: str = "",
		activityId: str = "",
	) -> bool:
		# NVDA Core issue 17841: announce window restore/maximize/snap states.
		# Resolved in NVDA 2025.2.
		if activityId == "Windows.Shell.SnapComponent.SnapHotKeyResults":
			return True
		return bool(UIAHandler.handler.getNearestWindowHandle(sender))

	def event_UIA_notification(
		self,
		obj: NVDAObject,
		nextHandler: Callable[[], None],
		notificationKind: int | None = None,
		notificationProcessing: int | None = None,
		displayString: str | None = None,
		activityId: str | None = None,
	) -> None:
		# NVDA Core issues 17841 and 18175: announce window states across apps (Windows 11 24H2 and later).
		# These messages come from a File Explorer (shell) element and there is no native window handle.
		# Resolved in NVDA 2025.2.
		if activityId == "Windows.Shell.SnapComponent.SnapHotKeyResults":
			ui.message(displayString)
			return
		nextHandler()
