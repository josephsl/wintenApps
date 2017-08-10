# WinTenApps/calculator.py
# Part of Windows 10 App Essentials collection
# Copyright 2015-2017 Joseph Lee, released under GPL.

# Provides enhanced support for modern Calculator, including announcing results.

import appModuleHandler
import api
import controlTypes
from NVDAObjects.UIA import UIA
import queueHandler
import ui

# Filter live region change elements to avoid repeated announcements.
# A dedicated function is provded to react to future Calculator changes.
def shouldLiveRegionChangeProceed(obj):
	automationID = obj.UIAElement.cachedAutomationID
	if automationID == "DateDiffAllUnitsResultLabel":
		return True
	elif automationID == "":
		prevAutomationID = obj.previous.UIAElement.cachedAutomationID
		if prevAutomationID == "negateButton":
			return False
		elif prevAutomationID == "numberPad":
			return api.getForegroundObject().children[1].children[3].UIAElement.cachedAutomationID != "CalculatorResults"
	return False


class AppModule(appModuleHandler.AppModule):

	shouldAnnounceResult = False

	def event_nameChange(self, obj, nextHandler):
		if not self.shouldAnnounceResult:
			return
		self.shouldAnnounceResult = False
		nextHandler()

	def event_UIA_liveRegionChanged(self, obj, nextHandler):
		# Unfortunately, the control that fires this has no automation ID yet says it is a generic te4xt block.
		# This may mean anything can be announced, so try to filter them.
		if shouldLiveRegionChangeProceed(obj):
			nextHandler()

	try:
		event_liveRegionChange = event_UIA_liveRegionChanged
	except:
		pass

	def script_calculatorResult(self, gesture):
		# To prevent double focus announcement, check where we are.
		focus = api.getFocusObject()
		navMenu = False
		if isinstance(focus, UIA) and isinstance(focus.parent.parent, UIA) and focus.parent.parent.UIAElement.cachedAutomationID == "FlyoutNav":
			navMenu = True
		gesture.send()
		# In redstone, calculator result keeps firing name change, so tell it to do so if and only if enter has been pressed.
		self.shouldAnnounceResult = True
		# Hack: only announce display text when an actual calculator button (usually equals button) is pressed.
		# In redstone, pressing enter does not move focus to equals button.
		if isinstance(focus, UIA):
			if focus.UIAElement.cachedAutomationID == "CalculatorResults":
				queueHandler.queueFunction(queueHandler.eventQueue, focus.reportFocus)
			elif focus.UIAElement.cachedAutomationID != "NavButton":
				# In newer releases, result is located on the same spot in the object hierarchy.
				result = api.getForegroundObject().children[1].children[3]
				if result.UIAElement.cachedAutomationID == "CalculatorResults" and not navMenu:
					# And no, do not allow focus to move.
					queueHandler.queueFunction(queueHandler.eventQueue, result.reportFocus)

	__gestures={
		"kb:enter":"calculatorResult",
		"kb:numpadEnter":"calculatorResult",
		"kb:escape":"calculatorResult"
	}
