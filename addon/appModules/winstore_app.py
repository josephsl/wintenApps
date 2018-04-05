# Microsoft Store
# Part of Windows 10 App Essentials collection
# Copyright 2016-2018 Joseph Lee, released under GPL

# Enhancements to support Microsoft Store (formerly Windows Store).

import appModuleHandler
import ui
import controlTypes
from NVDAObjects.UIA import UIA

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# Extraneous information announced when going through apps to be updated/installed, so use a grandchild's name.
		if isinstance(obj, UIA) and obj.role == controlTypes.ROLE_LISTITEM and obj.firstChild and obj.firstChild.UIAElement.cachedAutomationID == "InstallControl":
			obj.name = obj.firstChild.firstChild.name

	# just like Settings app, have a cache of download progress text handy.
	_appInstallProgress = ""

	def event_nameChange(self, obj, nextHandler):
		# It turns out name change event will suffice from January 2018 release onwards.
		if self.productVersion >= "11801":
			if isinstance(obj, UIA) and obj.UIAElement.cachedAutomationID == "InstallControl":
				# Install control comes with an anoying name, so look at its children.
				progressText = " ".join([obj.firstChild.name, obj.simpleFirstChild.name])
				if progressText != self._appInstallProgress:
					self._appInstallProgress = progressText
					ui.message(progressText)
		nextHandler()
