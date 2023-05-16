# MSN Weather
# Part of Windows App Essentials collection
# Copyright 2016-2023 Derek Riemer, Joseph Lee, released under GPL.

# Provides workarounds for the weather app.

import re
import controlTypes
import appModuleHandler
from NVDAObjects import NVDAObject

# Deprecated: regexp for deciding whether this ID should be a tab control
RE_TAB_AUTOMATION_MATCH = re.compile("|".join([
	r"L1NavigationButton_(Places|Home|Maps|Historical|Pollen|Life|HourlyForecast|MonthlyForecast|Feedback)",
]))


class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj: NVDAObject):
		# Deprecated: role reclassifications no longer make sense as UIA class name is radio button.
		try:
			theId = obj.UIAAutomationId
		except AttributeError:
			return
		if theId == "SideNavigationBar" and obj.role != controlTypes.Role.GROUPING:
			obj.role = controlTypes.Role.TABCONTROL
		if RE_TAB_AUTOMATION_MATCH.match(theId):
			obj.role = controlTypes.Role.TAB
		elif theId == "L1NavigationButton_Settings":
			obj.role = controlTypes.Role.BUTTON
