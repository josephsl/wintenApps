# Voice access
# Part of Windows App Essentials collection
# Copyright 2022-2023 Joseph Lee, released under GPL

# Support for Voice access on Windows 11 22H2 and later.

from typing import List
import appModuleHandler
import scriptHandler
import ui
import winUser
from NVDAObjects.UIA import UIA, Dialog
from NVDAObjects import NVDAObject
from winAPI.types import HWNDValT


# Deprecated: inaccurate announcements (perhaps due to input timing) and cannot be toggled using mouse/touch.
class MicrophoneButton(UIA):

	def announceMicStatus(self):
		ui.message(self.name)

	@scriptHandler.script(gestures=["kb:space", "kb:enter", "kb:numpadEnter"])
	def script_toggleMicrophone(self, gesture) -> None:
		# Until NVDA gets a chance to handle UIA notifications when these commands are pressed...
		gesture.send()
		import core
		core.callLater(1, self.announceMicStatus)


class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: List[NVDAObject]) -> None:
		if isinstance(obj, UIA):
			if obj.UIAElement.cachedClassName == "Popup":
				clsList.insert(0, Dialog)
			elif obj.UIAAutomationId == "MicrophoneButtonControl":
				clsList.insert(0, MicrophoneButton)

	def isGoodUIAWindow(self, hwnd: HWNDValT) -> bool:
		# #72: allow proper mouse and touch interaction from main Voice access interface.
		if winUser.getClassName(hwnd) == "Voice access":
			return True
		return False
