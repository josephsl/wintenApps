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

	def event_NVDAObject_init(self, obj):
		# NVDA Core issue 6948: treat the below grouping control as a pane, results in "WebRuntime Content View" announcement suppression.
		# Remove this once NVDA Core comes up with a fix."
		if isinstance(obj, UIA) and obj.role == controlTypes.ROLE_GROUPING and obj.UIAElement.cachedAutomationID == "AccessibilityView":
			obj.role = controlTypes.ROLE_PANE

	def event_nameChange(self, obj, nextHandler):
		if isinstance(obj, UIA):
			if obj.role == controlTypes.ROLE_STATICTEXT and obj.parent.UIAElement.cachedClassName == "NotificationBar":
				ui.message(obj.name)
		nextHandler()
