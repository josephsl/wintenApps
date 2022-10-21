# WinTenApps/peopleapp.py
# Part of Windows App Essentials collection
# Copyright 2018-2022 Joseph Lee, released under GPL.

# Various workarounds for People app (modern version of Outlook Contacts).

import appModuleHandler
from NVDAObjects.UIA import UIA, SuggestionListItem, SearchField


class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			# Apart from different Automation Id's,
			# contacts search field and suggestions are search field and suggestions, respectively.
			# Resolved in a more generic way in NVDA 2023.1, app module is deprecated.
			if obj.UIAAutomationId == "SuggestedListItem":
				clsList.insert(0, SuggestionListItem)
			elif obj.UIAAutomationId == "ContactSearchTextBox":
				clsList.insert(0, SearchField)
