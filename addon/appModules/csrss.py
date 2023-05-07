# Client/Server Runtime Subsystem (Windows subsystem process)
# Copyright 2022-2023 Joseph Lee, released under GPL.

# Specifically designed to handle virtual desktop switches.
# Split from WinAppObjs global plugin in 2022.

from typing import Callable
import appModuleHandler
import core
from NVDAObjects import NVDAObject


class AppModule(appModuleHandler.AppModule):

	def event_nameChange(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# NVDA Core issue 5641: try catching virtual desktop switch event,
		# which will result in name change for the desktop object.
		# Do this while NVDA Core itself does not include virtual desktop switch announcement facility.
		import eventHandler
		if obj.windowClassName == "#32769" and not hasattr(eventHandler, "handlePossibleDesktopNameChange"):
			import globalPlugins.winappObjs
			globalPlugins.winappObjs.virtualDesktopName = obj.name
			core.callLater(100, globalPlugins.winappObjs.handlePossibleDesktopNameChange)
		nextHandler()
