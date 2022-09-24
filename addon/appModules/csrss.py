# Client/Server Runtime Subsystem (Windows subsystem process)
# Copyright 2022 Joseph Lee, released under GPL.

# Specifically designed to handle virtual desktop switches.
# Split from WinAppObjs global plugin in 2022.

import appModuleHandler
import ui
import core


class AppModule(appModuleHandler.AppModule):

	def event_nameChange(self, obj, nextHandler):
		# NVDA Core issue 5641: try catching virtual desktop switch event,
		# which will result in name change for the desktop object.
		if obj.windowClassName == "#32769":
			core.callLater(250, ui.message, obj.name)
		nextHandler()
