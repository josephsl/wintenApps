# Windows app controls repository
# Copyright 2015-2023 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10 and later.

from typing import List, Optional, Dict, Callable
import globalPluginHandler
from NVDAObjects.UIA import UIA, Dialog
from NVDAObjects import NVDAObject
import NVDAObjects
import globalVars
import UIAHandler
import eventHandler
import controlTypes
import ui
import scriptHandler
import core
import addonHandler
addonHandler.initTranslation()


# Virtual desktop announcements come from a combination of this add-on and an NVDA Core pull request.
# Resolved in NVDA 2023.2.
virtualDesktopName: Optional[str] = None


def handlePossibleDesktopNameChange():
	"""
	Reports the new virtual desktop name if changed.
	On Windows versions lower than Windows 10, this function does nothing.
	"""
	global virtualDesktopName
	if virtualDesktopName:
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
	if sleepMode:
		return True
	# Fire focus entered events for all new ancestors of the focus if this is a gainFocus event
	for parent in api.getFocusAncestors()[api.getFocusDifferenceLevel():]:
		eventHandler.executeEvent("focusEntered", parent)
	if obj.treeInterceptor is not oldTreeInterceptor:
		if hasattr(oldTreeInterceptor, "event_treeInterceptor_loseFocus"):
			oldTreeInterceptor.event_treeInterceptor_loseFocus()
		if (
			obj.treeInterceptor
			and obj.treeInterceptor.isReady
			and hasattr(obj.treeInterceptor, "event_treeInterceptor_gainFocus")
		):
			obj.treeInterceptor.event_treeInterceptor_gainFocus()
	return True


# Transferred from File Explorer app module in 2023.
# Insider Preview (dev/canary) introduced enhancements to taskbar item position reporting,
# including rearranged position reporting (25267) and item position (25281), both removed in 25352.
# Therefore emulate these changes on other Windows 11 builds via the below overlay class.
# On Windows 10, taskbar item rearrangement via keyboard is unavailable.
# Emulated feature, might be disabled or removed in the future.
class TaskbarItem(NVDAObject):

	def _get_itemName(self) -> str:
		# Icon name contains open window count if windows are open after a hyphen (-).
		return self.name.rpartition(" - ")[0] if " -" in self.name else self.name

	def announceDragPosition(self) -> None:
		# Rearranging taskbar items with the keyboard is possible in Windows 11.
		# Reporting this info is included in build 25267 and removed in 25352.
		# Inform mypy about gettext call.
		import gettext
		_ = gettext.gettext
		left = self.previous if isinstance(self.previous, TaskbarItem) else None
		right = self.next if isinstance(self.next, TaskbarItem) else None
		if left and right:
			# Translators: announced when rearranging taskbar icons in Windows 11.
			ui.message(_("{appName} moved between {previousAppName} and {nextAppName}").format(
				appName=self.itemName, previousAppName=left.itemName, nextAppName=right.itemName
			))
		elif left and not right:
			# Translators: announced when rearranging taskbar icons in Windows 11.
			ui.message(_("{appName} moved to end of the apps list").format(appName=self.itemName))
		elif right and not left:
			# Translators: announced when rearranging taskbar icons in Windows 11.
			ui.message(_("{appName} moved to beginning of the apps list").format(appName=self.itemName))

	@scriptHandler.script(gesture="kb:alt+shift+rightArrow")
	def script_moveRight(self, gesture) -> None:
		announcePosition = isinstance(self, UIA) and isinstance(self.next, TaskbarItem)
		gesture.send()
		if announcePosition:
			core.callLater(1, self.announceDragPosition)

	@scriptHandler.script(gesture="kb:alt+shift+leftArrow")
	def script_moveLeft(self, gesture) -> None:
		announcePosition = isinstance(self, UIA) and isinstance(self.previous, TaskbarItem)
		gesture.send()
		if announcePosition:
			core.callLater(1, self.announceDragPosition)


# #20: don't even think about proceeding in secure screens.
def disableInSecureMode(cls):
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super().__init__()
		# Patch event handler if NVDA does not support virtual desktop switch announcements.
		# Resolved in NVDA 2023.2.
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

	def event_nameChange(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# NVDA Core issue 5641: try catching virtual desktop switch event,
		# which will result in name change for the desktop object.
		# Do this while NVDA Core itself does not include virtual desktop switch announcement facility.
		# Resolved in NVDA 2023.2 (remove this method completely).
		if (
			obj.appModule.appName == "csrss"
			and obj.windowClassName == "#32769"
			and not hasattr(eventHandler, "handlePossibleDesktopNameChange")
		):
			global virtualDesktopName
			virtualDesktopName = obj.name
			core.callLater(100, handlePossibleDesktopNameChange)
		nextHandler()
