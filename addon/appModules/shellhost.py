# Shell Host/quick settings
# Copyright 2024 Joseph Lee, released under GPL

# Workarounds for Windows 11 24H2 quick settings interface
# Quick settings was split from Shell Experience Host in 24H2.

import appModuleHandler
import winUser
from winAPI.types import HWNDValT


class AppModule(appModuleHandler.AppModule):

	def isGoodUIAWindow(self, hwnd: HWNDValT) -> bool:
		# NVDA Core issue 16348: reclassify control center window as UIA to allow mouse/touch interaction.
		# Resolved in NVDA 2024.2.
		if winUser.getClassName(hwnd) == "ControlCenterWindow":
			return True
		return False
