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
# Parts come from Microsoft Quick Input support pull request (author: Mick Curran from NV Access)

from nvdaBuiltin.appModules.windowsinternal_composableshell_experiences_textinput_inputapp import *
import eventHandler
import controlTypes
from comtypes import COMError
from NVDAObjects.behaviors import CandidateItem as CandidateItemBehavior


class ImeCandidateUI(UIA):
	"""
	The UIAutomation-based IME candidate UI (such as for  the modern Chinese Microsoft Quick input).
	This class ensures NVDA is notified of the first selected item when the UI is shown.
	"""

	def event_show(self):
		# The IME candidate UI is shown.
		# Report the current candidates page and the currently selected item.
		# Sometimes UIA does not fire an elementSelected event when it is first opened,
		# Therefore we must fake it here.
		if (self.UIAElement.cachedAutomationId == "IME_Prediction_Window"):
			candidateItem = self.firstChild
			eventHandler.queueEvent("UIA_elementSelected", candidateItem)
		elif (
			self.firstChild
			and self.firstChild.role == controlTypes.ROLE_LIST
			and isinstance(self.firstChild.firstChild, ImeCandidateItem)
		):
			candidateItem = self.firstChild.firstChild
			eventHandler.queueEvent("UIA_elementSelected", candidateItem)


class ImeCandidateItem(CandidateItemBehavior, UIA):
	"""
	A UIAutomation-based IME candidate Item (such as for  the modern Chinese Microsoft Quick input).
	This class  presents Ime candidate items in the standard way NVDA does for all other IMEs.
	E.g. reports entire candidate page content if it is new or has changed pages,
	And reports the currently selected item, including symbol descriptions.
	"""

	keyboardShortcut = ""

	def _get_candidateNumber(self):
		number = super(ImeCandidateItem, self).keyboardShortcut
		try:
			number = int(number)
		except (ValueError, TypeError):
			pass
		return number

	def _get_parent(self):
		parent = super(ImeCandidateItem, self).parent
		# Translators: A label for a 'candidate' list
		# which contains symbols the user can choose from  when typing east-asian characters into a document.
		parent.name = _("Candidate")
		parent.description = None
		return parent

	def _get_name(self):
		try:
			number = int(self.candidateNumber)
		except (TypeError, ValueError):
			return super(ImeCandidateItem, self).name
		candidate = super(ImeCandidateItem, self).name
		return self.getFormattedCandidateName(number, candidate)

	def _get_description(self):
		candidate = super(ImeCandidateItem, self).name
		return self.getFormattedCandidateDescription(candidate)

	def _get_basicText(self):
		return super(ImeCandidateItem, self).name

	def event_UIA_elementSelected(self):
		oldNav = api.getNavigatorObject()
		if isinstance(oldNav, ImeCandidateItem) and self.name == oldNav.name:
			# Duplicate selection event fired on the candidate item. Ignore it.
			return
		api.setNavigatorObject(self)
		speech.cancelSpeech()
		# Report the entire current page of candidate items if it is newly shown  or it has changed.
		if config.conf["inputComposition"]["autoReportAllCandidates"]:
			oldText = getattr(self.appModule, '_lastImeCandidateVisibleText', '')
			newText = self.visibleCandidateItemsText
			if not isinstance(oldNav, ImeCandidateItem) or newText != oldText:
				print(f"oldText: {oldText}")
				print(f"newText: {newText}")
				self.appModule._lastImeCandidateVisibleText = newText
				# speak the new page
				ui.message(newText)
		# Now just report the currently selected candidate item.
		self.reportFocus()


class AppModule(AppModule):

	_modernKeyboardInterfaceActive = False
	_symbolsGroupSelected = False

	def event_UIA_elementSelected(self, obj, nextHandler):
		# Ask NVDA to respond to UIA events coming from this overlay.
		# Focus change event will not work, as it'll cause focus to be lost when the panel closes.
		import UIAHandler
		if hasattr(UIAHandler.handler, "addEventHandlerGroup") and config.conf["UIA"]["selectiveEventRegistration"]:
			UIAHandler.handler.removeEventHandlerGroup(obj.UIAElement, UIAHandler.handler.localEventHandlerGroup)
			UIAHandler.handler.addEventHandlerGroup(obj.UIAElement, UIAHandler.handler.localEventHandlerGroup)
		# Logic for IME candidate items is handled all within its own object
		# Therefore pass these events straight on.
		if isinstance(obj, ImeCandidateItem):
			return nextHandler()
		# Wait until modern keyboard is fully displayed on screen.
		if winVersion.isWin10(version=1803) and not self._modernKeyboardInterfaceActive:
			return
		# If emoji/kaomoji/symbols group item gets selected, just tell NVDA to treat it as the new navigator object (for presentational purposes) and move on.
		if obj.parent.UIAElement.cachedAutomationId == "TEMPLATE_PART_Groups_ListView":
			api.setNavigatorObject(obj)
			if obj.positionInfo["indexInGroup"] != 1:
				# Symbols group flag must be set if and only if emoji panel is active, as UIA item selected event is fired just before emoji panel opens when opening the panel after closing it for a while.
				self._symbolsGroupSelected = True
			return
		automationId = obj._getUIACacheablePropertyValue(UIAHandler.UIA_AutomationIdPropertyId)
		# #7273: When this is fired on categories, the first emoji from the new category is selected but not announced.
		# Therefore, move the navigator object to that item if possible.
		# However, in recent builds, name change event is also fired.
		# For consistent experience, report the new category first by traversing through controls.
		# #8189: do not announce candidates list itself (not items), as this is repeated each time candidate items are selected.
		if (
			automationId == "CandidateList"
			# Also, when changing categories (emoji, kaomoji, symbols) in Version 1903 or later, category items are selected when in fact they have no text labels.
			or obj.parent.UIAElement.cachedAutomationId == "TEMPLATE_PART_Sets_ListView"
			# Specifically to suppress skin tone modifiers from being announced after an emoji group was selected.
			or self._symbolsGroupSelected
			# In Version 1709 and 1803, both categories and items raise element selected event when category changes.
			or obj.name == self._recentlySelected and not winVersion.isWin10(version=1809)
		):
			return
		speech.cancelSpeech()
		# Sometimes, due to bad tree traversal or wrong item getting selected, something other than the selected item sees this event.
		# In build 18262, emoji panel may open to People group and skin tone modifier gets selected.
		# Skin tone modifiers are also selected when switching to People emoji group, and this should be suppressed.
		if obj.parent.UIAElement.cachedAutomationId == "SkinTonePanelModifier_ListView":
			# But this will point to nothing if emoji search results are not people.
			if obj.parent.next is not None:
				obj = obj.parent.next
			else:
				obj = obj.parent.parent.firstChild
		candidate = obj
		if obj and obj.UIAElement.cachedClassName == "ListViewItem" and obj.parent and isinstance(obj.parent, UIA) and obj.parent.UIAElement.cachedAutomationId != "TEMPLATE_PART_ClipboardItemsList":
			# The difference between emoji panel and suggestions list is absence of categories/emoji separation.
			# Turns out automation ID for the container is different, observed in build 17666 when opening clipboard copy history.
			candidate = obj.parent.previous
			if candidate is not None:
				# Emoji categories list.
				ui.message(candidate.name)
				obj = candidate.firstChild
		if obj is not None:
			api.setNavigatorObject(obj)
			# NVDA Core issue 10093: for Japanese IME, candidates must be spelled.
			if obj.parent.UIAElement.cachedAutomationId == "IME_Candidate_Window":
				speech.speakSpelling(obj.name, useCharacterDescriptions=True)
			else:
				obj.reportFocus()
			# NVDA Core issue 10371: as part of speech sequence work in 2019.3, braille.getBrailleTextForProperties has been renamed to getPropertiesBraille.
			braille.handler.message(braille.getPropertiesBraille(name=obj.name, role=obj.role, positionInfo=obj.positionInfo))
			# Cache selected item.
			self._recentlySelected = obj.name
		else:
			from . import skipTranslation
			skipTranslation.translate("No emoji")
		nextHandler()

	# Emoji panel for build 16299 and 17134.
	_classicEmojiPanelAutomationIds = ("TEMPLATE_PART_ExpressiveInputFullViewFuntionBarItemControl", "TEMPLATE_PART_ExpressiveInputFullViewFuntionBarCloseButton")

	def event_UIA_window_windowOpen(self, obj, nextHandler):
		# Ask NVDA to respond to UIA events coming from modern keyboard interface.
		# Focus change event will not work, as it'll cause focus to be lost when the panel closes.
		import UIAHandler
		if hasattr(UIAHandler.handler, "addEventHandlerGroup") and config.conf["UIA"]["selectiveEventRegistration"] and obj.firstChild is not None:
			localEventHandlerElements = [obj.firstChild]
			# For dictation, add elements manually so name change event can be handled.
			if obj.firstChild.UIAElement.cachedAutomationId == "DictationMicrophoneButton":
				element = obj.children[1]
				while element.next is not None:
					localEventHandlerElements.append(element)
					element = element.next
			for element in localEventHandlerElements:
				UIAHandler.handler.removeEventHandlerGroup(element.UIAElement, UIAHandler.handler.localEventHandlerGroup)
				UIAHandler.handler.addEventHandlerGroup(element.UIAElement, UIAHandler.handler.localEventHandlerGroup)
		# Make sure to announce most recently used emoji first in post-1709 builds.
		# Fake the announcement by locating 'most recently used" category and calling selected event on this.
		# However, in build 17666 and later, child count is the same for both emoji panel and hardware keyboard candidates list.
		# Thankfully first child automation ID's are different for each modern input technology.
		# However this event is raised when the input panel closes.
		inputPanel = obj.firstChild
		if inputPanel is None:
			self._modernKeyboardInterfaceActive = False
			self._recentlySelected = None
			return
		# Handle Ime Candidate UI being shown
		if isinstance(inputPanel, ImeCandidateUI):
			eventHandler.queueEvent("show", inputPanel)
			return
		inputPanelAutomationId = inputPanel.UIAElement.cachedAutomationId
		self._modernKeyboardInterfaceActive = True
		self._symbolsGroupSelected = False
		# Emoji panel for build 16299 and 17134.
		# This event is properly raised in build 17134.
		if not winVersion.isWin10(version=1809) and inputPanelAutomationId in self._classicEmojiPanelAutomationIds:
			eventHandler.queueEvent("UIA_elementSelected", obj.lastChild.firstChild)
		# Handle hardware keyboard and CJK IME suggestions.
		# Treat it the same as CJK composition list - don't announce this if candidate announcement setting is off.
		# In fact, in 20H1, this is the CJK IME candidates window.
		elif inputPanelAutomationId in ("CandidateWindowControl", "IME_Candidate_Window", "IME_Prediction_Window") and config.conf["inputComposition"]["autoReportAllCandidates"]:
			try:
				eventHandler.queueEvent("UIA_elementSelected", inputPanel.firstChild.firstChild)
			except AttributeError:
				# Because this is dictation window.
				pass
		# Emoji panel in build 17666 and later (unless this changes).
		elif inputPanelAutomationId == "TEMPLATE_PART_ExpressionGroupedFullView":
			# On some systems, there is something else besides grouping controls, so another child control must be used.
			emojisList = inputPanel.children[-2]
			if emojisList.UIAElement.cachedAutomationId != "TEMPLATE_PART_Items_GridView":
				emojisList = emojisList.previous
			try:
				# Avoid announcing skin tone modifiers if possible.
				emojiItem = emojisList.firstChild.firstChild
				if emojiItem.UIAElement.cachedAutomationId == "SkinTonePanelModifier_ListView":
					emojiItem = emojiItem.next
				eventHandler.queueEvent("UIA_elementSelected", emojiItem)
			except AttributeError:
				# In build 18272's emoji panel, emoji list becomes empty in some situations.
				pass
		# Clipboard history.
		# Move to clipboard list so element selected event can pick it up.
		elif inputPanelAutomationId == "TEMPLATE_PART_ClipboardTitleBar":
			# Under some cases, clipboard tip text isn't shown on screen, causing clipboard history title to be announced instead of most recently copied item.
			clipboardHistoryItem = obj.children[-2]
			if clipboardHistoryItem.UIAElement.cachedAutomationId == inputPanelAutomationId:
				clipboardHistoryItem = clipboardHistoryItem.next
			# Make sure to move to actual clipboard history item if available.
			if clipboardHistoryItem.firstChild is not None:
				clipboardHistoryItem = clipboardHistoryItem.firstChild
			eventHandler.queueEvent("UIA_elementSelected", clipboardHistoryItem)
		nextHandler()

	def event_nameChange(self, obj, nextHandler):
		# Logic for IME candidate items is handled all within its own object
		# Therefore pass these events straight on.
		if isinstance(obj, ImeCandidateItem):
			return nextHandler()
		elif isinstance(obj, ImeCandidateUI):
			return nextHandler()
		try:
			cachedAutomationId = obj.UIAElement.cachedAutomationId
		except COMError:
			cachedAutomationId = ""
		# Forget it if there is no Automation ID and class name set.
		if (
			(obj.UIAElement.cachedClassName == "" and cachedAutomationId == "")
			# In build 18975, CJK IME candidates fire name change event.
			or obj.UIAElement.cachedClassName == "ListViewItem"
			# Clipboard entries fire name change event when opened.
			or (obj.UIAElement.cachedClassName == "TextBlock" and cachedAutomationId == "")
		):
			return
		# On some systems, touch keyboard keys keeps firing name change event.
		# In build 17704, whenever skin tones are selected, name change is fired by emoji entries (GridViewItem).
		if (
			(obj.UIAElement.cachedClassName in ("CRootKey", "GridViewItem"))
			# Just ignore useless clipboard status and vertical scroll bar label.
			# Also top emoji search result must be announced for better user experience.
			or (cachedAutomationId in ("TEMPLATE_PART_ClipboardItemsList", "TEMPLATE_PART_Search_TextBlock", "VerticalScrollBar"))
			# And no, emoji entries should not be announced here.
			or (self._recentlySelected is not None and self._recentlySelected in obj.name)
		):
			return
		# The word "blank" is kept announced, so suppress this on build 17666 and later.
		if winVersion.isWin10(version=1809):
			# In build 17672 and later, return immediatley when element selected event on clipboard item was fired just prior to this.
			# In some cases, parent will be None, as seen when emoji panel is closed in build 18267.
			try:
				if cachedAutomationId == "TEMPLATE_PART_ClipboardItemIndex" or obj.parent.UIAElement.cachedAutomationId == "TEMPLATE_PART_ClipboardItemsList":
					return
			except AttributeError:
				return
			if not self._modernKeyboardInterfaceActive or cachedAutomationId != "TEMPLATE_PART_ExpressionGroupedFullView":
				speech.cancelSpeech()
		# Don't forget to add "Microsoft Candidate UI" as something that should be suppressed.
		if cachedAutomationId not in ("TEMPLATE_PART_ExpressionFullViewItemsGrid", "TEMPLATE_PART_ClipboardItemIndex", "CandidateWindowControl"):
			ui.message(obj.name)
		self._symbolsGroupSelected = False
		if not any(obj.location):
			self._modernKeyboardInterfaceActive = False
			self._recentlySelected = None
		nextHandler()

	def event_stateChange(self, obj, nextHandler):
		# Unconditionally clear symbols group selected flag.
		self._symbolsGroupSelected = False
		# Try detecting if modern keyboard elements are off-screen or the window itself is gone (parent's first child is nothing).
		# But attempting to retrieve object location fails when emoji panel closes without selecting anything, especially in Version 1903 and later.
		# Because of exceptions, check location first.
		if (
			(obj.location is None and obj.parent.firstChild is None and winVersion.isWin10(version=1903))
			or controlTypes.STATE_OFFSCREEN in obj.states
		):
			self._modernKeyboardInterfaceActive = False
			self._recentlySelected = None
		nextHandler()

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			if obj.role == controlTypes.ROLE_LISTITEM and (
				(
					obj.parent.UIAElement.cachedAutomationId in (
						"ExpandedCandidateList",
						"TEMPLATE_PART_AdaptiveSuggestionList",
					)
					and obj.parent.parent.UIAElement.cachedAutomationId == "IME_Candidate_Window"
				)
				or obj.parent.UIAElement.cachedAutomationId in ("IME_Candidate_Window", "IME_Prediction_Window")
			):
				clsList.insert(0, ImeCandidateItem)
			elif obj.role == controlTypes.ROLE_PANE and obj.UIAElement.cachedAutomationId in (
				"IME_Candidate_Window",
				"IME_Prediction_Window"
			):
				clsList.insert(0, ImeCandidateUI)
