# Windows app controls repository
# Copyright 2015-2025 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.

import globalPluginHandler
import globalVars
import UIAHandler


# Don't even think about proceeding in secure screens.
def disableInSecureMode(cls):
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super().__init__()
		# NVDA Core issue 17771 (hack): add WinUI3 top-level class name to good UIA window class names tuple.
		goodUIAWindowClassNames = set(UIAHandler.goodUIAWindowClassNames)
		goodUIAWindowClassNames.add("Microsoft.UI.Content.DesktopChildSiteBridge")
		UIAHandler.goodUIAWindowClassNames = tuple(goodUIAWindowClassNames)
