# Windows 11 Settings/Restart to install updates
# Part of Windows App Essentials collection
# Copyright 2018-2021 Joseph Lee, released under GPL

# Specific to Restart to install updates window in Windows 11 Settings.

import appModuleHandler
from NVDAObjects.UIA import UIA
from NVDAObjects.behaviors import Dialog


class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			# Install updates window is actually a dialog.
			if obj.UIAElement.cachedClassName == "Shell_SystemDialog":
				clsList.insert(0, Dialog)
