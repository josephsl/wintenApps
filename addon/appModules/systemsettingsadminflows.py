# Windows Settings/Reset This PC
# Part of Windows App Essentials collection
# Copyright 2018-2021 Joseph Lee, released under GPL

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

	def event_UIA_window_windowOpen(self, obj, nextHandler):
		# With selective UIA event registration on, name change event from the header text will not be handled.
		import UIAHandler
		# First child is a title bar, but simple first child is the actual header text.
		# Therefore try using simple first child unless the situation changes in the future.
		# Wrap this inside a try/except block
		# as NotImplementedError is raised if selective event registration is off.
		try:
			UIAHandler.handler.removeEventHandlerGroup(
				obj.simpleFirstChild.UIAElement, UIAHandler.handler.localEventHandlerGroup
			)
			UIAHandler.handler.addEventHandlerGroup(
				obj.simpleFirstChild.UIAElement, UIAHandler.handler.localEventHandlerGroup
			)
		except NotImplementedError:
			pass
		nextHandler()
