# MSN Weather
# Part of Windows App Essentials collection
# Copyright 2016-2023 Derek Riemer, Joseph Lee, released under GPL.

# Provides workarounds for the weather app.

import re
import controlTypes
import appModuleHandler
from NVDAObjects import NVDAObject


class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj: NVDAObject):
		# Deprecated: role reclassifications no longer make sense as UIA class name is radio button.
		try:
			theId = obj.UIAAutomationId
		except AttributeError:
			return
