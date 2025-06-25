# Voice access
# Part of Windows App Essentials collection
# Copyright 2022-2025 Joseph Lee, released under GPL

# Support for Voice access on Windows 11.

from collections.abc import Callable
import appModuleHandler
import ui
import winUser
from NVDAObjects import NVDAObject
from winAPI.types import HWNDValT
import UIAHandler


class AppModule(appModuleHandler.AppModule):
	def isGoodUIAWindow(self, hwnd: HWNDValT) -> bool:
		# #72: allow proper mouse and touch interaction from main Voice access interface.
		# Resolved in NVDA 2025.2.
		if winUser.getClassName(hwnd) == "Voice access":
			return True
		return False

	def shouldProcessUIANotificationEvent(
		self,
		sender: UIAHandler.UIA.IUIAutomationElement,
		notificationKind: int | None = None,
		notificationProcessing: int | None = None,
		displayString: str = "",
		activityId: str = "",
	) -> bool:
		# Say "yes" so microphone status, dictated text, and others can be announced.
		# Resolved in NVDA 2025.2.
		return True

	def event_UIA_notification(
		self,
		obj: NVDAObject,
		nextHandler: Callable[[], None],
		notificationKind: int | None = None,
		notificationProcessing: int | None = None,
		displayString: str | None = None,
		activityId: str | None = None,
	):
		# NVDA Core issue 16862: report Voice access messages such as microphone toggle from everywhere.
		# Resolved in NVDA 2025.2.
		if displayString is not None:
			ui.message(displayString)
