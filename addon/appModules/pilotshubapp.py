# WinTenApps/pilotshubapp.py
# Part of Windows 10 Apps Essentials collection
# Copyright 2015 Joseph Lee, released under GPL.

# Workarounds for radio button label issues.

import appModuleHandler
from NVDAObjects.UIA import UIA
import controlTypes

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# Until Microsoft labels the radio buttons properly...
		if obj.role == controlTypes.ROLE_RADIOBUTTON and obj.name == "":
			obj.name = obj.lastChild.name
