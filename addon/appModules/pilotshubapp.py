# WinTenApps/pilotshubapp.py
# Part of Windows 10 App Essentials collection
# Copyright 2018 Joseph Lee, released under GPL.

# A collection of workarounds for Feedback Hub app.

import appModuleHandler
from NVDAObjects.UIA import UIA

class AppModule(appModuleHandler.AppModule):

	def event_UIA_notification(self, obj, nextHandler, activityId=None, **kwargs):
		if activityId in ("CategoryChangedContext",): return
		nextHandler(activityId=activityId, **kwargs)
