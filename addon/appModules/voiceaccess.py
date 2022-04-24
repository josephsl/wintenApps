# Voice access
# Part of Windows App Essentials collection
# Copyright 2022 Joseph Lee, released under GPL

# Support for Windows 11 Voice access (Version 22H2).

import appModuleHandler
import scriptHandler
import ui
from NVDAObjects.UIA import UIA
from NVDAObjects.behaviors import Dialog


class MicrophoneButton(UIA):

	@scriptHandler.script(gestures=["kb:space", "kb:enter", "kb:numpadEnter"])
	def script_toggleMicrophone(self, gesture):
		# Until NVDA gets a chance to handle UIA notifications when these commands are pressed...
		gesture.send()
		ui.message(self.name)


class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			if obj.UIAElement.cachedClassName == "Popup":
				clsList.insert(0, Dialog)
			elif obj.UIAAutomationId == "MicrophoneButtonControl":
				clsList.insert(0, MicrophoneButton)
