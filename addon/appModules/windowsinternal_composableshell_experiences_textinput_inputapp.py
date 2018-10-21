# App module for Composable Shell (CShell) input panel
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2017-2018 NV Access Limited, Joseph Lee
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
			obj = obj.parent.next
		candidate = obj
		parent = obj.parent
		if obj.UIAElement.cachedClassName == "ListViewItem" and isinstance(parent, UIA) and parent.UIAElement.cachedAutomationID != "TEMPLATE_PART_ClipboardItemsList":
			# The difference between emoji panel and suggestions list is absence of categories/emoji separation.
			# Turns out automation ID for the container is different, observed in build 17666 when opening clipboard copy history.
			candidate = obj.parent.previous
			if candidate is not None:
				# Emoji categories list.
				ui.message(candidate.name)
				obj = candidate.firstChild
		if obj is not None:
			api.setNavigatorObject(obj)
			obj.reportFocus()
			braille.handler.message(braille.getBrailleTextForProperties(name=obj.name, role=obj.role, positionInfo=obj.positionInfo))
			# Cache selected item.
			self._recentlySelected = obj.name
		else:
			# Translators: presented when there is no emoji when searching for one in Windows 10 Fall Creators Update and later.
			ui.message(_("No emoji"))
		nextHandler()
