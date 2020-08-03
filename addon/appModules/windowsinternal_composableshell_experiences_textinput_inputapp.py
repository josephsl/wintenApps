# App module for Composable Shell (CShell) input panel
# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2017-2020 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for Windows 10 Modern Keyboard aka new touch keyboard panel.
The chief feature is allowing NVDA to announce selected emoji when using the keyboard to search for and select one.
Another feature is to announce candidates for misspellings if suggestions for hardware keyboard is selected.
This is applicable on Windows 10 Fall Creators Update and later."""

# The add-on version of this module will extend the one that comes with NVDA Core (2018.3 and later).

from nvdaBuiltin.appModules.windowsinternal_composableshell_experiences_textinput_inputapp import *
import eventHandler


class AppModule(AppModule):

	_symbolsGroupSelected = False
	_searchInProgress = False

	def event_UIA_elementSelected(self, obj, nextHandler):
		# Ask NvDA to respond to UIA events coming from this overlay.
		# Focus change event will not work, as it'll cause focus to be lost when the panel closes.
		import UIAHandler
		if hasattr(UIAHandler.handler, "addEventHandlerGroup") and config.conf["UIA"]["selectiveEventRegistration"]:
			UIAHandler.handler.removeEventHandlerGroup(obj.UIAElement, UIAHandler.handler.localEventHandlerGroup)
			UIAHandler.handler.addEventHandlerGroup(obj.UIAElement, UIAHandler.handler.localEventHandlerGroup)
		# Wait until modern keyboard is fully displayed on screen.
		# Force this flag on if search is in progress.
		if self._searchInProgress: self._emojiPanelJustOpened = True
		if winVersion.isWin10(version=1803) and not self._emojiPanelJustOpened: return
		# If emoji/kaomoji/symbols group item gets selected, just tell NVDA to treat it as the new navigator object (for presentational purposes) and move on.
		if obj.parent.UIAElement.cachedAutomationID == "TEMPLATE_PART_Groups_ListView":
			if obj._getUIACacheablePropertyValue(UIAHandler.UIA_PositionInSetPropertyId) == 1:
				self._searchInProgress = True
			else:
				# Symbols group flag must be set if and only if emoji panel is active, as UIA item selected event is fired just before emoji panel opens when opening the panel after closing it for a while.
				api.setNavigatorObject(obj)
				if self._emojiPanelJustOpened: 
					self._symbolsGroupSelected = True
			return
		automationID = obj._getUIACacheablePropertyValue(UIAHandler.UIA_AutomationIdPropertyId)
		# #7273: When this is fired on categories, the first emoji from the new category is selected but not announced.
		# Therefore, move the navigator object to that item if possible.
		# However, in recent builds, name change event is also fired.
		# For consistent experience, report the new category first by traversing through controls.
		# #8189: do not announce candidates list itself (not items), as this is repeated each time candidate items are selected.
		if (
			automationID == "CandidateList"
			# Also, when changing categories (emoji, kaomoji, symbols) in Version 1903 or later, category items are selected when in fact they have no text labels.
			or obj.parent.UIAElement.cachedAutomationID == "TEMPLATE_PART_Sets_ListView"
			# Specifically to suppress skin tone modifiers from being announced after an emoji group was selected.
			or self._symbolsGroupSelected
			# In Version 1709 and 1803, both categories and items raise element selected event when category changes.
			or obj.name == self._recentlySelected and not winVersion.isWin10(version=1809)
		):
			return
		speech.cancelSpeech()
		# Sometimes, due to bad tree traversal or wrong item getting selected, something other than the selected item sees this event.
		# Sometimes clipboard candidates list gets selected, so ask NvDA to descend one more level.
		if automationID == "TEMPLATE_PART_ClipboardItemsList":
			obj = obj.firstChild
		# In build 18262, emoji panel may open to People group and skin tone modifier or the list housing them gets selected.
		# Skin tone modifiers are also selected when switching to People emoji group, and this should be suppressed.
		elif automationID == "SkinTonePanelModifier_ListView":
			obj = obj.next
		elif obj.parent.UIAElement.cachedAutomationID == "SkinTonePanelModifier_ListView":
			# But this will point to nothing if emoji search results are not people.
			if obj.parent.next is not None: obj = obj.parent.next
			else: obj = obj.parent.parent.firstChild
		candidate = obj
		if obj and obj.UIAElement.cachedClassName == "ListViewItem" and obj.parent and isinstance(obj.parent, UIA) and obj.parent.UIAElement.cachedAutomationID != "TEMPLATE_PART_ClipboardItemsList":
			# The difference between emoji panel and suggestions list is absence of categories/emoji separation.
			# Turns out automation ID for the container is different, observed in build 17666 when opening clipboard copy history.
			candidate = obj.parent.previous
			if candidate is not None:
				# Emoji categories list.
				ui.message(candidate.name)
				obj = candidate.firstChild
		if obj is not None:
			api.setNavigatorObject(obj)
			# NvDA Core issue 10093: for Japanese IME, candidates must be spelled.
			if obj.parent.UIAElement.cachedAutomationID == "IME_Candidate_Window": speech.speakSpelling(obj.name, useCharacterDescriptions=True)
			else: obj.reportFocus()
			# NVDA Core issue 10371: as part of speech sequence work in 2019.3, braille.getBrailleTextForProperties has been renamed to getPropertiesBraille.
			braille.handler.message(braille.getPropertiesBraille(name=obj.name, role=obj.role, positionInfo=obj.positionInfo))
			# Cache selected item.
			self._recentlySelected = obj.name
		else:
			from . import skipTranslation
			skipTranslation.translate("No emoji")
		nextHandler()

	# Emoji panel for build 16299 and 17134.
	_classicEmojiPanelAutomationID = ("TEMPLATE_PART_ExpressiveInputFullViewFuntionBarItemControl", "TEMPLATE_PART_ExpressiveInputFullViewFuntionBarCloseButton")

	def event_UIA_window_windowOpen(self, obj, nextHandler):
		# Make sure to announce most recently used emoji first in post-1709 builds.
		# Fake the announcement by locating 'most recently used" category and calling selected event on this.
		# However, in build 17666 and later, child count is the same for both emoji panel and hardware keyboard candidates list.
		# Thankfully first child automation ID's are different for each modern input technology.
		# However this event is raised when the input panel closes.
		inputPanel = obj.firstChild
		if inputPanel is None:
			self._symbolsGroupSelected = False
			self._emojiPanelJustOpened = False
			self._recentlySelected = None
			return
		inputPanelAutomationID = inputPanel.UIAElement.cachedAutomationID
		self._emojiPanelJustOpened = True
		self._symbolsGroupSelected = False
		# Emoji panel for build 16299 and 17134.
		# This event is properly raised in build 17134.
		if not winVersion.isWin10(version=1809) and inputPanelAutomationID in self._classicEmojiPanelAutomationID:
			eventHandler.executeEvent("UIA_elementSelected", obj.lastChild.firstChild)
		# Handle hardware keyboard and CJK IME suggestions.
		# Treat it the same as CJK composition list - don't announce this if candidate announcement setting is off.
		# In fact, in 20H1, this is the CJK IME candidates window.
		elif inputPanelAutomationID in ("CandidateWindowControl", "IME_Candidate_Window", "IME_Prediction_Window") and config.conf["inputComposition"]["autoReportAllCandidates"]:
			try:
				eventHandler.executeEvent("UIA_elementSelected", inputPanel.firstChild.firstChild)
			except AttributeError:
				# Because this is dictation window.
				pass
		# Emoji panel in build 17666 and later (unless this changes).
		elif inputPanelAutomationID == "TEMPLATE_PART_ExpressionGroupedFullView":
			# Ask NvDA to respond to UIA events coming from this overlay.
			# Focus change event will not work, as it'll cause focus to be lost when the panel closes.
			import UIAHandler
			if hasattr(UIAHandler.handler, "addEventHandlerGroup") and config.conf["UIA"]["selectiveEventRegistration"]:
				UIAHandler.handler.removeEventHandlerGroup(inputPanel.UIAElement, UIAHandler.handler.localEventHandlerGroup)
				UIAHandler.handler.addEventHandlerGroup(inputPanel.UIAElement, UIAHandler.handler.localEventHandlerGroup)
			# On some systems, there is something else besides grouping controls, so another child control must be used.
			emojisList = inputPanel.children[-2]
			if emojisList.UIAElement.cachedAutomationID != "TEMPLATE_PART_Items_GridView":
				emojisList = emojisList.previous
			try:
				eventHandler.executeEvent("UIA_elementSelected", emojisList.firstChild.firstChild)
			except AttributeError:
				# In build 18272's emoji panel, emoji list becomes empty in some situations.
				pass
		# Clipboard history.
		# Move to clipboard list so element selected event can pick it up.
		elif inputPanelAutomationID == "TEMPLATE_PART_ClipboardTitleBar":
			# Under some cases, clipboard tip text isn't shown on screen, causing clipboard history title to be announced instead of most recently copied item.
			clipboardHistory = obj.children[-2]
			if clipboardHistory.UIAElement.cachedAutomationID == inputPanelAutomationID:
				clipboardHistory = clipboardHistory.next
			eventHandler.executeEvent("UIA_elementSelected", clipboardHistory)
		nextHandler()

	def event_nameChange(self, obj, nextHandler):
		# In build 18975, CJK IME candidates fire name change event.
		if obj.UIAElement.cachedClassName == "ListViewItem": return
		try:
			cachedAutomationID = obj.UIAElement.cachedAutomationID
		except:
			cachedAutomationID = ""
		# On some systems, touch keyboard keys keeps firing name change event.
		# In build 17704, whenever skin tones are selected, name change is fired by emoji entries (GridViewItem).
		if ((obj.UIAElement.cachedClassName in ("CRootKey", "GridViewItem"))
		# Just ignore useless clipboard status and vertical scroll bar label.
		# Also top emoji search result must be announced for better user experience.
		or (cachedAutomationID in ("TEMPLATE_PART_ClipboardItemsList", "TEMPLATE_PART_Search_TextBlock", "VerticalScrollBar"))
		# And no, emoji entries should not be announced here.
		or (self._recentlySelected is not None and self._recentlySelected in obj.name)):
			return
		# The word "blank" is kept announced, so suppress this on build 17666 and later.
		if winVersion.winVersion.build > 17134:
			# In build 17672 and later, return immediatley when element selected event on clipboard item was fired just prior to this.
			# In some cases, parent will be None, as seen when emoji panel is closed in build 18267.
			try:
				if cachedAutomationID == "TEMPLATE_PART_ClipboardItemIndex" or obj.parent.UIAElement.cachedAutomationID == "TEMPLATE_PART_ClipboardItemsList": return
			except AttributeError:
				return
			if not self._emojiPanelJustOpened or cachedAutomationID != "TEMPLATE_PART_ExpressionGroupedFullView": speech.cancelSpeech()
		# Don't forget to add "Microsoft Candidate UI" as something that should be suppressed.
		if cachedAutomationID not in ("TEMPLATE_PART_ExpressionFullViewItemsGrid", "TEMPLATE_PART_ClipboardItemIndex", "CandidateWindowControl"):
			ui.message(obj.name)
		self._symbolsGroupSelected = False
		if obj.location == (0, 0, 0, 0):
			self._emojiPanelJustOpened = False
			self._symbolsGroupSelected = False
			self._recentlySelected = None
			self._searchInProgress = False
		nextHandler()

	def event_stateChange(self, obj, nextHandler):
		# Attempting to retrieve object location fails when emoji panel closes without selecting anything, especially in Version 1903 and later.
		if obj.location is None and winVersion.isWin10(version=1903):
			self._symbolsGroupSelected = False
			self._emojiPanelJustOpened = False
			self._recentlySelected = None
		nextHandler()
