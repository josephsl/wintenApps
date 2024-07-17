# Windows app controls repository
# Copyright 2015-2024 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.
# No longer included in the add-on package but kept in code repository.

import globalPluginHandler
import UIAHandler
from typing import Optional
from comtypes import (
	COMError,
	COMObject,
)
import config
import eventHandler
from logHandler import log


# Extended UIA handler to handle notification events from apps without objects.
class UIAHandlerEx(UIAHandler.UIAHandler):

	def IUIAutomationNotificationEventHandler_HandleNotificationEvent(
		self,
		sender,
		NotificationKind,
		NotificationProcessing,
		displayString,
		activityId,
	):
		if _isDebug():
			log.debug(
				"handleNotificationEvent called "
				f"with notificationKind {self.getUIANotificationKindDebugString(NotificationKind)}, "
				f"notificationProcessing {self.getUIANotificationProcessingValueDebugString(NotificationProcessing)}, "
				f"displayString {str(displayString)[:50]}, "
				f"activityID {activityId}, "
				f"for element {self.getUIAElementDebugString(sender)}",
			)
		if not self.MTAThreadInitEvent.is_set():
			# UIAHandler hasn't finished initialising yet, so just ignore this event.
			if _isDebug():
				log.debug("HandleNotificationEvent: event received while not fully initialized")
			return
		import NVDAObjects.UIA

		try:
			obj = NVDAObjects.UIA.UIA(UIAElement=sender)
		except Exception:
			if _isDebug():
				log.debugWarning(
					"HandleNotificationEvent: Exception while creating object: "
					f"NotificationProcessing={NotificationProcessing} "
					f"displayString={displayString} "
					f"activityId={activityId}",
					exc_info=True,
				)
			return
		if not obj:
			# Sometimes notification events can be fired on a UIAElement that has no windowHandle and does not connect through parents back to the desktop.
			# There is nothing we can do with these.
			if _isDebug():
				log.debug(
					"HandleNotificationEvent: Ignoring because no object: "
					f"NotificationProcessing={NotificationProcessing} "
					f"displayString={displayString} "
					f"activityId={activityId}",
				)
			return
		if _isDebug():
			log.debug(
				"Queuing UIA_notification NVDA event " f"for NVDAObject {obj}",
			)
		eventHandler.queueEvent(
			"UIA_notification",
			obj,
			notificationKind=NotificationKind,
			notificationProcessing=NotificationProcessing,
			displayString=displayString,
			activityId=activityId,
		)


handler: Optional[UIAHandler] = None


def initialize():
	global handler
	if not config.conf["UIA"]["enabled"]:
		raise RuntimeError("UIA forcefully disabled in configuration")
	try:
		handler = UIAHandler()
	except COMError:
		handler = None
		raise


def terminate():
	global handler
	if handler:
		handler.terminate()
		handler = None


def _isDebug():
	return config.conf["debugLog"]["UIA"]


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Placeholder global plugin class in case it is needed in the future.
	pass
