# Microsoft Solitaire Collection
# Part of Windows App Essentials collection
# Copyright 2020-2021 Joseph Lee, released under GPL

# Support for Microsoft Solitaire Collection.

import appModuleHandler
import controlTypes


class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# Cards are seen as "unknown" by NVDA, but thankfully localized control type serves as the label.
		if obj.role == controlTypes.Role.UNKNOWN:
			obj.name = obj.UIAElement.currentLocalizedControlType
