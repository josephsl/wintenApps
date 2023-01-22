# Windows app controls repository
# Copyright 2015-2023 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.

import globalPluginHandler
from NVDAObjects.UIA import Dialog
import globalVars
import UIAHandler
import controlTypes
import ui
import winVersion


# #20: don't even think about proceeding in secure screens.
def disableInSecureMode(cls):
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super().__init__()
		from logHandler import log
		currentWinVer = winVersion.getWinVer()
		# Report processor architecture at startup.
		# Resolved in NVDA 2023.1.
		if not hasattr(currentWinVer, "processorArchitecture"):
			import platform
			log.info(f"winapps: processor architecture: {platform.machine()}")
		# Is this a Windows 11 22H2 beta build (2262x)?
		if currentWinVer.build in (22622, 22623):
			log.info("winapps: Windows 11 22H2 beta detected")

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		try:
			UIAClassName = obj.UIAElement.cachedClassName
		except AttributeError:
			UIAClassName = ""
		# Windows that are really dialogs.
		# Some dialogs, although listed as a dialog thanks to UIA class name,
		# does not advertise the proper role of dialog.
		# This is still the case with some dialogs such as restart to install updates dialog in Windows 11.
		if UIAClassName in UIAHandler.UIADialogClassNames and Dialog not in clsList:
			clsList.insert(0, Dialog)

	def _detectEmptyFolder(self, obj):
		clientObject = UIAHandler.handler.clientObject
		condition = clientObject.CreatePropertyCondition(UIAHandler.UIA_ClassNamePropertyId, "UIItemsView")
		uiItemWindow = clientObject.ElementFromHandleBuildCache(
			obj.windowHandle, UIAHandler.handler.baseCacheRequest
		)
		# Instantiate UIA object directly.
		# In order for this to work, a valid UIA pointer must be returned.
		try:
			uiItems = UIA(
				UIAElement=uiItemWindow.FindFirstBuildCache(
					UIAHandler.TreeScope_Descendants, condition, UIAHandler.handler.baseCacheRequest
				)
			)
		except ValueError:
			return
		lastUIItem = uiItems.lastChild
		if (
			isinstance(lastUIItem, UIA)
			and lastUIItem.role == controlTypes.Role.STATICTEXT
			and lastUIItem.UIAElement.currentClassName == "Element"
		):
			ui.message(lastUIItem.name)

	def event_nameChange(self, obj, nextHandler):
		# Originally written by Javi Dominguez as part of Explorer Enhancements add-on.
		# Ideally this should be part of File Explorer app module but to avoid conflicts with other add-ons...
		if obj.appModule.appName == "explorer" and obj.windowClassName == "ShellTabWindowClass":
			self._detectEmptyFolder(obj)
		nextHandler()

	def event_focusEntered(self, obj, nextHandler):
		# Originally written by Javi Dominguez as part of Explorer Enhancements add-on.
		# Ideally this should be part of File Explorer app module but to avoid conflicts with other add-ons...
		if (
			obj.appModule.appName == "explorer"
			and isinstance(obj, UIA)
			and obj.role == controlTypes.Role.LIST
			and obj.UIAElement.currentClassName == "UIItemsView"
		):
			self._detectEmptyFolder(obj.parent.parent)
		nextHandler()
