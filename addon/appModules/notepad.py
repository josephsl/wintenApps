# Windows 11 Notepad
# Part of Windows App Essentials collection
# Copyright 2021-2022 Joseph Lee, released under GPL

# Support for Windows 11 Notepad.

import appModuleHandler
import api


class AppModule(appModuleHandler.AppModule):

	def _get_statusBar(self):
		# NVDA Core issue 13688: Notepad 11 uses Windows 11 user interface,
		# therefore status bar is harder to obtain.
		# This does not affect earlier versions.
		notepadVersion = int(self.productVersion.split(".")[0])
		if notepadVersion < 11:
			raise NotImplementedError()
		# And no, status bar is shown when editing documents.
		# Thankfully, of all the UIA objects encountered, document window has a unique window class name.
		if api.getFocusObject().windowClassName != "RichEditD2DPT":
			raise NotImplementedError()
		# Look for a specific child as some children report the same UIA properties such as class name.
		# Status bar location in the UI tree has changed in 11.2112,
		# made available to stable build users in February 2022.
		statusBar = api.getForegroundObject().children[7].firstChild
		# No location for a disabled status bar i.e. location is 0 (x, y, width, height).
		if not any(statusBar.location):
			raise NotImplementedError()
		return statusBar
