# Windows 10 Store
# Part of Windows 10 App Essentials collection
# Copyright 2016 Joseph Lee, released under GPL

# Enhancements to support Windows Store.

import appModuleHandler
import ui
import controlTypes
from NVDAObjects.UIA import UIA

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# Extraneous information announced when going through apps to be updated/installed, so use a grandchild's name.
		if isinstance(obj, UIA) and obj.role == controlTypes.ROLE_LISTITEM and obj.firstChild and obj.firstChild.UIAElement.cachedAutomationID == "InstallControl":
			obj.name = obj.firstChild.firstChild.name
