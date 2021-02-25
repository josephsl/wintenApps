# WinTenApps/peopleapp.py
# Part of Windows 10 App Essentials collection
# Copyright 2018-2021 Joseph Lee, released under GPL.

# Various workarounds for People app (modern version of Outlook Contacts).

import appModuleHandler
from NVDAObjects.UIA import UIA, SuggestionListItem


class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			# Apart from a different Automation Id, contacts search suggestions are suggestions.
			if obj.UIAAutomationId == "SuggestedListItem":
				clsList.insert(0, SuggestionListItem)
