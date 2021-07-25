# Microsoft Solitaire Collection
# Part of Windows App Essentials collection
# Copyright 2020-2021 Joseph Lee, released under GPL

# Support for Microsoft Solitaire Collection.

import appModuleHandler
import UIAHandler
import controlTypes


# Support control types refactor (both before (2021.1) and after (2021.2) for a time).
# Note that pre-refactor attributes will be gone in NVDA 2022.1.


class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# Cards are seen as "unknown" by NVDA, but thankfully localized control type serves as the label.
		if obj.role == controlTypes.ROLE_UNKNOWN:
			obj.name = obj._getUIACacheablePropertyValue(UIAHandler.UIA_LocalizedControlTypePropertyId)
