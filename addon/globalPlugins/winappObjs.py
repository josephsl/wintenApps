# Windows app controls repository
# Copyright 2015-2025 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 11.

import globalPluginHandler
import globalVars


# Don't even think about proceeding in secure screens.
# Don't worry about "cls" type.
def disableInSecureMode(cls):  # type: ignore
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super().__init__()
