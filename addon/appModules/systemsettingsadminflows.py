# Windows 10 Settings/Reset This PC
# Part of Windows 10 App Essentials collection
# Copyright 2018-2020 Joseph Lee, released under GPL

# Specific to Reset This PC window in Settings.

import appModuleHandler
import ui
from NVDAObjects.UIA import UIA


class AppModule(appModuleHandler.AppModule):

	def event_nameChange(self, obj, nextHandler):
		if isinstance(obj, UIA) and obj.UIAAutomationId == "HeaderTextBlock":
			# Not only header should be announced, dialog text should also be announced as well.
			# This works properly if the parent object is recognized as a dialog.
			ui.message(obj.parent.description)
		nextHandler()
