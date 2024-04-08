# Windows app controls repository
# Copyright 2015-2024 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.

import globalPluginHandler
import appModuleHandler
import versionInfo


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super().__init__()
		# Register Windows 11 24H2 version of quick settings interface.
		# Resolved in NVDA 2024.2 (do not add another app alias if NVDA 2024.2 is in use).
		if (versionInfo.version_year, versionInfo.version_major) < (2024, 2):
			appModuleHandler.registerExecutableWithAppModule("shellhost", "shellexperiencehost")
