# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015-2022 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Reintroduced in 2022, extends SearchUI ap module from NVDA Core

# Start menu search field is not used here but must be imported as it causes error when the app module loads.
from nvdaBuiltin.appModules.searchui import AppModule, StartMenuSearchField  # NOQA: F401
import controlTypes
from NVDAObjects.UIA import UIA, SuggestionListItem


# Mypy should be reminded that this app module is powered by built-in SearchUI app module.
class AppModule(AppModule):  # type: ignore[no-redef]

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			# Start menu search result details are not announced due to UI redesign in 2019.
			# This is applicable across Windows 10 and 11, thus fix it from the base app module.
			if obj.role == controlTypes.Role.LISTITEM and isinstance(obj.parent.parent, SuggestionListItem):
				clsList.insert(0, SuggestionListItem)
				return
		super().chooseNVDAObjectOverlayClasses(obj, clsList)
