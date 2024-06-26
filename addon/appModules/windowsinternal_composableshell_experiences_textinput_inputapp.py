# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2017-2024 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# The add-on version of this module will extend the one that comes with NVDA Core.
# As of NVDA 2024.3, contents of this module are part of NVDA Core.

from typing import Callable
# Yes, this app module is powered by built-in modern keyboard (TextInputHost) app module
# (formerly WindowsInternal.ComposableShell.Experiences.TextInput.InputApp).
# #70: NVDA Core pull requests are made using the core app module, not alias modules.
from nvdaBuiltin.appModules.windowsinternal_composableshell_experiences_textinput_inputapp import (
	AppModule, ImeCandidateUI
)
import winVersion
import eventHandler
import api
import ui
import config
import versionInfo
import controlTypes
from NVDAObjects import NVDAObject
from NVDAObjects.UIA import UIA, ListItem


# NVDA Core issue 16346: handle Windows 11 emoji panel navigation menu items.
# Resolved in NVDA 2024.3.
class NavigationMenuItem(ListItem):

	def event_UIA_elementSelected(self) -> None:
		# All of these resolved in NVDA 2024.3.
		# Ignore the event altogether.
		if (
			# NVDA Core issue 16346: system focus restored.
			(focus := api.getFocusObject()).appModule != self.appModule
			# NVDA Core issue 16532: repeat announcement due to pending gain focus event on category entries.
			or eventHandler.isPendingEvents("gainFocus")
			# NVDA Core issue 16533: system focus is located in GIF/kaomoji/symbol entry.
			or focus.UIAAutomationId.startswith("item-")
		):
			return
		# Manipulate NVDA's focus object.
		if (
			# NVDA Core issue 16346: NVDA is stuck in a nonexistent edit field (location is None).
			not any(focus.location)
			# NVDA Core issue 16347: Focus is once again stuck in top-level modern keyboard window
			# after switching to clipboard history from other emoji panel screens.
			or focus.firstChild and focus.firstChild.UIAAutomationId == "Windows.Shell.InputApp.FloatingSuggestionUI"
		):
			eventHandler.queueEvent("gainFocus", self.objectWithFocus())
			return
		# Report the selected navigation menu item.
		super().event_UIA_elementSelected()


# Built-in modern keyboard app module powers bulk of the below app module class, so inform Mypy.
class AppModule(AppModule):  # type: ignore[no-redef]

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[NVDAObject]) -> None:
		# NVDA Core issue 16346: recognize Windows 11 emoji panel navigation menu items.
		# Resolved in NVDA 2024.3.
		if (
			(versionInfo.version_year, versionInfo.version_major) < (2024, 3)
			and isinstance(obj, UIA)
			and obj.role == controlTypes.Role.LISTITEM
			and obj.UIAAutomationId.startswith("navigation-menu-item")
		):
			clsList.insert(0, NavigationMenuItem)
			return
		# NVDA Core takes care of the rest.
		super().chooseNVDAObjectOverlayClasses(obj, clsList)

	# The following event handlers are hidden if NVDA 2024.3 or later is running.
	if (versionInfo.version_year, versionInfo.version_major) < (2024, 3):
		def event_UIA_elementSelected(self, obj: NVDAObject, nextHandler: Callable[[], None]):
			# NVDA Core issue 16346: logic for navigation menu items is handled all within its own object
			# Therefore pass these events straight on.
			# Resolved in NVDA 2024.3.
			if isinstance(obj, NavigationMenuItem):
				return nextHandler()
			# NVDA Core takes care of the rest.
			super().event_UIA_elementSelected(obj, nextHandler)

		def event_gainFocus(self, obj: NVDAObject, nextHandler: Callable[[], None]):
			# NVDA Core issue 16347: focus gets stuck in Modern keyboard
			# when clipboard history closes in Windows 11.
			# Resolved in NVDA 2024.3.
			if (
				winVersion.getWinVer() >= winVersion.WIN11
				and obj.firstChild
				and obj.firstChild.UIAAutomationId == "Windows.Shell.InputApp.FloatingSuggestionUI"
			):
				# Do not queue events if events are pending, otherwise move to system focus.
				if not eventHandler.isPendingEvents():
					eventHandler.queueEvent("gainFocus", obj.objectWithFocus())
				return
			nextHandler()

		def event_focusEntered(self, obj: NVDAObject, nextHandler: Callable[[], None]):
			# NVDA Core issue 14023: announce visible IME candidates.
			# Resolved in NVDA 2024.3.
			if (
				isinstance(obj, ImeCandidateUI)
				and obj.parent.UIAAutomationId == "IME_Candidate_Window"
				and config.conf["inputComposition"]["autoReportAllCandidates"]
			):
				ui.message(obj.firstChild.visibleCandidateItemsText)
			nextHandler()
