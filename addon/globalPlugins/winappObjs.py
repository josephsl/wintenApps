# Windows app controls repository
# Copyright 2015-2022 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.

from typing import Dict
import globalPluginHandler
from NVDAObjects.UIA import UIA, Dialog
import queueHandler
import globalVars
import UIAHandler
from logHandler import log


# Add additional UIA events not included in NVDA Core.
additionalEvents: Dict[int, str] = {}


# Add additional property events not included in NVDA Core.
additionalPropertyEvents: Dict[int, str] = {}


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

	# Manually add events after root element is located.
	def _addAdditionalUIAEvents(self, delay: bool = False) -> None:
		# Add a series of events and properties instead of doing it one at a time.
		# Some events and properties are only available in a specific build range
		# and/or while a specific version of IUIAutomation interface is in use.
		if delay:
			log.debug("winapps: adding additional events and properties after a delay")
		# Use event handler group facility to add more events.
		# Internally powered by IUIAutomation6 interface introduced in Windows 10 1809.
		addonGlobalEventHandlerGroup = UIAHandler.handler.clientObject.CreateEventHandlerGroup()
		for event, name in additionalEvents.items():
			if event not in UIAHandler.UIAEventIdsToNVDAEventNames:
				UIAHandler.UIAEventIdsToNVDAEventNames[event] = name
				# Global event handler group set must be updated, too.
				UIAHandler.globalEventHandlerGroupUIAEventIds.add(event)
				addonGlobalEventHandlerGroup.addAutomationEventHandler(
					event,
					UIAHandler.TreeScope_Subtree,
					UIAHandler.handler.baseCacheRequest,
					UIAHandler.handler
				)
				log.debug(f"winapps: added event ID {event}, assigned to {name}")
		for event, name in additionalPropertyEvents.items():
			if event not in UIAHandler.UIAPropertyIdsToNVDAEventNames:
				UIAHandler.UIAPropertyIdsToNVDAEventNames[event] = name
				log.debug(f"winapps: added property event ID {event}, assigned to {name}")
				# Global property event handler group set must be updated, too.
				UIAHandler.globalEventHandlerGroupUIAPropertyIds.add(event)
		addonGlobalEventHandlerGroup.AddPropertyChangedEventHandler(
			UIAHandler.TreeScope_Subtree,
			UIAHandler.handler.baseCacheRequest,
			UIAHandler.handler,
			*UIAHandler.handler.clientObject.IntSafeArrayToNativeArray(additionalPropertyEvents)
		)
		UIAHandler.handler.addEventHandlerGroup(UIAHandler.handler.rootElement, addonGlobalEventHandlerGroup)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if not isinstance(obj, UIA):
			return
		# Windows that are really dialogs.
		# Some dialogs, although listed as a dialog thanks to UIA class name,
		# does not advertise the proper role of dialog.
		# This is still the case with some dialogs such as restart to install updates dialog in Windows 11.
		if obj.UIAElement.cachedClassName in UIAHandler.UIADialogClassNames and Dialog not in clsList:
			clsList.insert(0, Dialog)
