# WinTenApps/hxcalendarappimm.py
# Part of Windows 10 App Essentials collection
# Copyright 2016-2020 Joseph Lee, released under GPL.

# Fixes for certain issues with Windows 10 Calendar app (based on Outlook 2016).

import appModuleHandler

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# It is quite anoying to hear the same text for name and description, so forget the description.
		if obj.name != "" and obj.description == obj.name:
			obj.description = None
