#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2015 NV Access Limited
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
# Extended by Joseph Lee (copyright 2016-2019, released under GPL)

# Extended to let NVDA cooperate with Cortana.

from nvdaBuiltin.appModules.searchui import *
import controlTypes
import api
import speech
import ui
import config
import nvwave
from NVDAObjects.UIA import SuggestionListItem


# In build 18363 and later, File Explorer gains Cortana search field.
# For Start menu and File Explorer, "suggestions" should not be brailled.
# This is more so for File Explorer as a live region will announce suggestion count.
class StartMenuSearchField(SearchField):

	# #7370: do not announce text when start menu (searchui) closes.
	announceNewLineText = False

	def event_suggestionsOpened(self):
		# Do not announce "suggestions" in braille.
		if config.conf["presentation"]["reportAutoSuggestionsWithSound"]:
			nvwave.playWaveFile(r"waves\suggestionsOpened.wav")


class AppModule(AppModule):

	def chooseNVDAObjectOverlayClasses(self,obj,clsList):
		if isinstance(obj,IAccessible):
			try:
				# #5288: Never use ContentGenericClient, as this uses displayModel
				# which will freeze if the process is suspended.
				clsList.remove(ContentGenericClient)
			except ValueError:
				pass
		elif isinstance(obj,UIA):
			# Since 2019, some suggestion items are not exposed as a list item but are children of a search category.
			if obj.role == controlTypes.ROLE_LISTITEM and isinstance(obj.parent, SuggestionListItem):
				clsList.insert(0, SuggestionListItem)
			elif obj.UIAElement.cachedAutomationID == "SearchTextBox":
				clsList.insert(0, StartMenuSearchField)

	# Past responses from Cortana (cached to prevent repetition, initially an empty string).
	# No longer appicable in Version 1809 due to UI redesign.
	cortanaResponseCache = ""

	def event_nameChange(self, obj, nextHandler):
		# NVDA, can you act as a mouthpiece for Cortana?
		if isinstance(obj, UIA) and isinstance(obj.next, UIA) and obj.next.UIAElement.cachedAutomationID != "SpeechButton" and obj.name != self.cortanaResponseCache:
			element = obj.UIAElement
			# There are two Cortana response lines. Usually line 2 is more reliable.
			# However, Redstone seems to favor line 1 better.
			# A specific automation ID is used for reminders and others.
			if element.cachedAutomationID in ("SpeechContentLabel", "WeSaidTextBlock", "GreetingLine1"):
				ui.message(obj.name)
				self.cortanaResponseCache = obj.name
		nextHandler()

	def event_liveRegionChange(self, obj, nextHandler):
		# Build 18945 introduces (or re-introduces) modern search experience in File Explorer, and as part of this, suggestion count is part of a live region.
		# Although it is geared for Narrator, it is applicable to other screen readers as well. The live region itself is a child of the one shown here.
		if isinstance(obj, UIA) and obj.UIAElement.cachedAutomationID == "suggestionCountForNarrator":
			if obj.firstChild.name: ui.message(obj.firstChild.name)
		nextHandler()
