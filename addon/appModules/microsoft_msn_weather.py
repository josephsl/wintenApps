# WinTenApps/microsoft_msn_weather.py
# Part of Windows 10 App Essentials collection
# Copyright 2016 Derek Riemer, released under GPL.

# Provides workarounds for the weather app.


import appModuleHandler
import controlTypes
import re

#Regexp for deciding whether this ID should be a tab control
RE_TAB_AUTOMATION_MATCH = re.compile(r"L1NavigationButton_\d+")

class AppModule(appModuleHandler.AppModule):
	def event_NVDAObject_init(self, obj):
		if obj.UIAElement.CachedAutomationId == u"SideNavigationBar" and not obj.role in (controlTypes.ROLE_GROUPING, ):
			obj.role = controlTypes.ROLE_TABCONTROL
		theId = obj.UIAElement.CachedAutomationId
		if RE_TAB_AUTOMATION_MATCH.match(theId):
			obj.role = controlTypes.ROLE_TAB