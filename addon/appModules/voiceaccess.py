# Voice access
# Part of Windows App Essentials collection
# Copyright 2022-2023 Joseph Lee, released under GPL

# Support for Voice access on Windows 11 22H2 and later.

from typing import List
import appModuleHandler
import scriptHandler
import ui
import winUser
from NVDAObjects.UIA import UIA
from NVDAObjects.behaviors import Dialog
from NVDAObjects import NVDAObject


class MicrophoneButton(UIA):

	@scriptHandler.script(gestures=["kb:space", "kb:enter", "kb:numpadEnter"])
	def script_toggleMicrophone(self, gesture) -> None:
		# Until NVDA gets a chance to handle UIA notifications when these commands are pressed...
		gesture.send()
		# There is no label for this button in build 25200 series, so consult its parent.
		ui.message(self.name if self.name else self.parent.name)


class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: List[NVDAObject]) -> None:
		if isinstance(obj, UIA):
			if obj.UIAElement.cachedClassName == "Popup":
				clsList.insert(0, Dialog)
			elif obj.UIAAutomationId == "MicrophoneButtonControl":
				clsList.insert(0, MicrophoneButton)

	def isGoodUIAWindow(self, hwnd):
		# #72: allow proper mouse and touch interaction from main Voice access interface.
		if winUser.getClassName(hwnd) == "Voice access":
			return True
		return False
