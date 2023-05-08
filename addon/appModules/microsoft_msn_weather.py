# MSN Weather
# Part of Windows App Essentials collection
# Copyright 2016-2023 Derek Riemer, Joseph Lee, released under GPL.

# Provides workarounds for the weather app.

import re
from typing import List
import controlTypes
import appModuleHandler
import ui
from NVDAObjects import NVDAObject
import scriptHandler

# Regexp for deciding whether this ID should be a tab control
RE_TAB_AUTOMATION_MATCH = re.compile("|".join([
	r"L1NavigationButton_(Places|Home|Maps|Historical|Pollen|Life|HourlyForecast|MonthlyForecast|Feedback)",
]))
# Regexp for deciding if this should be a button
RE_BUTTONCONTROL = re.compile("|".join([
	r"L1NavigationButton_Settings",
]))


# Deprecated: Weather 4.53.51095 and later shows forecast info in a web document control.
class WeatherForecastItem(NVDAObject):

	def initOverlayClass(self) -> None:
		self.curLine = -1  # Start out reading the first thing.
		self.lines = self.name.split("\r\n")

	@scriptHandler.script(gesture="kb:downArrow")
	def script_nextLine(self, gesture) -> None:
		if self.curLine < len(self.lines) - 1:
			self.curLine += 1
		ui.message(self.lines[self.curLine])

	@scriptHandler.script(gesture="kb:upArrow")
	def script_previousLine(self, gesture) -> None:
		if self.curLine == -1:
			self.curLine = 0
		if self.curLine > 0:
			self.curLine -= 1
		ui.message(self.lines[self.curLine])


class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj: NVDAObject):
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
