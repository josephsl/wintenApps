# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2017-2021 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for modern keyboard aka new touch keyboard panel.
The chief feature is allowing NVDA to announce
selected emoji when using the keyboard to search for and select one.
Another feature is to announce candidates for misspellings if suggestions for hardware keyboard is selected.
This is applicable on Windows 10 1709 (Fall Creators Update) and later."""

# The add-on version of this module will extend the one that comes with NVDA Core (2018.3 and later).
# For IME candidate item/UI definition, Flake8 must be told to ignore it.

# Yes, this app module is powered by built-in modern keyboard (TextInputHost) app module
# (formerly WindowsInternal.ComposableShell.Experiences.TextInput.InputApp).
from nvdaBuiltin.appModules.textinputhost import *  # NOQA: F403
import winVersion
import eventHandler
import UIAHandler
import controlTypes
import api
import scriptHandler
import speech
import ui
from logHandler import log
from NVDAObjects.UIA import UIA


# Temporary: detect Windows 11.
# Use build 22000 as cut-off build.
WIN11 = winVersion.WinVersion(major=10, minor=0, build=22000)


# Built-in modern keyboard app module powers bulk of the below app module class, so inform Mypy.
# And Flake8 and other linters, to.
class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405

	_modernKeyboardInterfaceActive: bool = False
	_symbolsGroupSelected: bool = False

	def event_UIA_elementSelected(self, obj, nextHandler):
		# Ask NVDA to respond to UIA events coming from this overlay.
		# Focus change event will not work, as it'll cause focus to be lost when the panel closes.
		try:
			UIAHandler.handler.removeEventHandlerGroup(obj.UIAElement, UIAHandler.handler.localEventHandlerGroup)
			UIAHandler.handler.addEventHandlerGroup(obj.UIAElement, UIAHandler.handler.localEventHandlerGroup)
		except NotImplementedError:
			pass
		# Logic for IME candidate items is handled all within its own object
		# Therefore pass these events straight on.
		if isinstance(obj, ImeCandidateItem):  # NOQA: F405
			return nextHandler()
		# The rest of this event handler isn't applicable in Windows 11 due to UI redesign.
		# Early builds had accessibility problems, which was improved in build 21000 series.
		if winVersion.getWinVer() >= WIN11:
			return
		# Wait until modern keyboard is fully displayed on screen.
		# Windows 10 1803 or later
		if not self._modernKeyboardInterfaceActive:
			return
		# If emoji/kaomoji/symbols group item gets selected, just tell NVDA to treat it as the new navigator object
		# (for presentational purposes) and move on.
		if obj.parent.UIAAutomationId == "TEMPLATE_PART_Groups_ListView":
			api.setNavigatorObject(obj)
			if obj.positionInfo["indexInGroup"] != 1:
				# Symbols group flag must be set if and only if emoji panel is active,
				# as UIA item selected event is fired just before emoji panel opens
				# when opening the panel after closing it for a while.
				self._symbolsGroupSelected = True
			return
		if (
			# When changing categories (emoji, kaomoji, symbols) in Windows 10 1903 or later,
			# category items are selected when in fact they have no text labels.
			obj.parent.UIAAutomationId == "TEMPLATE_PART_Sets_ListView"
			# Specifically to suppress skin tone modifiers from being announced after an emoji group was selected.
			or self._symbolsGroupSelected
		):
			return
		# NVDA Core takes care of the rest.
		super(AppModule, self).event_UIA_elementSelected(obj, nextHandler)

	# Register modern keyboard interface elements with local event handler group.
	def _windowOpenEventInternalEventHandlerGroupRegistration(self, firstChild):
		# Gather elements to be registered inside a list so they can be registered in one go.
		localEventHandlerElements = [firstChild]
		# For dictation, add elements manually so name change event can be handled.
		# Object hierarchy is different in voice typing (Windows 11).
		if firstChild.UIAAutomationId in ("DictationMicrophoneButton", "FloatyTip"):
			if firstChild.UIAAutomationId == "DictationMicrophoneButton":
				element = firstChild.next
			else:
				element = firstChild.firstChild.firstChild
			while element.next is not None:
				localEventHandlerElements.append(element)
				element = element.next
		# Don't forget to add actual candidate item element so name change event can be handled
		# (mostly for hardware keyboard input suggestions).
		if isinstance(firstChild, ImeCandidateUI):  # NOQA: F405
			imeCandidateItem = firstChild.firstChild.firstChild
			# In Windows 11, an extra element is located between candidate UI window and items themselves.
			if winVersion.getWinVer() >= WIN11:
				# For some odd reason, suggested text is the last element.
				imeCandidateItem = imeCandidateItem.lastChild
			localEventHandlerElements.append(imeCandidateItem)
		for element in localEventHandlerElements:
			UIAHandler.handler.removeEventHandlerGroup(element.UIAElement, UIAHandler.handler.localEventHandlerGroup)
			UIAHandler.handler.addEventHandlerGroup(element.UIAElement, UIAHandler.handler.localEventHandlerGroup)

	def event_UIA_window_windowOpen(self, obj, nextHandler):
		# Ask NVDA to respond to UIA events coming from modern keyboard interface.
		# Focus change event will not work, as it'll cause focus to be lost when the panel closes.
		firstChild = obj.firstChild
		# Make sure to announce most recently used emoji first in post-1709 builds.
		# Fake the announcement by locating 'most recently used" category and calling selected event on this.
		# However, in build 17666 and later,
		# child count is the same for both emoji panel and hardware keyboard candidates list.
		# Thankfully first child Automation Id's are different for each modern input technology.
		# However this event is raised when the input panel closes.
		if firstChild is None:
			self._modernKeyboardInterfaceActive = False
			self._recentlySelected = None
			return
		# Log which modern keyboard header is active.
		if log.isEnabledFor(log.DEBUG):
			log.debug(
				"W10: Automation Id for currently opened modern keyboard feature "
				f"is {firstChild.UIAAutomationId}"
			)
		# Originally part of this method, split into an internal function to reduce complexity.
		try:
			self._windowOpenEventInternalEventHandlerGroupRegistration(firstChild)
		except NotImplementedError:
			pass
		# Handle Ime Candidate UI being shown
		if isinstance(firstChild, ImeCandidateUI):  # NOQA: F405
			eventHandler.queueEvent("show", firstChild)
			return
		childAutomationId = firstChild.UIAAutomationId
		self._modernKeyboardInterfaceActive = True
		self._symbolsGroupSelected = False
		# Emoji panel in build 17666 and later (unless this changes).
		if childAutomationId == "TEMPLATE_PART_ExpressionGroupedFullView":
			self._emojiPanelJustOpened = True
			# On some systems (particularly non-English builds of Windows 10 1903 and later),
			# there is something else besides grouping controls, so another child control must be used.
			emojisList = firstChild.children[-2]
			if emojisList.UIAAutomationId != "TEMPLATE_PART_Items_GridView":
				emojisList = emojisList.previous
			if emojisList.firstChild and emojisList.firstChild.firstChild:
				emojiItem = emojisList.firstChild.firstChild
			# Avoid announcing skin tone modifiers if possible.
			# For people emoji, the first emoji is actually next to skin tone modifiers list.
			if emojiItem.UIAAutomationId == "SkinTonePanelModifier_ListView" and emojiItem.next:
				emojiItem = emojiItem.next
			eventHandler.queueEvent("UIA_elementSelected", emojiItem)
			return
		# Clipboard history.
		# Move to clipboard list so element selected event can pick it up.
		elif childAutomationId == "TEMPLATE_PART_ClipboardTitleBar":
			# Under some cases, clipboard tip text isn't shown on screen,
			# causing clipboard history title to be announced instead of most recently copied item.
			clipboardHistoryItem = obj.children[-2]
			if clipboardHistoryItem.UIAAutomationId == childAutomationId:
				clipboardHistoryItem = clipboardHistoryItem.next
			# Make sure to move to actual clipboard history item if available.
			if clipboardHistoryItem.firstChild is not None:
				clipboardHistoryItem = clipboardHistoryItem.firstChild
			eventHandler.queueEvent("UIA_elementSelected", clipboardHistoryItem)
			return
		# Combined emoji panel and clipboard history.
		# Windows 11 introduced a completely different user interface for modern keyboard.
		# Essentially, emoji panel and clipboard are combined and housed inside a web document interface.
		# As a result, Automation Id's are the same and UIA tree is different (hosted inside an EdgeHTML document).
		# Move NVDA's focus to input experience panel so arrow keys can be used to navigate among emojis.
		elif childAutomationId == "Windows.Shell.InputApp.FloatingSuggestionUI":
			api.setFocusObject(obj)
			return
		# NVDA Core takes care of the rest.
		super(AppModule, self).event_UIA_window_windowOpen(obj, nextHandler)

	def event_nameChange(self, obj, nextHandler):
		# Logic for IME candidate items is handled all within its own object
		# Therefore pass these events straight on.
		if isinstance(obj, ImeCandidateItem):  # NOQA: F405
			return nextHandler()
		elif isinstance(obj, ImeCandidateUI):  # NOQA: F405
			return nextHandler()
		# Forget it if there is no Automation Id and class name set.
		if (
			(obj.UIAElement.cachedClassName == "" and obj.UIAAutomationId == "")
			# Clipboard entries fire name change event when opened.
			or (obj.UIAElement.cachedClassName == "TextBlock" and obj.UIAAutomationId == "")
			# Ignore useless clipboard entry scrolling announcements.
			or obj.UIAAutomationId == "VerticalScrollBar"
		):
			return
		# NVDA Core takes care of the rest.
		super(AppModule, self).event_nameChange(obj, nextHandler)
		# Back on add-on version.
		self._symbolsGroupSelected = False
		if not any(obj.location):
			self._modernKeyboardInterfaceActive = False
			self._recentlySelected = None

	def event_stateChange(self, obj, nextHandler):
		# Do not clear symbols group selected flag if an emoji group item is still the navigator object.
		parent = api.getNavigatorObject().parent
		if isinstance(parent, UIA) and parent.UIAAutomationId != "TEMPLATE_PART_Groups_ListView":
			self._symbolsGroupSelected = False
		# Try detecting if modern keyboard elements are off-screen or the window itself is gone
		# (parent's first child is nothing).
		# But attempting to retrieve obj location fails when emoji panel closes without selecting anything,
		# especially in Windows 10 1903 and later.
		# Because of exceptions, check location first.
		# Windows 10 1903 or later.
		if (
			(obj.location is None and obj.parent.firstChild is None)
			or controlTypes.STATE_OFFSCREEN in obj.states
		):
			self._modernKeyboardInterfaceActive = False
			self._recentlySelected = None
		nextHandler()

	def event_UIA_notification(
			self, obj, nextHandler,
			notificationProcessing=UIAHandler.NotificationProcessing_CurrentThenMostRecent,
			displayString=None, activityId=None, **kwargs
	):
		# Announce input experience panel items (emoji/clipboard) in Windows 11.
		# Note that input experience panel is not really a focusable window - it is an overlay.
		# Filter out extraneous notifications such as those raised by root document window
		# (after all, input experience panel (at least emoji panel and clipboard history) is a web document).
		if activityId == "Windows.Shell.InputApp.SuggestionUI.DocumentTitle":
			return
		# Try emulating default UIA notification event handler for UIA objects.
		if notificationProcessing in (
			UIAHandler.NotificationProcessing_ImportantMostRecent, UIAHandler.NotificationProcessing_MostRecent
		):
			speech.cancelSpeech()
		ui.message(displayString)
		nextHandler()

	def event_gainFocus(self, obj, nextHandler):
		# Input experience panel is focused when trying to close it, so move focus to somewhere else.
		if obj.parent.childCount == 0:
			objectWithFocus = obj.objectWithFocus()
			eventHandler.queueEvent("gainFocus", objectWithFocus)
		nextHandler()

	@scriptHandler.script(gesture="kb:escape")
	def script_closeInputExperiencePanel(self, gesture):
		# In Windows 11, pressing Escape moves focus to input experience panel.
		# Therefore tell NVDA to move focus to system focus.
		# Focus redirect is applicable for emoji panel and clipboard history.
		gesture.send()
		if winVersion.getWinVer() >= WIN11:
			objectWithFocus = api.getFocusObject().objectWithFocus()
			eventHandler.queueEvent("gainFocus", objectWithFocus)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Recognize more candidate UI and item elements in Windows 11.
		if isinstance(obj, UIA):
			# Candidate item.
			if obj.role == controlTypes.ROLE_LISTITEM and obj.parent.UIAAutomationId == "TEMPLATE_PART_CandidatePanel":
				clsList.insert(0, ImeCandidateItem)  # NOQA: F405
			# Candidate UI.
			elif (
				obj.role in (controlTypes.ROLE_LIST, controlTypes.ROLE_POPUPMENU)
				and obj.UIAAutomationId in ("TEMPLATE_PART_CandidatePanel", "IME_Prediction_Window")
			):
				clsList.insert(0, ImeCandidateUI)
			return
		# NVDA Core takes care of the rest.
		super(AppModule, self).chooseNVDAObjectOverlayClasses(obj, clsList)
