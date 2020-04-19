# WinTenApps/microsoft_msn_weather.py
# Part of Windows 10 App Essentials collection
# Copyright 2016-2020 Derek Riemer, released under GPL.

# Provides workarounds for the weather app.

import re
import controlTypes
import appModuleHandler
import ui
import wx
from NVDAObjects import NVDAObject
import addonHandler
addonHandler.initTranslation()

# Regexp for deciding whether this ID should be a tab control
RE_TAB_AUTOMATION_MATCH = re.compile("|".join([
	r"L1NavigationButton_(Places|Home|Maps|Historical|News)",
	r"L1NavigationButton_Feedback",
]))
# Regexp for deciding if this should be a button
RE_BUTTONCONTROL = re.compile("|".join([
	r"L1NavigationButton_Settings",
]))
# Regexp for multiLine List items, whos children need the list class added.
# This is because the AutomationID for them is non existant, so we check their parent.
RE_PARENT_LISTS = re.compile("|".join([
	r"DailyList",
	r"HourlyList",
]))

class WeatherForecastItem(NVDAObject):

	def initOverlayClass(self):
		self.curLine = -1 #Start out reading the first thing.
		self.lines = self.name.split("\r\n")

	def script_nextLine(self, gesture):
		if self.curLine < len(self.lines)-1:
			self.curLine += 1
			ui.message(self.lines[self.curLine])
		else:
			# Translators: Message presented when no more weather data is available for the current item.
			ui.message(_("No more weather data for this item."))
			wx.Bell()

	def script_previousLine(self, gesture):
		if self.curLine > 0:
			self.curLine -= 1
			ui.message(self.lines[self.curLine])
		else:
			# Translators: Message presented when no more weather data is available for the current item.
			ui.message(_("No more weather data for this item."))
			wx.Bell()

	__gestures = {
		"kb:downArrow": "nextLine",
		"kb:upArrow": "previousLine",
	}

class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.role == controlTypes.ROLE_LISTITEM and RE_PARENT_LISTS.match(obj.parent.UIAElement.CachedAutomationID):
			clsList.insert(0, WeatherForecastItem)

	def event_NVDAObject_init(self, obj):
		try:
			theId = obj.UIAElement.CachedAutomationId
		except AttributeError:
			return
		if obj.UIAElement.CachedAutomationId == "SideNavigationBar" and not obj.role in (controlTypes.ROLE_GROUPING, ):
			obj.role = controlTypes.ROLE_TABCONTROL
		if RE_TAB_AUTOMATION_MATCH.match(theId):
			obj.role = controlTypes.ROLE_TAB
		elif RE_BUTTONCONTROL.match(theId):
			obj.role = controlTypes.ROLE_BUTTON
