# Voice Access
# Part of Windows App Essentials collection
# Copyright 2022 Joseph Lee, released under GPL

# Support for Windows 11 Voice Access (Version 22H2).

import appModuleHandler
from NVDAObjects.UIA import UIA
from NVDAObjects.behaviors import Dialog


class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			if obj.UIAElement.cachedClassName == "Popup":
				clsList.insert(0, Dialog)
