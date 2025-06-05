# Voice access
# Part of Windows App Essentials collection
# Copyright 2022-2025 Joseph Lee, released under GPL

# Support for Voice access on Windows 11.

from typing import Callable
import appModuleHandler
import ui
import winUser
from NVDAObjects import NVDAObject
from winAPI.types import HWNDValT


class AppModule(appModuleHandler.AppModule):
	def isGoodUIAWindow(self, hwnd: HWNDValT) -> bool:
		# #72: allow proper mouse and touch interaction from main Voice access interface.
		if winUser.getClassName(hwnd) == "Voice access":
			return True
		return False

	def event_UIA_notification(
		self,
		obj: NVDAObject,
		nextHandler: Callable[[], None],
		displayString: str | None = None,
		**kwargs,
	):
		# NVDA Core issue 16862: report Voice access messages such as microphone toggle from everywhere.
		ui.message(displayString)
