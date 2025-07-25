# Windows app controls repository
# Copyright 2015-2025 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 11.

import globalPluginHandler
import appModuleHandler
import globalVars
import UIAHandler
from UIAHandler import _isDebug, COMError
import config
import eventHandler
import winVersion
from logHandler import log


# Determine UIA notification processing on behalf of app modules.
# Resolved in NVDA 2025.2 (part of app modules).
def winapps_shouldProcessUIANotificationEvent(
	sender: UIAHandler.UIA.IUIAutomationElement,
	notificationKind: int | None = None,
	notificationProcessing: int | None = None,
	displayString: str = "",
	activityId: str = "",
) -> bool:
	"""
	Determines whether NVDA should process a UIA notification event.
	By default, events from elements with window handle value set
	and traversable back to the desktop will be accepted.
	Returning False will cause the event to be dropped completely.
	Returning True means that the event will be processed, but it might still
	be rejected later; e.g. because it isn't native UIA, because
	shouldAcceptEvent returns False, etc.
	"""
	# By default, see if UIA tree can be traversed to arrive at the desktop element.
	return bool(UIAHandler.handler.getNearestWindowHandle(sender))


# Don't even think about proceeding in secure screens.
# Don't worry about "cls" type.
def disableInSecureMode(cls):  # type: ignore
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super().__init__()
