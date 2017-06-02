# WinTenApps/calculator.py
# Part of Windows 10 App Essentials collection
# Copyright 2015-2017 Joseph Lee, released under GPL.

# Provides enhanced support for modern Calculator, including announcing results.

import appModuleHandler
import api
import winVersion
import controlTypes
from NVDAObjects.UIA import UIA
import queueHandler

# Handle kwirks with calculation result.
class CalculatorResult(UIA):

	def event_nameChange(self):
		if not self.appModule.shouldAnnounceResult:
			return
		else:
			self.appModule.shouldAnnounceResult = False


class AppModule(appModuleHandler.AppModule):

	shouldAnnounceResult = False

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			# To handle calculator result announcement.
			if obj.UIAElement.cachedAutomationID == "CalculatorResults":
				clsList.insert(0, CalculatorResult)

	def script_calculatorResult(self, gesture):
		gesture.send()
		# In redstone, calculator result keeps firing name change, so tell it to do so if and only if enter has been pressed.
		self.shouldAnnounceResult = True
		# Hack: only announce display text when an actual calculator button (usually equals button) is pressed.
		focus = api.getFocusObject()
		# In redstone, pressing enter does not move focus to equals button.
		if isinstance(focus, CalculatorResult):
			queueHandler.queueFunction(queueHandler.eventQueue, focus.reportFocus)
		elif focus.role == controlTypes.ROLE_BUTTON and focus.UIAElement.cachedAutomationID != "NavButton":
			result = api.getForegroundObject().children[1].children[2]
			if result.UIAElement.cachedAutomationID != "CalculatorResults":
				# Programmer mode is active.
				result = result.simplePrevious
			if result.UIAElement.cachedAutomationID == "CalculatorResults":
				queueHandler.queueFunction(queueHandler.eventQueue, result.setFocus)

	__gestures={
		"kb:enter":"calculatorResult",
		"kb:numpadEnter":"calculatorResult",
		"kb:escape":"calculatorResult"
	}
