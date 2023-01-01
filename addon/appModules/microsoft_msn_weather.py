# MSN Weather
# Part of Windows App Essentials collection
# Copyright 2016-2023 Derek Riemer, released under GPL.

# Provides workarounds for the weather app.

import re
import controlTypes
import appModuleHandler
import ui
import wx
from NVDAObjects import NVDAObject
import scriptHandler
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
# This is because the Automation Id for them is non-existent, so we check their parent.
RE_PARENT_LISTS = re.compile("|".join([
	r"DailyList",
	r"HourlyList",
]))


class WeatherForecastItem(NVDAObject):

	def initOverlayClass(self):
		self.curLine = -1  # Start out reading the first thing.
		self.lines = self.name.split("\r\n")

	@scriptHandler.script(gesture="kb:downArrow")
	def script_nextLine(self, gesture):
		if self.curLine < len(self.lines) - 1:
			self.curLine += 1
			ui.message(self.lines[self.curLine])
		else:
			# Translators: Message presented when no more weather data is available for the current item.
			ui.message(_("No more weather data for this item."))
			wx.Bell()

	@scriptHandler.script(gesture="kb:upArrow")
	def script_previousLine(self, gesture):
		if self.curLine > 0:
			self.curLine -= 1
			ui.message(self.lines[self.curLine])
		else:
			# Translators: Message presented when no more weather data is available for the current item.
			ui.message(_("No more weather data for this item."))
			wx.Bell()


class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if (
			obj.role == controlTypes.Role.LISTITEM
			and RE_PARENT_LISTS.match(obj.parent.UIAAutomationId)
		):
			clsList.insert(0, WeatherForecastItem)

	def event_NVDAObject_init(self, obj):
		try:
			theId = obj.UIAAutomationId
		except AttributeError:
			return
		if theId == "SideNavigationBar" and obj.role != controlTypes.Role.GROUPING:
			obj.role = controlTypes.Role.TABCONTROL
		if RE_TAB_AUTOMATION_MATCH.match(theId):
			obj.role = controlTypes.Role.TAB
		elif RE_BUTTONCONTROL.match(theId):
			obj.role = controlTypes.Role.BUTTON
