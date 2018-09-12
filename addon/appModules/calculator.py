# WinTenApps/calculator.py
# Part of Windows 10 App Essentials collection
# Copyright 2015-2018 Joseph Lee, released under GPL.

# Provides enhanced support for modern Calculator, including announcing results.

import appModuleHandler
import api
import controlTypes
from NVDAObjects.UIA import UIA
import queueHandler
import ui

# Filter live region change elements to avoid repeated announcements.
# A dedicated function is provided to react to future Calculator changes.
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

	def event_NVDAObject_init(self, obj):
		# Remove heading designation from calculator results, as the output is confusing.
		# Sometimes, this won't work because global plugin isn't loaded at that time.
		import globalPlugins
		try:
			if isinstance(obj, globalPlugins.wintenObjs.XAMLHeading):
				obj.role = controlTypes.ROLE_STATICTEXT
		except AttributeError:
			pass

	shouldAnnounceResult = False
	# Again, name change says the same thing multiple times for some items.
	resultsCache = ""

	def event_nameChange(self, obj, nextHandler):
		# No, announce value changes immediately except for calculator results.
		if isinstance(obj, UIA) and obj.UIAElement.cachedAutomationID != "CalculatorResults" and obj.name != self.resultsCache:
			# For unit conversion, UIA notification event presents much better messages.
			if obj.UIAElement.cachedAutomationID not in ("Value1", "Value2"):
				ui.message(obj.name)
			self.resultsCache = obj.name
		if not self.shouldAnnounceResult:
			return
		self.shouldAnnounceResult = False
		nextHandler()

	def event_liveRegionChange(self, obj, nextHandler):
		# Unfortunately, the control that fires this has no automation ID yet says it is a generic text block.
		# This may mean anything can be announced, so try to filter them.
		if shouldLiveRegionChangeProceed(obj):
			nextHandler()

	def event_UIA_notification(self, obj, nextHandler, **kwargs):
		# From May 2018 onwards, unit converter uses a different automation iD.
		# Changed significantly in July 2018 thanks to UI redesign, and as a result, attribute error is raised.
		try:
			shouldAnnounceNotification = obj.previous.UIAElement.cachedAutomationID in ("numberPad", "UnitConverterRootGrid")
		except AttributeError:
			shouldAnnounceNotification = api.getForegroundObject().children[1].lastChild.firstChild.UIAElement.cachedAutomationID != "CalculatorResults"
		if shouldAnnounceNotification:
			nextHandler()

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
