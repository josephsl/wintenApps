# Windows app controls repository
# Copyright 2015-2024 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.

import globalPluginHandler
from NVDAObjects.UIA import Dialog
from NVDAObjects import NVDAObject
import globalVars
import UIAHandler
import versionInfo


# #20: don't even think about proceeding in secure screens.
def disableInSecureMode(cls):
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[NVDAObject]) -> None:
		if versionInfo.version_year >= 2024:
			return
		try:
			UIAClassName = obj.UIAElement.cachedClassName
		except AttributeError:
			return
		# Windows that are really dialogs.
		# Some dialogs, although listed as a dialog thanks to UIA class name,
		# does not advertise the proper role of dialog.
		# This is still the case with some dialogs such as restart to install updates dialog in Windows 11.
		# Resolved in NVDA 2024.1 (turns out there was a flaw with IsDialog property check in NVDA Core).
		if UIAClassName in UIAHandler.UIADialogClassNames and Dialog not in clsList:
			clsList.insert(0, Dialog)
