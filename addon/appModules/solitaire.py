# Microsoft Solitaire Collection
# Part of Windows App Essentials collection
# Copyright 2020-2021 Joseph Lee, released under GPL

# Support for Microsoft Solitaire Collection.

import appModuleHandler
import UIAHandler
import controlTypes


# Support control types refactor (both before and after for a time).
if hasattr(controlTypes, "Role"):
	ROLE_UNKNOWN = controlTypes.Role.UNKNOWN
else:
	ROLE_UNKNOWN = controlTypes.ROLE_UNKNOWN


class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# Cards are seen as "unknown" by NVDA, but thankfully localized control type serves as the label.
		if obj.role == ROLE_UNKNOWN:
			obj.name = obj._getUIACacheablePropertyValue(UIAHandler.UIA_LocalizedControlTypePropertyId)
