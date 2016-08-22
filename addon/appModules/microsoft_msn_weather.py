# WinTenApps/microsoft_msn_weather.py
# Part of Windows 10 App Essentials collection
# Copyright 2016 Derek Riemer, released under GPL.

# Provides workarounds for the weather app.


import re
import controlTypes
import appModuleHandler
from NVDAObjects import NVDAObject

#Regexp for deciding whether this ID should be a tab control
RE_TAB_AUTOMATION_MATCH = re.compile(r"L1NavigationButton_\d+")
#Regexp for deciding if this should be a button
RE_BUTTONCONTROL = re.compile("|".join([
	r"L1NavigationButton_Settings",
]))

class AppModule(appModuleHandler.AppModule):
	def event_NVDAObject_init(self, obj):
		try:
			
		if obj.UIAElement.CachedAutomationId == u"SideNavigationBar" and not obj.role in (controlTypes.ROLE_GROUPING, ):
			obj.role = controlTypes.ROLE_TABCONTROL
		theId = obj.UIAElement.CachedAutomationId
		if RE_TAB_AUTOMATION_MATCH.match(theId):
			obj.role = controlTypes.ROLE_TAB
		elif RE_BUTTONCONTROL.match(theId):
			obj.role = controlTypes.ROLE_BUTTON