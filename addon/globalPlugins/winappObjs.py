# Windows app controls repository
# Copyright 2015-2025 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.
# No longer included in the add-on package but kept in the add-on code repository.

import globalPluginHandler
import UIAHandler


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super().__init__()
		# NVDA Core issue 17771 (hack): add WinUI3 top-level class name to good UIA window class names tuple.
		goodUIAWindowClassNames = set(UIAHandler.goodUIAWindowClassNames)
		goodUIAWindowClassNames.add("Microsoft.UI.Content.DesktopChildSiteBridge")
		UIAHandler.goodUIAWindowClassNames = tuple(goodUIAWindowClassNames)
