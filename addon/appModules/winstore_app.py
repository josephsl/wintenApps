# Windows 10 Store
# Part of Windows 10 App Essentials collection
# Copyright 2016-2017 Joseph Lee, released under GPL

# Enhancements to support Windows Store.

import appModuleHandler
import ui
import controlTypes
import NVDAObjects.UIA
from NVDAObjects.behaviors import ProgressBar

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# Extraneous information announced when going through apps to be updated/installed, so use a grandchild's name.
		if isinstance(obj, NVDAObjects.UIA.UIA) and obj.role == controlTypes.ROLE_LISTITEM and obj.firstChild and obj.firstChild.UIAElement.cachedAutomationID == "InstallControl":
			obj.name = obj.firstChild.firstChild.name

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# This whole thing (function) will be gone in NVDA 2017.3.
		if not hasattr(NVDAObjects.UIA, "SearchField") and isinstance(obj, NVDAObjects.UIA.UIA):
			if obj.UIAElement.cachedAutomationID == "SearchTextBox":
				import globalPlugins.wintenObjs
				clsList.insert(0, globalPlugins.wintenObjs.SearchField)

	def event_valueChange(self, obj, nextHandler):
		if isinstance(obj, NVDAObjects.UIA.UIA):
			# Detect change in app installation progress bar.
			if obj.UIAElement.cachedAutomationID == "_progressBar":
				obj.event_valueChange()
		nextHandler()

	# just like Settings app, have a cache of download progress text handy.
	_appInstallProgress = ""

	def event_liveRegionChange(self, obj, nextHandler):
		if isinstance(obj, NVDAObjects.UIA.UIA) and obj.UIAElement.cachedAutomationID == "_progressText":
			if obj.name != self._appInstallProgress:
				self._appInstallProgress = obj.name
				# Don't forget to announce product title.
				productTitle = obj.parent.previous
				# Since March 2017 update, it is no longer the product name, but a progress button.
				if productTitle and productTitle.role == controlTypes.ROLE_BUTTON:
					# But since September 2017 update, the title is next door.
					possibleProductTitle = productTitle.parent.previous
					productTitle = productTitle.previous if possibleProductTitle is None else productTitle.parent.previous
				if productTitle and isinstance(productTitle, NVDAObjects.UIA.UIA) and productTitle.UIAElement.cachedAutomationID == "_productTitle":
					ui.message(" ".join([productTitle.name, obj.name]))
			return
		nextHandler()
