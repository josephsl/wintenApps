# Windows Copilot (WebView2)
# Copyright 2025 Joseph Lee, released under GPL

# Workarounds for Windows Copilot WebView2 app interface

import appModuleHandler
import typing
import ui
import NVDAObjects


class AppModule(appModuleHandler.AppModule):  # type: ignore[no-redef]
	def event_liveRegionChange(self, obj: NVDAObjects.NVDAObject, nextHandler: typing.Callable[[], None]):
		# Announce first child object name (actual Copilot response) as the live region name is empty.
		ui.message(obj.firstChild.name)
		nextHandler()
