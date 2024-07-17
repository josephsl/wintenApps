# Windows app controls repository
# Copyright 2015-2024 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.
# No longer included in the add-on package but kept in code repository.

import globalPluginHandler
import UIAHandler
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
		if UIAHandler._isDebug():
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
			if UIAHandler._isDebug():
				log.debug("HandleNotificationEvent: event received while not fully initialized")
			return
		import NVDAObjects.UIA

		# NVDA Core issue 16871: some elements do not report native window handle when in fact
		# native window handle is shown via runtime ID.
		# This is seen when handling Windows 11 Voice Access notifications.
		if not (window := self.getNearestWindowHandle(sender)):
			if any(runtimeID := sender.getRuntimeID()):
				# Second item in runtime ID array is native window handle.
				window = runtimeID[1]
			else:
				# No runtime ID (tuple is empty).
				if UIAHandler._isDebug():
					log.debugWarning(
						"HandleNotificationEvent: native window handle not found in runtime ID: "
						f"NotificationProcessing={NotificationProcessing} "
						f"displayString={displayString} "
						f"activityId={activityId}"
					)
					return
		try:
			obj = NVDAObjects.UIA.UIA(windowHandle=window, UIAElement=sender)
		except Exception:
			if UIAHandler._isDebug():
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
			if UIAHandler._isDebug():
				log.debug(
					"HandleNotificationEvent: Ignoring because no object: "
					f"NotificationProcessing={NotificationProcessing} "
					f"displayString={displayString} "
					f"activityId={activityId}",
				)
			return
		if UIAHandler._isDebug():
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


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super().__init__()
		# Add extra things for UIA support if required.
		UIAHandler.terminate()
		# Hack: add extra events and such via an extended UIAHandler class.
		if not config.conf["UIA"]["enabled"]:
			raise RuntimeError("UIA forcefully disabled in configuration")
		try:
			UIAHandler.handler = UIAHandlerEx()
		except UIAHandler.COMError:
			UIAHandler.handler = None
			raise
