# WinTenApps/teamviewertouch.py
# Part of Windows 10 Apps Essentials collection
# Copyright 2015 Joseph Lee, released under GPL.

# TeamViewer Touch allows tablets to connect to remote computers.
# Exhibits same radio button issues as in Insider Hub.
# Additionally has issues with button markup.

import appModuleHandler
from NVDAObjects.UIA import UIA
import controlTypes

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# Teamviewer, please fix the markup of radio buttons and buttons...
		if obj.role in (controlTypes.ROLE_RADIOBUTTON, controlTypes.ROLE_BUTTON) and obj.name == "":
			obj.name = obj.lastChild.name
