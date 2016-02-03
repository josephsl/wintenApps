# Windows 10 Settings appModuleHandler
# Part of Windows 10 App Essentials
# Copyright 2016 Joseph Lee, released under GPL

# Several hacks related to Settings app.

import appModuleHandler
import ui

class AppModule(appModuleHandler.AppModule):

	def event_nameChange(self, obj, nextHandler):
		# For now, all name change events will result in items being announced.
		ui.message(obj.name)
		nextHandler()
