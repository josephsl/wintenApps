# Microsoft Store
# Part of Windows 10 App Essentials collection
# Copyright 2016-2021 Joseph Lee, released under GPL

# Enhancements to support Microsoft Store (formerly Windows Store).

# Help Mypy and other static checkers for a time by importing uppercase versions of built-in types.
from typing import Any
import appModuleHandler
import api
import ui
import controlTypes
from NVDAObjects.UIA import UIA


class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# Extraneous information announced when going through apps to be updated/installed,
		# so use a grandchild's name.
		if (
			isinstance(obj, UIA) and obj.role == controlTypes.ROLE_LISTITEM
			and obj.firstChild and obj.firstChild.UIAAutomationId == "InstallControl"
		):
			obj.name = obj.firstChild.firstChild.name

	# just like Settings app, have a cache of download progress text handy.
	_appInstallProgress: str = ""

	def event_valueChange(self, obj, nextHandler):
		# Version 12007 and later fires value change event instead, but the procedure is same as name change event.
		# Do not proceed if we're not even focused on Microsoft Store.
		if any([obj.appModule.appName == self.appName for obj in api.getFocusAncestors()]):
			if isinstance(obj, UIA) and obj.UIAAutomationId == "InstallControl":
				# Install control comes with an anoying name, so look at its children.
				# Sometimes one of its children disappears, causing attribute error to be thrown.
				try:
					# Separate title and progress message for readability and to react to UI changes.
					downloadTitle = obj.firstChild.name
					# Optimization: obtain first child according to UIA instead of using simple first child.
					# This speeds up element lookup significantly.
					downloadProgress = obj.children[0].name
					progressText = " ".join([downloadTitle, downloadProgress])
				except AttributeError:
					progressText = ""
				if progressText != self._appInstallProgress:
					self._appInstallProgress = progressText
					ui.message(progressText)
		nextHandler()
