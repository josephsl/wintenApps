# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2020-2023 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for Windows 10 Calculator.
This is also the base app module for Windows 11 Calculator."""

from nvdaBuiltin.appModules.calculator import AppModule, noCalculatorEntryAnnouncements  # NOQA: F403
import braille


class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405

	def event_UIA_notification(self, obj, nextHandler, displayString=None, activityId=None, **kwargs):
		# When no results shortcuts such as number row keys are pressed, display content will be announced.
		# #13383: it might be possible that the next command is a calculation shortcut such as S for sine.
		# Therefore, clear no result gestures flag from the app module while storing a copy of the flag here.
		# The event handler copy is used to handle the overall notification announcement later.
		doNotAnnounceCalculatorResults = self._noCalculatorResultsGesturePressed
		self._noCalculatorResultsGesturePressed = False
		# #12268: for "DisplayUpdated", announce display strings in braille  no matter what they are.
		# There are other activity Id's such as "MemorySlotAdded" and "MemoryCleared"
		# but they do not involve number entry.
		# Therefore, only handle the below activity Id.
		if activityId == "DisplayUpdated":
			braille.handler.message(displayString)
			# Locate results via UIA tree traversal.
			# Redesigned in 2019 due to introduction of "always on top" i.e. compact overlay mode.
			# Resolved in NVDA 2023.2 (remove this method completely).
			import UIAHandler
			from . import appmodUtils
			try:
				resultElement = appmodUtils.findUIADescendant(
					obj, UIAHandler.UIA_ClassNamePropertyId, "LandmarkTarget"
				)
			except LookupError:
				resultElement = None
			# Display string announcement is redundant if speak typed characters is on.
			if (
				resultElement
				and resultElement.firstChild
				and resultElement.firstChild.UIAAutomationId in noCalculatorEntryAnnouncements
				and doNotAnnounceCalculatorResults
			):
				return
		nextHandler()
