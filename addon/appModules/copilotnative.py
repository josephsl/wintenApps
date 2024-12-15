# Windows Copilot
# Copyright 2025 Joseph Lee, released under GPL

# Workarounds for Windows Copilot interface

from typing import Callable
import appModuleHandler
import ui
from NVDAObjects import NVDAObject


class AppModule(appModuleHandler.AppModule):  # type: ignore[no-redef]
	def event_liveRegionChange(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# Announce first child object name (actual Copilot response) as the live region name is empty.
		ui.message(obj.firstChild.name)
		nextHandler()
