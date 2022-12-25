# Windows app controls repository
# Copyright 2015-2023 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.

import globalPluginHandler
from NVDAObjects.UIA import UIA, Dialog
import globalVars
import UIAHandler
from logHandler import log


# #20: don't even think about proceeding in secure screens.
def disableInSecureMode(cls):
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super().__init__()
		# Is this a Windows 11 22H2 beta build (2262x)?
		import winVersion
		if winVersion.getWinVer().build in (22622, 22623):
			log.info("winapps: Windows 11 22H2 beta detected")
		# Report processor architecture if running NVDA 2022.4 and earlier.
		if not hasattr(winVersion.getWinVer(), "processorArchitecture"):
			import platform
			log.info(f"winapps: processor architecture: {platform.machine()}")
		# #82: Windows 11 22H2 Moment 2 introduces a redesigned taskbar and systray powered by Win32.
		# However touch and mouse interaction does not work when systray overflow window is open.
		# Therefore reclassify the new systray overflow window class name as a good UIA window class.
		# A better solution is patching File Explorer app module but the below workaround will suffice.
		goodUIAWindowClassNames = list(UIAHandler.goodUIAWindowClassNames)
		goodUIAWindowClassNames.append("TopLevelWindowForOverflowXamlIsland")
		UIAHandler.goodUIAWindowClassNames = tuple(goodUIAWindowClassNames)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if not isinstance(obj, UIA):
			return
		# Windows that are really dialogs.
		# Some dialogs, although listed as a dialog thanks to UIA class name,
		# does not advertise the proper role of dialog.
		# This is still the case with some dialogs such as restart to install updates dialog in Windows 11.
		if obj.UIAElement.cachedClassName in UIAHandler.UIADialogClassNames and Dialog not in clsList:
			clsList.insert(0, Dialog)
