# Shell Host/Action Center
# Copyright 2024 Joseph Lee, released under GPL

# Workarounds for Windows 11 24H2 action center

import appModuleHandler
import winUser
from winAPI.types import HWNDValT


class AppModule(appModuleHandler.AppModule):

	def isGoodUIAWindow(self, hwnd: HWNDValT) -> bool:
		if winUser.getClassName(hwnd) == "ControlCenterWindow":
			return True
		return False
