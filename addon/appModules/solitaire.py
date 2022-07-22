# Microsoft Solitaire Collection
# Part of Windows App Essentials collection
# Copyright 2020-2022 Joseph Lee, released under GPL

# Support for Microsoft Solitaire Collection.
# DEPRECATED: version 4.13 and later improves accessibility significantly by adding labels for cards.

import appModuleHandler
import controlTypes


class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# Cards are seen as "unknown" by NVDA, but thankfully localized control type serves as the label.
		# In 4.13 and later, card suits and ranks are labeled but not the stacks.
		if obj.role == controlTypes.Role.UNKNOWN and not obj.name:
			obj.name = obj.UIAElement.currentLocalizedControlType
