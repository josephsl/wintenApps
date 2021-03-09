# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2017-2021 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for Windows 10 Modern Keyboard aka new touch keyboard panel.
The chief feature is allowing NVDA to announce
selected emoji when using the keyboard to search for and select one.
Another feature is to announce candidates for misspellings if suggestions for hardware keyboard is selected.
This is applicable on Windows 10 Fall Creators Update and later."""

# The add-on version of this module will extend the one that comes with NVDA Core (2018.3 and later).
# Parts come from Microsoft Quick Input support pull request (author: Mick Curran from NV Access)
# For IME candidate item/UI definition, Flake8 must be told to ignore it.

# Help Mypy and other static checkers for a time by importing uppercase versions of built-in types.
from typing import Tuple
# Yes, this app module is powered by built-in modern keyboard app module.
# Argh, line length exceeded.
from nvdaBuiltin.appModules.windowsinternal_composableshell_experiences_textinput_inputapp import *  # NOQA: F403, E501
# Until winVersion.getWinVer function shows up.
import sys
import eventHandler
import UIAHandler
import controlTypes
import config
import api
import speech
import braille
import ui
from NVDAObjects.UIA import UIA


# Built-in modern keyboard app module powers bulk of the below app module class, so inform Mypy.
# And Flake8 and other linters, to.
class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405

	_modernKeyboardInterfaceActive: bool = False
	_symbolsGroupSelected: bool = False

	def event_UIA_elementSelected(self, obj, nextHandler):
		# Ask NVDA to respond to UIA events coming from this overlay.
		# Focus change event will not work, as it'll cause focus to be lost when the panel closes.
		if config.conf["UIA"]["selectiveEventRegistration"]:
			UIAHandler.handler.removeEventHandlerGroup(obj.UIAElement, UIAHandler.handler.localEventHandlerGroup)
			UIAHandler.handler.addEventHandlerGroup(obj.UIAElement, UIAHandler.handler.localEventHandlerGroup)
		# Logic for IME candidate items is handled all within its own object
		# Therefore pass these events straight on.
		if isinstance(obj, ImeCandidateItem):  # NOQA: F405
			return nextHandler()
		# The rest of this event handler isn't applicable in build 20200 and later due to UI redesign.
		# Early builds had accessibility problems, which was improved in build 21000 series.
		if sys.getwindowsversion().build >= 21296:
			return
		# Wait until modern keyboard is fully displayed on screen.
		if sys.getwindowsversion().build >= 17134 and not self._modernKeyboardInterfaceActive:
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
		automationId = obj.UIAAutomationId
		# #7273: When this is fired on categories,
		# the first emoji from the new category is selected but not announced.
		# Therefore, move the navigator object to that item if possible.
		# However, in recent builds, name change event is also fired.
		# For consistent experience, report the new category first by traversing through controls.
		# #8189: do not announce candidates list itself (not items),
		# as this is repeated each time candidate items are selected.
		if (
			automationId == "CandidateList"
			# Also, when changing categories (emoji, kaomoji, symbols) in Version 1903 or later,
			# category items are selected when in fact they have no text labels.
			or obj.parent.UIAAutomationId == "TEMPLATE_PART_Sets_ListView"
			# Specifically to suppress skin tone modifiers from being announced after an emoji group was selected.
			or self._symbolsGroupSelected
			# In Version 1709 and 1803, both categories and items raise element selected event when category changes.
			or obj.name == self._recentlySelected and sys.getwindowsversion().build < 17763
		):
			return
		speech.cancelSpeech()
		# Sometimes, due to bad tree traversal or wrong item getting selected,
		# something other than the selected item sees this event.
		# In build 18262, emoji panel may open to People group and skin tone modifier gets selected.
		# Skin tone modifiers are also selected when switching to People emoji group, and this should be suppressed.
		if obj.parent.UIAAutomationId == "SkinTonePanelModifier_ListView":
			# But this will point to nothing if emoji search results are not people.
			if obj.parent.next is not None:
				obj = obj.parent.next
			else:
				obj = obj.parent.parent.firstChild
		candidate = obj
		if (
			obj and obj.UIAElement.cachedClassName == "ListViewItem"
			and obj.parent and isinstance(obj.parent, UIA)
			and obj.parent.UIAAutomationId != "TEMPLATE_PART_ClipboardItemsList"
		):
			# The difference between emoji panel and suggestions list is absence of categories/emoji separation.
			# Turns out Automation Id for the container is different,
			# observed in build 17666 when opening clipboard copy history.
			candidate = obj.parent.previous
			if candidate is not None:
				# Emoji categories list.
				ui.message(candidate.name)
				obj = candidate.firstChild
		if obj is not None:
			api.setNavigatorObject(obj)
			# NVDA Core issue 10093: for Japanese IME, candidates must be spelled.
			if obj.parent.UIAAutomationId == "IME_Candidate_Window":
				speech.speakSpelling(obj.name, useCharacterDescriptions=True)
			else:
				obj.reportFocus()
			# NVDA Core issue 10371: as part of speech sequence work in 2019.3,
			# braille.getBrailleTextForProperties has been renamed to getPropertiesBraille.
			braille.handler.message(
				braille.getPropertiesBraille(name=obj.name, role=obj.role, positionInfo=obj.positionInfo)
			)
			# Cache selected item.
			self._recentlySelected = obj.name
		else:
			from . import skipTranslation
			skipTranslation.translate("No emoji")
		nextHandler()

	# Emoji panel for build 16299 and 17134.
	_classicEmojiPanelAutomationIds: Tuple[str, ...] = (
		"TEMPLATE_PART_ExpressiveInputFullViewFuntionBarItemControl",
		"TEMPLATE_PART_ExpressiveInputFullViewFuntionBarCloseButton"
	)

	def event_UIA_window_windowOpen(self, obj, nextHandler):
		# Ask NVDA to respond to UIA events coming from modern keyboard interface.
		# Focus change event will not work, as it'll cause focus to be lost when the panel closes.
		firstChild = obj.firstChild
		if config.conf["UIA"]["selectiveEventRegistration"] and obj.firstChild is not None:
			localEventHandlerElements = [firstChild]
			# For dictation, add elements manually so name change event can be handled.
			# Object hierarchy is different in voice typing (build 21296 and later).
			if firstChild.UIAAutomationId in ("DictationMicrophoneButton", "FloatyTip"):
				if firstChild.UIAAutomationId == "DictationMicrophoneButton":
					element = firstChild.next
				else:
					element = firstChild.firstChild.firstChild
				while element.next is not None:
					localEventHandlerElements.append(element)
					element = element.next
			for element in localEventHandlerElements:
				UIAHandler.handler.removeEventHandlerGroup(element.UIAElement, UIAHandler.handler.localEventHandlerGroup)
				UIAHandler.handler.addEventHandlerGroup(element.UIAElement, UIAHandler.handler.localEventHandlerGroup)
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
		# Handle Ime Candidate UI being shown
		if isinstance(firstChild, ImeCandidateUI):  # NOQA: F405
			eventHandler.queueEvent("show", firstChild)
			# Don't forget to add actual candidate item element so name change event can be handled
			# (mostly for hardware keyboard input suggestions).
			if config.conf["UIA"]["selectiveEventRegistration"]:
				UIAHandler.handler.removeEventHandlerGroup(
					firstChild.firstChild.firstChild.UIAElement, UIAHandler.handler.localEventHandlerGroup
				)
				UIAHandler.handler.addEventHandlerGroup(
					firstChild.firstChild.firstChild.UIAElement, UIAHandler.handler.localEventHandlerGroup
				)
			return
		# Build 20200 and later introduced a completely different user interface for modern keyboard.
		# Essentially, emoji panel and clipboard are combined and housed inside a web document interface.
		# As a result, Automation Id's are the same and UIA tree is different (hosted inside an EdgeHTML document),
		# so the rest of this event handler isn't applicable.
		# At least call nextHandler so other objects can respond to window open event.
		if sys.getwindowsversion().build >= 21296:
			return nextHandler()
		childAutomationId = firstChild.UIAAutomationId
		self._modernKeyboardInterfaceActive = True
		self._symbolsGroupSelected = False
		# Emoji panel for build 16299 and 17134.
		# This event is properly raised in build 17134.
		if sys.getwindowsversion().build < 17763 and childAutomationId in self._classicEmojiPanelAutomationIds:
			eventHandler.queueEvent("UIA_elementSelected", obj.lastChild.firstChild)
		# Handle hardware keyboard and CJK IME suggestions.
		# Treat it the same as CJK composition list - don't announce this if candidate announcement setting is off.
		# In fact, in 20H1, this is the CJK IME candidates window.
		elif (
			childAutomationId in ("CandidateWindowControl", "IME_Candidate_Window", "IME_Prediction_Window")
			and config.conf["inputComposition"]["autoReportAllCandidates"]
		):
			try:
				eventHandler.queueEvent("UIA_elementSelected", firstChild.firstChild.firstChild)
			except AttributeError:
				# Because this is dictation window.
				pass
		# Emoji panel in build 17666 and later (unless this changes).
		elif childAutomationId == "TEMPLATE_PART_ExpressionGroupedFullView":
			# On some systems (particularly non-English builds of Version 1903 and later),
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
		nextHandler()

	def event_nameChange(self, obj, nextHandler):
		# Logic for IME candidate items is handled all within its own object
		# Therefore pass these events straight on.
		if isinstance(obj, ImeCandidateItem):  # NOQA: F405
			return nextHandler()
		elif isinstance(obj, ImeCandidateUI):  # NOQA: F405
			return nextHandler()
		automationId = obj.UIAAutomationId
		# Forget it if there is no Automation Id and class name set.
		if (
			(obj.UIAElement.cachedClassName == "" and automationId == "")
			# Clipboard entries fire name change event when opened.
			or (obj.UIAElement.cachedClassName == "TextBlock" and automationId == "")
		):
			return
		# On some systems, touch keyboard keys keeps firing name change event.
		# In build 17704, whenever skin tones are selected, name change is fired by emoji entries (GridViewItem).
		if (
			(obj.UIAElement.cachedClassName in ("CRootKey", "GridViewItem"))
			# Just ignore useless clipboard status and vertical scroll bar label.
			# Also top emoji search result must be announced for better user experience.
			or (automationId in (
				"TEMPLATE_PART_ClipboardItemsList", "TEMPLATE_PART_Search_TextBlock", "VerticalScrollBar"
			))
			# And no, emoji entries should not be announced here.
			or (self._recentlySelected is not None and self._recentlySelected in obj.name)
		):
			return
		# The word "blank" is kept announced, so suppress this on build 17666 and later.
		if sys.getwindowsversion().build >= 17763:
			# In build 17672 and later,
			# return immediately when element selected event on clipboard item was fired just prior to this.
			# In some cases, parent will be None, as seen when emoji panel is closed in build 18267.
			try:
				if (
					automationId == "TEMPLATE_PART_ClipboardItemIndex"
					or obj.parent.UIAAutomationId == "TEMPLATE_PART_ClipboardItemsList"
				):
					return
			except AttributeError:
				return
			if (
				not self._modernKeyboardInterfaceActive
				or automationId != "TEMPLATE_PART_ExpressionGroupedFullView"
			):
				speech.cancelSpeech()
		# Don't forget to add "Microsoft Candidate UI" as something that should be suppressed.
		if automationId not in (
			"TEMPLATE_PART_ExpressionFullViewItemsGrid",
			"TEMPLATE_PART_ClipboardItemIndex",
			"CandidateWindowControl"
		):
			ui.message(obj.name)
		self._symbolsGroupSelected = False
		if not any(obj.location):
			self._modernKeyboardInterfaceActive = False
			self._recentlySelected = None
		nextHandler()

	def event_stateChange(self, obj, nextHandler):
		# Do not clear symbols group selected flag if an emoji group item is still the navigator object.
		parent = api.getNavigatorObject().parent
		if isinstance(parent, UIA) and parent.UIAAutomationId != "TEMPLATE_PART_Groups_ListView":
			self._symbolsGroupSelected = False
		# Try detecting if modern keyboard elements are off-screen or the window itself is gone
		# (parent's first child is nothing).
		# But attempting to retrieve obj location fails when emoji panel closes without selecting anything,
		# especially in Version 1903 and later.
		# Because of exceptions, check location first.
		if (
			(obj.location is None and obj.parent.firstChild is None and sys.getwindowsversion().build >= 18362)
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
		# Announce input experience panel items (emoji/clipboard) in build 21296 and later.
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
