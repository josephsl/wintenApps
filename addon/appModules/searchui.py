# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015-2022 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Reintroduced in 2022, extends SearchUI ap module from NVDA Core

# Start menu search field is not used here but must be imported as it causes error when the app module loads.
from nvdaBuiltin.appModules.searchui import AppModule, StartMenuSearchField  # NOQA: F401
import controlTypes
from NVDAObjects.UIA import UIA, SuggestionListItem
import ui
import queueHandler


# Mypy should be reminded that this app module is powered by built-in SearchUI app module.
class AppModule(AppModule):  # type: ignore[no-redef]

	def event_gainFocus(self, obj, nextHandler):
		if isinstance(obj, StartMenuSearchField):
			# Detect search highlights and anounce it.
			if obj.lastChild.UIAAutomationId == "PlaceholderTextContentPresenter":
				queueHandler.queueFunction(queueHandler.eventQueue, ui.message, obj.lastChild.name)
		nextHandler()
