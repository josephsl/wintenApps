# Windows app controls repository
# Copyright 2015-2025 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.

import globalPluginHandler
import globalVars
import UIAHandler
import config
import eventHandler
from logHandler import log


# Extended UIA handler to handle notification events from apps without objects.
class UIAHandlerEx(UIAHandler.UIAHandler):

	def IUIAutomationNotificationEventHandler_HandleNotificationEvent(
		self,
		sender: UIAHandler.UIA.IUIAutomationElement,
		NotificationKind: int,
		NotificationProcessing: int,
		displayString: str,
		activityId: str,
	) -> None:
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
			# Some runtime ID array has four elements, while others do not, and for Voice Access, it is four.
			# Therefore, handle runtime ID tuple of four elements.
			if len(runtimeID := sender.getRuntimeID()) == 4:
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
		# Hack: add extra things for UIA support if required and uIA is enabled.
		if not config.conf["UIA"]["enabled"]:
			raise RuntimeError("UIA forcefully disabled in configuration")
		# Add support for enhanced notification events (to handle apps such as Windows 11 Voice Access).
		log.debug("winapps: restarting UIA handler to add additional events")
		UIAHandler.terminate()
		try:
			UIAHandler.handler = UIAHandlerEx()
			log.debug("winapps: UIA handler restarted")
		except UIAHandler.COMError:
			UIAHandler.handler = None
			raise
