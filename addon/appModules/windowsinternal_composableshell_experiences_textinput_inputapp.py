# App module for Composable Shell (CShell) input panel
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2017-2019 NV Access Limited, Joseph Lee
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""App module for Windows 10 Modern Keyboard aka new touch keyboard panel.
The chief feature is allowing NVDA to announce selected emoji when using the keyboard to search for and select one.
Another feature is to announce candidates for misspellings if suggestions for hardware keyboard is selected.
This is applicable on Windows 10 Fall Creators Update and later."""

# The add-on version of this module will extend the one that comes with NVDA Core (2018.3 and later).

from nvdaBuiltin.appModules.windowsinternal_composableshell_experiences_textinput_inputapp import *

class AppModule(AppModule):

	def event_UIA_elementSelected(self, obj, nextHandler):
		# #7273: When this is fired on categories, the first emoji from the new category is selected but not announced.
		# Therefore, move the navigator object to that item if possible.
		# However, in recent builds, name change event is also fired.
		# For consistent experience, report the new category first by traversing through controls.
		# #8189: do not announce candidates list itself (not items), as this is repeated each time candidate items are selected.
		if obj.UIAElement.cachedAutomationID == "CandidateList": return
		speech.cancelSpeech()
		# Sometimes, due to bad tree traversal or wrong item getting selected, something other than the selected item sees this event.
		# Sometimes clipboard candidates list gets selected, so ask NvDA to descend one more level.
		if obj.UIAElement.cachedAutomationID == "TEMPLATE_PART_ClipboardItemsList":
			obj = obj.firstChild
		# In build 18262, emoji panel may open to People group and skin tone modifier or the list housing them gets selected.
		elif obj.UIAElement.cachedAutomationID == "SkinTonePanelModifier_ListView":
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
			braille.handler.message(braille.getBrailleTextForProperties(name=obj.name, role=obj.role, positionInfo=obj.positionInfo))
			# Cache selected item.
			self._recentlySelected = obj.name
		else:
			from . import skipTranslation
			skipTranslation.translate("No emoji")
		nextHandler()

	def event_UIA_window_windowOpen(self, obj, nextHandler):
		# Make sure to announce most recently used emoji first in post-1709 builds.
		# Fake the announcement by locating 'most recently used" category and calling selected event on this.
		# However, in build 17666 and later, child count is the same for both emoji panel and hardware keyboard candidates list.
		# Thankfully first child automation ID's are different for each modern input technology.
		# However this event is raised when the input panel closes.
		inputPanel = obj.firstChild
		if inputPanel is None:
			return
		inputPanelAutomationID = inputPanel.UIAElement.cachedAutomationID
		# Emoji panel for build 16299 and 17134.
		# This event is properly raised in build 17134.
		if winVersion.winVersion.build <= 17134 and inputPanelAutomationID in ("TEMPLATE_PART_ExpressiveInputFullViewFuntionBarItemControl", "TEMPLATE_PART_ExpressiveInputFullViewFuntionBarCloseButton"):
			self.event_UIA_elementSelected(obj.lastChild.firstChild, nextHandler)
		# Handle hardware keyboard and CJK IME suggestions.
		# Treat it the same as CJK composition list - don't announce this if candidate announcement setting is off.
		# In fact, in 20H1, this is the CJK IME candidates window.
		elif inputPanelAutomationID in ("CandidateWindowControl", "IME_Candidate_Window", "IME_Prediction_Window") and config.conf["inputComposition"]["autoReportAllCandidates"]:
			try:
				self.event_UIA_elementSelected(inputPanel.firstChild.firstChild, nextHandler)
			except AttributeError:
				# Because this is dictation window.
				pass
		# Emoji panel in build 17666 and later (unless this changes).
		elif inputPanelAutomationID == "TEMPLATE_PART_ExpressionGroupedFullView":
			self._emojiPanelJustOpened = True
			# On some systems, there is something else besides grouping controls, so another child control must be used.
			emojisIndex = -3 if inputPanel.children[-2].UIAElement.cachedAutomationID != "TEMPLATE_PART_Items_GridView" else -2
			try:
				self.event_UIA_elementSelected(inputPanel.children[emojisIndex].firstChild.firstChild, nextHandler)
			except AttributeError:
				# In build 18272's emoji panel, emoji list becomes empty in some situations.
				pass
		# Clipboard history.
		# Move to clipboard list so element selected event can pick it up.
		elif inputPanelAutomationID == "TEMPLATE_PART_ClipboardTitleBar":
			# Under some cases, clipboard tip text isn't shown on screen, causing clipboard history title to be announced instead of most recently copied item.
			clipboardItemsIndex = -2 if obj.children[-2].UIAElement.cachedAutomationID != inputPanelAutomationID else -1
			self.event_UIA_elementSelected(obj.children[clipboardItemsIndex], nextHandler)
		nextHandler()

	def event_nameChange(self, obj, nextHandler):
		# In build 18975, CJK IME candidates fire name change event.
		if obj.UIAElement.cachedClassName == "ListViewItem": return
		super(AppModule, self).event_nameChange(obj, nextHandler)
