# Microsoft Store
# Part of Windows App Essentials collection
# Copyright 2016-2021 Joseph Lee, released under GPL

# Enhancements to support Microsoft Store (formerly Windows Store).

import appModuleHandler
import api
import ui
from NVDAObjects.UIA import UIA


class AppModule(appModuleHandler.AppModule):

	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		# The rest of the app module applies to Store version 1 (old Store in Windows 10)
		# with the bulk of it being value change event handler.
		# See older add-on releases for details.
		if self.productVersion.startswith("2"):
			self.event_valueChange = None

	# just like Settings app, have a cache of download progress text handy.
	_appInstallProgress: str = ""

	def event_valueChange(self, obj, nextHandler):
		# Version 12007 and later fires value change event instead, but the procedure is same as name change event.
		# Do not proceed if we're not even focused on Microsoft Store.
		# Store version 2 uses name change event with the update progress text being part of the label.
		if any([obj.appModule.appName == self.appName for obj in api.getFocusAncestors()]):
			# Optimization: only handle value changes if progress text is shown on screen.
			# This may result in missing some announcements.
			if isinstance(obj, UIA) and obj.UIAAutomationId == "InstallControl" and any(obj.location):
				# Install control comes with an anoying name, so look at its children.
				# Separate title and progress message for readability and to react to UI changes.
				downloadTitle = obj.firstChild.name
				# Optimization: obtain first child according to UIA instead of using simple first child.
				# This speeds up element lookup significantly.
				downloadProgress = obj.children[0].name
				progressText = " ".join([downloadTitle, downloadProgress])
				if progressText != self._appInstallProgress:
					self._appInstallProgress = progressText
					ui.message(progressText)
		nextHandler()

	def event_appModule_loseFocus(self):
		self._appInstallProgress = ""
