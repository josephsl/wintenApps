# Windows 11 Calculator
# Part of Windows App Essentials collection
# Copyright 2021 Joseph Lee, released under GPL

"""App module for redesigned modern Calculator on Windows 11"""

# This is similar to older Calculator app but was redesigned from ground up.
# NVDA Core includes bulk of this app module.
from nvdaBuiltin.appModules.calculator import *  # NOQA: F403
import api
import queueHandler
import ui
from NVDAObjects.UIA import UIA
import braille
import scriptHandler


# Mypy should be reminded that this app module is powered by built-in Calculator app module.
# Inform Flake8 as well.
class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405

	def event_NVDAObject_init(self, obj):
		if not isinstance(obj, UIA):
			return
		# Version 10.2009 introduces a regression where history and memory items have no names
		# but can be fetched through its children.
		if not obj.name and obj.parent.UIAAutomationId in ("HistoryListView", "MemoryListView"):
			obj.name = "".join([item.name for item in obj.children])

	def event_UIA_notification(self, obj, nextHandler, displayString=None, activityId=None, **kwargs):
		# Some notification messages are repeated (most notable being graph view change notification).
		if activityId == "GraphViewChanged" and self._resultsCache == displayString:
			return
		self._resultsCache = displayString
		# Version 10.2109 changes the UI a bit, requiring custom event handler implementation.
		# NVDA Core issue 12268: for "DisplayUpdated", announce display strings in braille and move on.
		if activityId == "DisplayUpdated":
			braille.handler.message(displayString)
		try:
			shouldAnnounceNotification = (
				obj.previous.UIAAutomationId in
				("numberPad", "UnitConverterRootGrid")
			)
		except AttributeError:
			# The actual display text and other controls live inside a toggle control window.
			# Therefore move one more level down compared to older Calculator releases.
			resultElement = api.getForegroundObject().children[1].lastChild.firstChild
			# Redesigned in 2019 due to introduction of "always on top" i.e. compact overlay mode.
			if resultElement.UIAElement.cachedClassName != "LandmarkTarget":
				resultElement = resultElement.parent.children[1]
			shouldAnnounceNotification = (
				resultElement
				and resultElement.firstChild
				and resultElement.firstChild.UIAAutomationId not in noCalculatorEntryAnnouncements  # NOQA: F405
			)
		# Display updated activity ID seen when entering calculations should be ignored
		# as as it is redundant if speak typed characters is on.
		if shouldAnnounceNotification or activityId != "DisplayUpdated":
			nextHandler()

	# A list of native commands to handle calculator result announcement.
	_calculatorResultGestures = (
		"kb:enter",
		"kb:numpadEnter",
		"kb:escape",
		"kb:delete",
		"kb:numpadDelete"
	)

	@scriptHandler.script(gestures=_calculatorResultGestures)
	def script_calculatorResult(self, gesture):
		# To prevent double focus announcement, check where we are.
		focus = api.getFocusObject()
		gesture.send()
		# In newer app releases, calculator result keeps firing name change event,
		# so tell it to do so if and only if enter has been pressed.
		self._shouldAnnounceResult = True
		# Hack: only announce display text when an actual calculator button (usually equals button) is pressed.
		# In newer app releases, pressing enter does not move focus to equals button.
		if isinstance(focus, UIA):
			if focus.UIAAutomationId in ("CalculatorResults", "CalculatorAlwaysOnTopResults"):
				queueHandler.queueFunction(queueHandler.eventQueue, ui.message, focus.name)
			else:
				resultsScreen = api.getForegroundObject().children[1].lastChild
				if isinstance(resultsScreen, UIA) and resultsScreen.UIAElement.cachedClassName == "LandmarkTarget":
					# And no, do not allow focus to move.
					queueHandler.queueFunction(queueHandler.eventQueue, ui.message, resultsScreen.firstChild.name)
