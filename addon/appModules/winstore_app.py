# Windows 10 Store
# Part of Windows 10 App Essentials collection
# Copyright 2016 Joseph Lee, released under GPL

# Enhancements to support Windows Store.

import appModuleHandler
import ui
import controlTypes
from NVDAObjects.UIA import UIA
from NVDAObjects.behaviors import ProgressBar

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# Extraneous information announced when going through apps to be updated/installed, so use a grandchild's name.
		if isinstance(obj, UIA) and obj.role == controlTypes.ROLE_LISTITEM and obj.firstChild and obj.firstChild.UIAElement.cachedAutomationID == "InstallControl":
			obj.name = obj.firstChild.firstChild.name

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			if obj.UIAElement.cachedAutomationID == "SearchTextBox":
				import globalPlugins.wintenObjs
				clsList.insert(0, globalPlugins.wintenObjs.SearchField)

	def event_valueChange(self, obj, nextHandler):
		if isinstance(obj, UIA):
			# Detect change in app installation progress bar.
			if obj.UIAElement.cachedAutomationID == "_progressBar":
				obj.event_valueChange()
		nextHandler()

	# just like Settings app, have a cache of download progress text handy.
	_appInstallProgress = ""

	def event_nameChange(self, obj, nextHandler):
		if isinstance(obj, UIA) and obj.UIAElement.cachedAutomationID == "_progressText":
			if obj.name != self._appInstallProgress:
				self._appInstallProgress = obj.name
				# Don't forget to announce product title.
				productTitle = obj.parent.previous
				if productTitle.UIAElement.cachedAutomationID == "_productTitle":
					ui.message(" ".join([productTitle.name, obj.name]))
		nextHandler()
