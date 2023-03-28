# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2017-2023 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# The add-on version of this module will extend the one that comes with NVDA Core (2018.3 and later).
# For IME candidate item/UI definition, Flake8 must be told to ignore it.

from typing import List, Callable
# Yes, this app module is powered by built-in modern keyboard (TextInputHost) app module
# (formerly WindowsInternal.ComposableShell.Experiences.TextInput.InputApp).
# #70: NVDA Core pull requests are made using the core app module, not alias modules.
from nvdaBuiltin.appModules.windowsinternal_composableshell_experiences_textinput_inputapp import (
	AppModule, ImeCandidateItem, ImeCandidateUI
)
import winVersion
import eventHandler
import UIAHandler
import controlTypes
import api
from logHandler import log
from NVDAObjects.UIA import UIA
from NVDAObjects import NVDAObject


# Bulk of the below class comes from NVDA Core.
class ImeCandidateItem(ImeCandidateItem):  # type: ignore[no-redef]

	def event_UIA_elementSelected(self) -> None:
		# Focus event is fired when a candidate item receives focus, therefore ignore this event.
		if winVersion.getWinVer() >= winVersion.WIN11:
			return
		super().event_UIA_elementSelected()


# Built-in modern keyboard app module powers bulk of the below app module class, so inform Mypy.
class AppModule(AppModule):  # type: ignore[no-redef]

	# In Windows 11, clipboard history is seen as a web document.
	# Turn off browse mode by default so clipboard history entry menu items can be announced when tabbed to.
	# Resolved in NVDA 2023.1.
	disableBrowseModeByDefault = True

	def _emojiPanelClosed(self, obj: NVDAObject):
		# Move NVDA's focus object to what is actually focused on screen.
		# This is needed in Windows 11 when emoji panel closes.
		eventHandler.queueEvent("gainFocus", obj.objectWithFocus())

	def event_UIA_elementSelected(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		automationId = obj.UIAAutomationId
		# Do not proceed if emoji panel category item is selected when the panel itself is gone.
		# This is the case when closing emoji panel portion in Windows 11.
		if automationId.startswith("navigation-menu-item"):
			emojiPanelAncestors = [
				item.appModule for item in api.getFocusAncestors()
				if item.appModule == self
			]
			# Focus object location can be None sometimes.
			focusLocation = api.getFocusObject().location
			# System focus restored.
			if not len(emojiPanelAncestors):
				return
			# NVDA is stuck in a nonexistent edit field.
			elif focusLocation is not None and not any(focusLocation):
				self._emojiPanelClosed(obj)
				return
		# In Windows 11, candidate panel houses candidate items, not the prediction window.
		if automationId == "TEMPLATE_PART_CandidatePanel":
			obj = obj.firstChild
		# NVDA Core takes care of the rest.
		super().event_UIA_elementSelected(obj, nextHandler)

	# Register modern keyboard interface elements with local event handler group.
	def _windowOpenEventInternalEventHandlerGroupRegistration(self, firstChild: NVDAObject):
		# Gather elements to be registered inside a list so they can be registered in one go.
		localEventHandlerElements = [firstChild]
		firstChildAutomationId = firstChild.UIAAutomationId
		# For dictation, add elements manually so name change event can be handled.
		# Object hierarchy is different in voice typing (Windows 11).
		if firstChildAutomationId in ("DictationMicrophoneButton", "FloatyTip"):
			if firstChildAutomationId == "DictationMicrophoneButton":
				element = firstChild.next
			else:
				element = firstChild.firstChild.firstChild
			while element.next is not None:
				localEventHandlerElements.append(element)
				element = element.next
		# Don't forget to add actual candidate item element so name change event can be handled
		# (mostly for hardware keyboard input suggestions).
		if isinstance(firstChild, ImeCandidateUI):
			imeCandidateItem = firstChild.firstChild.firstChild
			# In Windows 11, an extra element is located between candidate UI window and items themselves.
			if winVersion.getWinVer() >= winVersion.WIN11:
				# For some odd reason, suggested text is the last element.
				imeCandidateItem = imeCandidateItem.lastChild
			localEventHandlerElements.append(imeCandidateItem)
		for element in localEventHandlerElements:
			UIAHandler.handler.removeEventHandlerGroup(element.UIAElement, UIAHandler.handler.localEventHandlerGroup)
			UIAHandler.handler.addEventHandlerGroup(element.UIAElement, UIAHandler.handler.localEventHandlerGroup)

	def event_UIA_window_windowOpen(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# Ask NVDA to respond to UIA events coming from modern keyboard interface.
		# Focus change event will not work, as it'll cause focus to be lost when the panel closes.
		# This is more so on Windows 10.
		firstChild = obj.firstChild
		# Sometimes window open event is raised when the input panel closes.
		if firstChild is None:
			return
		firstChildAutomationId = firstChild.UIAAutomationId
		# Log which modern keyboard header is active.
		if log.isEnabledFor(log.DEBUG):
			log.debug(
				"winapps: Automation Id for currently opened modern keyboard feature "
				f"is {firstChildAutomationId}"
			)
		# Originally part of this method, split into an internal function to reduce complexity.
		# However, in Windows 11, combined emoji panel and clipboard history moves system focus to itself.
		# Therefore there is no need to add UIA elements to local event handler group.
		try:
			if firstChildAutomationId != "Windows.Shell.InputApp.FloatingSuggestionUI":
				self._windowOpenEventInternalEventHandlerGroupRegistration(firstChild)
		except NotImplementedError:
			pass
		# Windows 11 22H2 Moment 1 (October 2022) and later uses modern keyboard interface to display
		# Suggested Actions such as Skype calls if data such as phone number is copied to the clipboard.
		# Because keyboard interaction is not possible, just report suggested actions.
		if (
			firstChildAutomationId == "Windows.Shell.InputApp.SmartActionsUX"
			and winVersion.getWinVer() >= winVersion.WIN11_22H2
		):
			import ui
			suggestedActions = [
				suggestedAction.name for suggestedAction in firstChild.children if suggestedAction.name
			]
			ui.message("; ".join(suggestedActions))
		# NVDA Core takes care of the rest.
		super().event_UIA_window_windowOpen(obj, nextHandler)

	def event_gainFocus(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# Focus gets stuck in Modern keyboard when clipboard history closes in Windows 11.
		if obj.parent.childCount == 0:
			self._emojiPanelClosed(obj)
		nextHandler()

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: List[NVDAObject]) -> None:
		# Recognize more candidate UI and item elements in Windows 11.
		# Return after checking each item so candidate UI and items from Windows 10 can be recognized.
		if isinstance(obj, UIA):
			role = obj.role
			# Candidate item.
			if role == controlTypes.Role.LISTITEM and obj.parent.UIAAutomationId == "TEMPLATE_PART_CandidatePanel":
				clsList.insert(0, ImeCandidateItem)
				return
			# Candidate UI.
			elif (
				role in (controlTypes.Role.LIST, controlTypes.Role.POPUPMENU)
				and obj.UIAAutomationId in ("TEMPLATE_PART_CandidatePanel", "IME_Prediction_Window")
			):
				clsList.insert(0, ImeCandidateUI)
				return
		# NVDA Core takes care of the rest.
		super().chooseNVDAObjectOverlayClasses(obj, clsList)
