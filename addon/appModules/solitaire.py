# Microsoft Solitaire Collection
# Part of Windows 10 App Essentials collection
# Copyright 2020 Joseph Lee, released under GPL

# Support for Microsoft Solitaire Collection.

import appModuleHandler
import UIAHandler
import controlTypes

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# Cards are seen as "unknown" by NVDA, but thankfully localized control type serves as the label.
		if obj.role == controlTypes.ROLE_UNKNOWN:
			obj.name = obj._getUIACacheablePropertyValue(UIAHandler.UIA_LocalizedControlTypePropertyId)
