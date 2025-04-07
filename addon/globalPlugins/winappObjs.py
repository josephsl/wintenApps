# Windows app controls repository
# Copyright 2015-2025 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 11.

import globalPluginHandler
import globalVars
import UIAHandler
from logHandler import log


# Don't even think about proceeding in secure screens.
def disableInSecureMode(cls):
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super().__init__()
		# NVDA Core issues 17407 and 17771 (hack):
		# add WinUI3 top-level class name to good UIA window classes tuple to enable mouse/touch navigation.
		# Resolved in NVDA 2025.2.
		if "Microsoft.UI.Content.DesktopChildSiteBridge" not in UIAHandler.goodUIAWindowClassNames:
			log.debug(
				"winapps: adding Microsoft.UI.Content.DesktopChildSiteBridge to good UIA window class names"
			)
			goodUIAWindowClassNames = set(UIAHandler.goodUIAWindowClassNames)
			goodUIAWindowClassNames.add("Microsoft.UI.Content.DesktopChildSiteBridge")
			UIAHandler.goodUIAWindowClassNames = tuple(goodUIAWindowClassNames)
