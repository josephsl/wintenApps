# Shell Host/quick settings
# Copyright 2024 Joseph Lee, released under GPL

# Workarounds for Windows 11 24H2 quick settings interface

import appModuleHandler
import winUser
from winAPI.types import HWNDValT


class AppModule(appModuleHandler.AppModule):

	def isGoodUIAWindow(self, hwnd: HWNDValT) -> bool:
		# NVDA Core issue 16348: reclassify control center window as UIA to allow mouse/touch interaction.
		if winUser.getClassName(hwnd) == "ControlCenterWindow":
			return True
		return False
