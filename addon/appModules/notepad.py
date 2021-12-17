# Windows 11 Notepad
# Part of Windows App Essentials collection
# Copyright 2021 Joseph Lee, released under GPL

# Support for Windows 11 Notepad.

import appModuleHandler
import api
from NVDAObjects.UIA import UIA


class NotepadDocument(UIA):

	# Do not announce the entered text when Enter key is pressed, similar to Start menu search field.
	announceNewLineText = False


class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Specifically to suppress text announcement when Enter key is pressed.
		if isinstance(obj, UIA) and obj.windowClassName == "RichEditD2DPT":
			clsList.insert(0, NotepadDocument)

	def _get_statusBar(self):
		# Notepad 11 uses Windows 11 user interface, therefore status bar is harder to obtain.
		# This does not affect earlier versions.
		if not self.productVersion.startswith("11"):
			raise NotImplementedError()
		fg = api.getForegroundObject()
		# Look for a specific child as some children report the same UIA properties such as class name.
		statusBar = fg.children[4].firstChild
		return statusBar
