# MicrosoftEdge.py
# Part of Windows 10 App Essentials collection
# Copyright 2016 Joseph Lee, released under GPL

# Core Edge support provided by NvDA Core (NVDAObjects/UIA package)
# Provides additional enhancements.

import appModuleHandler
from NVDAObjects.UIA import UIA
import controlTypes
import ui


class AppModule(appModuleHandler.AppModule):

	def event_nameChange(self, obj, nextHandler):
		if isinstance(obj, UIA):
			if obj.role == controlTypes.ROLE_STATICTEXT and obj.parent.UIAElement.cachedClassName == "NotificationBar":
				ui.message(obj.name)
		nextHandler()
