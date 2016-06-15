# Windows 10 Settings appModuleHandler
# Part of Windows 10 App Essentials
# Copyright 2016 Joseph Lee, released under GPL

# Several hacks related to Settings app.

import appModuleHandler
import ui
import controlTypes

class AppModule(appModuleHandler.AppModule):

	def event_nameChange(self, obj, nextHandler):
		# For now, all name change events will result in items being announced.
		# Prevent repeats, especially if it is part of a progress bar.
		if obj.role != controlTypes.ROLE_PROGRESSBAR:
			ui.message(obj.name)
		nextHandler()
