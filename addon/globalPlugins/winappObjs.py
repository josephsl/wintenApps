# Windows app controls repository
# Copyright 2015-2024 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.

import globalPluginHandler
import appModuleHandler


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super().__init__()
		# Register Windows 11 24H2 version of quick settings interface.
		appModuleHandler.registerExecutableWithAppModule("shellhost", "shellexperiencehost")
