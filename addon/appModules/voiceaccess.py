# Voice access
# Part of Windows App Essentials collection
# Copyright 2022-2024 Joseph Lee, released under GPL

# Support for Voice access on Windows 11.

import appModuleHandler
import scriptHandler
import ui
import winUser
from NVDAObjects.UIA import UIA, Dialog
from NVDAObjects import NVDAObject
from winAPI.types import HWNDValT


class AppModule(appModuleHandler.AppModule):

	def isGoodUIAWindow(self, hwnd: HWNDValT) -> bool:
		# #72: allow proper mouse and touch interaction from main Voice access interface.
		if winUser.getClassName(hwnd) == "Voice access":
			return True
		return False
