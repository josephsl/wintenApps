# WinTenApps/music_ui.py
# Part of Windows 10 App Essentials collection
# Copyright 2016 Joseph Lee, released under GPL.

# Various workarounds for Groove music.

import appModuleHandler
from NVDAObjects.UIA import UIA
from globalPlugins.wintenObjs import SearchField
import config

class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA) and obj.UIAElement.cachedClassName in ("TextBox", "RichEditBox") and obj.UIAElement.cachedAutomationID == "SearchTextBox":
			# But this app module is no longer needed from nVDA 2017.3 or later.
			if "reportAutoSuggestionsWithSound" not in config.conf["presentation"]:
				clsList.insert(0, SearchField)
