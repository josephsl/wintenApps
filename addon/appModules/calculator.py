# Joseph Lee
# Experimental UIA/app module for new style Calculator in Windows 10

import appModuleHandler
import api
import controlTypes
from NVDAObjects.UIA import UIA
import queueHandler
import tones
import time


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
		"kb:enter":"enter"
	}
