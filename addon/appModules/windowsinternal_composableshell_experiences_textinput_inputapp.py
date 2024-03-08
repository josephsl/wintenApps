# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2017-2024 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# The add-on version of this module will extend the one that comes with NVDA Core.

from typing import Callable, Optional
# Yes, this app module is powered by built-in modern keyboard (TextInputHost) app module
# (formerly WindowsInternal.ComposableShell.Experiences.TextInput.InputApp).
# #70: NVDA Core pull requests are made using the core app module, not alias modules.
from nvdaBuiltin.appModules.windowsinternal_composableshell_experiences_textinput_inputapp import (
	AppModule, ImeCandidateItem
)
import winVersion
import eventHandler
import api
from NVDAObjects import NVDAObject


# Built-in modern keyboard app module powers bulk of the below app module class, so inform Mypy.
class AppModule(AppModule):  # type: ignore[no-redef]

	def event_UIA_elementSelected(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# Do not proceed if emoji panel category item is selected when the panel is closed in Windows 11.
		if obj.UIAAutomationId.startswith("navigation-menu-item"):
			focus = api.getFocusObject()
			# System focus restored.
			if focus.appModule != self:
				return
			# NVDA is stuck in a nonexistent edit field.
			# Focus object location can be None sometimes.
			if not any(focus.location):
				eventHandler.queueEvent("gainFocus", obj.objectWithFocus())
				return
		# NVDA Core takes care of the rest.
		super().event_UIA_elementSelected(obj, nextHandler)

	def event_UIA_window_windowOpen(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# Ask NVDA to respond to UIA events coming from modern keyboard interface.
		# Focus change event will not work, as it'll cause focus to be lost when the panel closes.
		# This is more so on Windows 10.
		firstChild = obj.firstChild
		# Sometimes window open event is raised when the input panel closes.
		if firstChild is None:
			return
		# Register modern keyboard interface elements with local event handler group.
		# Used to handle events from non-focused elements.
		# (mostly for hardware keyboard input suggestions).
		# In Windows 11, combined emoji panel and clipboard history moves system focus to itself.
		if (
			firstChild.UIAAutomationId == "IME_Prediction_Window"
		):
			# Announce the first candidate (hardware keyboard input suggestion or IME candidate).
			imeCandidateItem = firstChild.firstChild.firstChild
			# In Windows 11, an extra element is located between candidate UI window and items themselves.
			if isinstance(imeCandidateItem, ImeCandidateItem):
				# For some odd reason, suggested text is the last element.
				imeCandidateItem = imeCandidateItem.lastChild
			imeCandidateItem.reportFocus()
		# NVDA Core takes care of the rest.
		super().event_UIA_window_windowOpen(obj, nextHandler)

	def event_gainFocus(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# Focus gets stuck in Modern keyboard when clipboard history closes in Windows 11.
		if obj.parent.childCount == 0:
			# Do not queue events if events are pending.
			if not eventHandler.isPendingEvents():
				eventHandler.queueEvent("gainFocus", obj.objectWithFocus())
			return
		nextHandler()

	def event_UIA_notification(
			self,
			obj: NVDAObject,
			nextHandler: Callable[[], None],
			displayString: Optional[str] = None,
			activityId: Optional[str] = None,
			**kwargs
	):
		# NVDA Core issue 16009: Windows 11 uses modern keyboard interface to display Suggested Actions
		# such as Skype calls when data such as phone number is copied to the clipboard.
		# Because keyboard interaction is not possible, just report the top suggested action.
		# Resolved in NVDA 2024.2.
		import ui
		if activityId == "Windows.Shell.InputApp.SmartActions.Popup":
			displayString = obj.name
		ui.message(displayString)
