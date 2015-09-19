# WinTenApps/calculator.py
# Part of Windows 10 App Essentials collection
# Copyright 2015 Joseph Lee, released under GPL.

# Provides enhanced support for modern Calculator, including announcing results.

import appModuleHandler
import api
import controlTypes
from NVDAObjects.UIA import UIA
import queueHandler


class AppModule(appModuleHandler.AppModule):

	def script_enter(self, gesture):
		gesture.send()
		# Hack: only announce display text when an actual calculator button (usually equals button) is pressed.
		focus = api.getFocusObject()
		if focus.role == controlTypes.ROLE_BUTTON and focus.UIAElement.cachedAutomationID != "NavButton":
			result = api.getForegroundObject().children[1].children[2]
			if result.UIAElement.cachedAutomationID != "CalculatorResults":
				# Programmer mode is active.
				result = result.simplePrevious
			if result.UIAElement.cachedAutomationID == "CalculatorResults":
				queueHandler.queueFunction(queueHandler.eventQueue, result.setFocus)

	__gestures={
		"kb:enter":"enter",
		"kb:numpadEnter":"enter"
	}
