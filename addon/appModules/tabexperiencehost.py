# WinTenApps/tabexperiencehost.py
# Part of Windows 10 App Essentials collection
# Copyright 2018-2019 Joseph Lee, released under GPL.

# Supports app tabs/Sets in Redstone 5.

import appModuleHandler
import ui
import braille

class AppModule(appModuleHandler.AppModule):

	def event_UIA_elementSelected(self, obj, nextHandler):
		# Announce Sets tab position.
		obj.reportFocus()
		braille.handler.message(braille.getBrailleTextForProperties(name=obj.name, role=obj.role, positionInfo=obj.positionInfo))
		nextHandler()

	def event_UIA_notification(self, obj, nextHandler, displayString=None, **kwargs):
		ui.message(displayString)
		nextHandler()
