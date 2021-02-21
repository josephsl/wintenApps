# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015 NV Access Limited
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Extended by Joseph Lee (copyright 2016-2021, released under GPL)

from nvdaBuiltin.appModules.searchui import *
import config
import nvwave


# In build 18363 and later, File Explorer gains Cortana search field.
# For Start menu and File Explorer, "suggestions" should not be brailled.
# This is more so for File Explorer as a live region will announce suggestion count.
# Note that tools such as Mypy may say there is a cyclic definition
# but the class is renamed thus to align with NVDA Core.
class StartMenuSearchField(StartMenuSearchField):  # type: ignore[misc]

	def event_suggestionsOpened(self):
		# Do not announce "suggestions" in braille.
		if config.conf["presentation"]["reportAutoSuggestionsWithSound"]:
			nvwave.playWaveFile(r"waves\suggestionsOpened.wav")


# Inherits from built-in Search UI app module class.
class AppModule(AppModule):  # type: ignore[misc]

	def event_NVDAObject_init(self, obj):
		if isinstance(obj, UIA):
			# Build 18945 introduces (or re-introduces) modern search experience in File Explorer,
			# and as part of this, suggestion count is part of a live region.
			# Although it is geared for Narrator, it is applicable to other screen readers as well.
			# The live region itself is a child of the one shown here.
			if obj.UIAAutomationId == "suggestionCountForNarrator" and obj.firstChild is not None:
				obj.name = obj.firstChild.name

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Without this, NVDA will announce "suggestions" in braille.
		# Return early so the app module class included in NVDA Core can check for other overlay classes.
		if isinstance(obj, UIA) and obj.UIAAutomationId == "SearchTextBox":
			clsList.insert(0, StartMenuSearchField)
			return
		super(AppModule, self).chooseNVDAObjectOverlayClasses(obj, clsList)
