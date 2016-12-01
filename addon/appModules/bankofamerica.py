# WinTenApps/BankOfAmerica.py
# Part of Windows 10 App Essentials collection
# Copyright 2016 Joseph Lee, released under GPL.

# Provides workarounds for BofA app.

import appModuleHandler
import controlTypes
from NVDAObjects.UIA import UIA

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# A variation of Twitter button issue: this time, last child is the one we're interested in.
		if isinstance(obj, UIA) and obj.role == controlTypes.ROLE_BUTTON and obj.name == "":
			try:
				obj.name = obj.lastChild.name
			except AttributeError:
				pass
