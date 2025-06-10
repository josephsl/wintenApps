# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015-2025 NV Access Limited, Joseph Lee, James Teh
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Reintroduced in 2025, extends SearchUI ap module from NVDA Core

from typing import List
# Start menu search field is not used here but must be imported as it causes error when the app module loads.
from nvdaBuiltin.appModules.searchui import AppModule, StartMenuSearchField  # NOQA: F401
from NVDAObjects.UIA import UIA
from NVDAObjects import NVDAObject


# Bulk of the below class comes from NVDA Core.
class StartMenuSearchField(StartMenuSearchField):  # type: ignore[no-redef]

	def _get_description(self) -> str:
		# NVDA Core issue 13841: detect search highlights and anounce it.
		# Resolved in NVDA 2023.1.
		if self.lastChild.UIAAutomationId == "PlaceholderTextContentPresenter":
			return self.lastChild.name
		return super().description


# Mypy should be reminded that this app module is powered by built-in SearchUI app module.
class AppModule(AppModule):  # type: ignore[no-redef]
	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: List[NVDAObject]) -> None:
		if isinstance(obj, UIA):
			if obj.UIAAutomationId == "SearchTextBox":
				clsList.insert(0, StartMenuSearchField)
				return
		super().chooseNVDAObjectOverlayClasses(obj, clsList)
