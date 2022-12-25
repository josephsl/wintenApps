# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015-2023 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Reintroduced in 2022, extends SearchUI ap module from NVDA Core

# Start menu search field is not used here but must be imported as it causes error when the app module loads.
from nvdaBuiltin.appModules.searchui import AppModule, StartMenuSearchField  # NOQA: F401
from NVDAObjects.UIA import UIA


class StartMenuSearchField(StartMenuSearchField):

	def _get_description(self) -> str:
		# NVDA Core issue 13841: detect search highlights and anounce it.
		# Resolved in NVDA 2023.1.
		if self.lastChild.UIAAutomationId == "PlaceholderTextContentPresenter":
			return self.lastChild.name
		return super().description


# Mypy should be reminded that this app module is powered by built-in SearchUI app module.
class AppModule(AppModule):  # type: ignore[no-redef]

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			if obj.UIAAutomationId == "SearchTextBox":
				clsList.insert(0, StartMenuSearchField)
				return
		super().chooseNVDAObjectOverlayClasses(obj, clsList)
