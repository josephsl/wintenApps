# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015 NV Access Limited
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Extended by Joseph Lee (copyright 2016-2021, released under GPL)

# Powered by built-in SearchApp (formerly SearchUI) app module.
from nvdaBuiltin.appModules.searchapp import *  # NOQA: F403
import config
import nvwave
from NVDAObjects.UIA import UIA


# In Windows 10 1909 and later, File Explorer gains Cortana search field.
# For Start menu and File Explorer, "suggestions" should not be brailled.
# This is more so for File Explorer as a live region will announce suggestion count.
# Note that tools such as Mypy may say there is a cyclic definition
# but the class is renamed thus to align with NVDA Core.
class StartMenuSearchField(StartMenuSearchField):  # type: ignore[misc]  # NOQA: F405

	def event_suggestionsOpened(self):
		# Do not announce "suggestions" in braille.
		if config.conf["presentation"]["reportAutoSuggestionsWithSound"]:
			nvwave.playWaveFile(r"waves\suggestionsOpened.wav")


# Inherits from built-in Search UI app module class.
class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Without this, NVDA will announce "suggestions" in braille.
		# Return early so the app module class included in NVDA Core can check for other overlay classes.
		if isinstance(obj, UIA) and obj.UIAAutomationId == "SearchTextBox":
			clsList.insert(0, StartMenuSearchField)
			return
		super(AppModule, self).chooseNVDAObjectOverlayClasses(obj, clsList)
