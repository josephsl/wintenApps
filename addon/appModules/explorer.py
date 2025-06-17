# -*- coding: UTF-8 -*-
# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2025 NV Access Limited, Joseph Lee, Łukasz Golonka, Julien Cochuyt
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Provides additional routines on top of the built-in File Explorer app module.

from typing import Callable
# Flake8 F403: detect other add-ons that overrode File Explorer app module.
from nvdaBuiltin.appModules.explorer import *  # NOQA: F403
import ui
from NVDAObjects import NVDAObject


# App module class comes from built-in File Explorer app module but Ruff doesn't know that.
class AppModule(AppModule):  # NOQA: F405
	def shouldProcessUIANotificationEvent(
		self,
		sender,
		activityId: str = "",
		**kwargs,
	) -> bool:
		# NVDA Core issue 17841: announce window restore/maximize/snap states.
		if activityId == "Windows.Shell.SnapComponent.SnapHotKeyResults":
			return True
		import UIAHandler
		return bool(UIAHandler.handler.getNearestWindowHandle(sender))

	def event_UIA_notification(
		self,
		obj: NVDAObject,
		nextHandler: Callable[[], None],
		displayString: str | None = None,
		activityId: str | None = None,
		**kwargs,
	) -> None:
		# NVDA Core issues 17841 and 18175: announce window states across apps (Windows 11 24H2 and later).
		# These messages come from a File Explorer (shell) element and there is no native window handle.
		if activityId == "Windows.Shell.SnapComponent.SnapHotKeyResults":
			ui.message(displayString)
			return
		nextHandler()
