# Windows app controls repository
# Copyright 2015-2023 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.

from typing import List
import globalPluginHandler
from NVDAObjects.UIA import Dialog
from NVDAObjects import NVDAObject
import NVDAObjects
import globalVars
import UIAHandler
import eventHandler


virtualDesktopName = None


def handlePossibleDesktopNameChange():
	"""
	Reports the new virtual desktop name if changed.
	On Windows versions lower than Windows 10, this function does nothing.
	"""
	global virtualDesktopName
	if virtualDesktopName:
		import ui
		ui.message(virtualDesktopName)
		virtualDesktopName = None


def winapps_doPreGainFocus(obj: "NVDAObjects.NVDAObject", sleepMode: bool = False) -> bool:
	from IAccessibleHandler import SecureDesktopNVDAObject
	from utils.security import objectBelowLockScreenAndWindowsIsLocked
	import config
	from logHandler import log
	import api
	import speech

	if objectBelowLockScreenAndWindowsIsLocked(
		obj,
		shouldLog=config.conf["debugLog"]["events"],
	):
		return False
	oldFocus = api.getFocusObject()
	oldTreeInterceptor = oldFocus.treeInterceptor if oldFocus else None
	if not api.setFocusObject(obj):
		return False
	if speech.manager._shouldCancelExpiredFocusEvents():
		log._speechManagerDebug("executeEvent: Removing cancelled speech commands.")
		# ask speechManager to check if any of it's queued utterances should be cancelled
		# Note: Removing cancelled speech commands should happen after all dependencies for the isValid check
		# have been updated:
		# - obj.WAS_GAIN_FOCUS_OBJ_ATTR_NAME
		# - api.setFocusObject()
		# - api.getFocusAncestors()
		# When these are updated:
		# - obj.WAS_GAIN_FOCUS_OBJ_ATTR_NAME
		#   - Set during creation of the _CancellableSpeechCommand.
		# - api.getFocusAncestors() via api.setFocusObject() called in doPreGainFocus
		speech._manager.removeCancelledSpeechCommands()

	if (
		api.getFocusDifferenceLevel() <= 1
		# This object should not set off a foreground event.
		# SecureDesktopNVDAObject uses a gainFocus event to trigger NVDA
		# to sleep as the secure instance of NVDA starts for the
		# secure desktop.
		# The newForeground object fetches from the User Desktop,
		# not the secure desktop.
		and not isinstance(obj, SecureDesktopNVDAObject)
	):
		newForeground = api.getDesktopObject().objectInForeground()
		if not newForeground:
			log.debugWarning("Can not get real foreground, resorting to focus ancestors")
			ancestors = api.getFocusAncestors()
			if len(ancestors) > 1:
				newForeground = ancestors[1]
			else:
				newForeground = obj
		if not api.setForegroundObject(newForeground):
			return False
		eventHandler.executeEvent('foreground', newForeground)
	handlePossibleDesktopNameChange()
	if sleepMode: return True
	#Fire focus entered events for all new ancestors of the focus if this is a gainFocus event
	for parent in api.getFocusAncestors()[api.getFocusDifferenceLevel():]:
		eventHandler.executeEvent("focusEntered",parent)
	if obj.treeInterceptor is not oldTreeInterceptor:
		if hasattr(oldTreeInterceptor,"event_treeInterceptor_loseFocus"):
			oldTreeInterceptor.event_treeInterceptor_loseFocus()
		if obj.treeInterceptor and obj.treeInterceptor.isReady and hasattr(obj.treeInterceptor,"event_treeInterceptor_gainFocus"):
			obj.treeInterceptor.event_treeInterceptor_gainFocus()
	return True


# #20: don't even think about proceeding in secure screens.
def disableInSecureMode(cls):
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super().__init__()
		# Patch event handler if NVDA does not support virtual desktop switch announcements.
		if not hasattr(eventHandler, "handlePossibleDesktopNameChange"):
			eventHandler.doPreGainFocus = winapps_doPreGainFocus

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: List[NVDAObject]) -> None:
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
