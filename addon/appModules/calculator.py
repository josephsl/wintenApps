# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015-2021 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for Windows 10 Calculator"""

# NVDA Core includes bulk of this app module.
from nvdaBuiltin.appModules.calculator import *  # NOQA: F403
import api
import queueHandler
import ui
from NVDAObjects.UIA import UIA
import braille


# Mypy should be reminded that this app module is powered by built-in Calculator app module.
# Inform Flake8 as well.
class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405

	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		# Add additional Calculator result gestures until they are added to NVDA Core.
		self.bindGesture("kb:delete", "calculatorResult")
		self.bindGesture("kb:numpadDelete", "calculatorResult")

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
		# NVDA Core issue 12268: for "DisplayUpdated", announce display strings in braille and move on.
		if activityId == "DisplayUpdated":
			braille.handler.message(displayString)
		# Call the built-in app module version of UIA notification event handler.
		super(AppModule, self).event_UIA_notification(obj, nextHandler, activityId=activityId, **kwargs)

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
