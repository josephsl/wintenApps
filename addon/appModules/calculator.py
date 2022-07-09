# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015-2022 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Extend NVDA Core's Calculator module.
from nvdaBuiltin.appModules.calculator import AppModule, noCalculatorEntryAnnouncements
import api
import braille
import scriptHandler


# Mypy should be reminded that this app module is powered by built-in Calculator app module.
class AppModule(AppModule):  # type: ignore[no-redef]

	# NVDA Core issue 13383: For some commands (such as number row keys),
	# NVDA should not announce calculator results.
	# Resolved in NVDA 2022.2.
	_noCalculatorResultsGesturePressed = False

	def event_UIA_notification(self, obj, nextHandler, displayString=None, activityId=None, **kwargs):
		# NVDA Core issue 13383: When no results shortcuts such as number row keys are pressed,
		# display content will be announced.
		# But it might be possible that the next command is a calculation shortcut such as S for sine.
		# Therefore, clear no results flag from the app module while storing a copy of the flag here.
		# The event handler copy is used to handle the overall notification announcement later.
		# Resolved in NVDA 2022.2.
		doNotAnnounceCalculatorResults = self._noCalculatorResultsGesturePressed
		self._noCalculatorResultsGesturePressed = False
		# Version 10.2109 changes the UI a bit, requiring tweaked event handler implementation.
		# Version bumped to 11 in October 2021.
		# This, together with results handling, are part of NVDA 2022.1.
		calculatorVersion = int(self.productVersion.split(".")[0])
		# NVDA Core issue 12268: for "DisplayUpdated", announce display strings in braille.
		if activityId == "DisplayUpdated":
			braille.handler.message(displayString)
			resultElement = api.getForegroundObject().children[1].lastChild
			# In version 11, the actual display text and other controls live inside a toggle control window.
			# Therefore move one more level down compared to older Calculator releases.
			if calculatorVersion >= 11:
				resultElement = resultElement.firstChild
			# Redesigned in 2019 due to introduction of "always on top" i.e. compact overlay mode.
			if resultElement.UIAElement.cachedClassName != "LandmarkTarget":
				resultElement = resultElement.parent.children[1]
			# Display updated activity ID seen when entering calculations should be ignored
			# as as it is redundant if speak typed characters is on.
			# A key requirement is that do not announce results flag must be set.
			if (
				resultElement
				and resultElement.firstChild
				and resultElement.firstChild.UIAAutomationId in noCalculatorEntryAnnouncements
				and doNotAnnounceCalculatorResults
			):
				return
		nextHandler()

	def script_calculatorResult(self, gesture):
		# If the superclass version is invoked, it will result in double announcement
		# as NVDA will look for the display content element in addition to handling UIA notification event.
		# Therefore, send gestures (Escape, Enter, Delete) and no more.
		# Resolved in NVDA 2022.2.
		gesture.send()

	# NVDA Core issue 13383: handle both number row and numpad with num lock on.
	# Resolved in NVDA 2022.2.
	@scriptHandler.script(
		gestures=[f"kb:{i}" for i in range(10)]
		+ [f"kb:numLockNumpad{i}" for i in range(10)]
	)
	def script_doNotAnnounceCalculatorResults(self, gesture):
		gesture.send()
		self._noCalculatorResultsGesturePressed = True
