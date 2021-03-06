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

	def announceDownloadProgress(self, obj: Any) -> None:
		if isinstance(obj, UIA) and obj.UIAAutomationId == "InstallControl":
			# Install control comes with an anoying name, so look at its children.
			# Sometimes one of its children disappears, causing attribute error to be thrown.
			try:
				progressText = " ".join([obj.firstChild.name, obj.simpleFirstChild.name])
			except AttributeError:
				progressText = ""
			if progressText != self._appInstallProgress:
				self._appInstallProgress = progressText
				ui.message(progressText)

	def event_nameChange(self, obj, nextHandler):
		# Do not proceed if we're not even focused on Microsoft Store.
		if any([obj.appModule.appName == self.appName for obj in api.getFocusAncestors()]):
			# In version 12007, it is value change event that will present content download progress.
			self.announceDownloadProgress(obj)
		nextHandler()

	def event_valueChange(self, obj, nextHandler):
		# Version 12007 and later fires value change event instead, but the procedure is same as name change event.
		if any([obj.appModule.appName == self.appName for obj in api.getFocusAncestors()]):
			self.announceDownloadProgress(obj)
		nextHandler()
