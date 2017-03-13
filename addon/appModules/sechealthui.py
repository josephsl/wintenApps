# WinTenApps/SecHealthUI.py
# Part of Windows 10 App Essentials collection
# Copyright 2016-2017 Joseph Lee, released under GPL.

# Workarounds for Windows Defender UWP (build 14986 and later).

import appModuleHandler
import controlTypes
from NVDAObjects.UIA import UIA
import winVersion

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# Until Microsoft fixes this...
		# Oddly enough, in build 15007 and later, button label is not the last child, but the one before that.
		# Fixed in build 15055, kept for now because slow ring Insiders are using 15048.
		if winVersion.winVersion.build < 15055 and isinstance(obj, UIA) and obj.role == controlTypes.ROLE_BUTTON and obj.name == "":
			try:
				obj.name = obj.getChild(-2).name
			except AttributeError:
				pass
