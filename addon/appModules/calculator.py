# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015-2022 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Extend NVDA Core's Calculator module.
from nvdaBuiltin.appModules.calculator import AppModule, noCalculatorEntryAnnouncements
import api
import braille
from NVDAObjects.UIA import UIA


# Mypy should be reminded that this app module is powered by built-in Calculator app module.
class AppModule(AppModule):  # type: ignore[no-redef]

	def event_NVDAObject_init(self, obj):
		if not isinstance(obj, UIA):
			return
		# Version 10.2009 introduces a regression where history and memory items have no names
		# but can be fetched through its children.
		if not obj.name and obj.parent.UIAAutomationId in ("HistoryListView", "MemoryListView"):
			obj.name = "".join([item.name for item in obj.children])

	def event_UIA_notification(self, obj, nextHandler, displayString=None, activityId=None, **kwargs):
		# Some notification messages are repeated (most notable being graph view change notification).
		if activityId == "GraphViewChanged" and self._resultsCache == displayString:
			return
		self._resultsCache = displayString
		# Version 10.2109 changes the UI a bit, requiring tweaked event handler implementation.
		# Version bumped to 11 in October 2021.
		calculatorVersion = int(self.productVersion.split(".")[0])
		# NVDA Core issue 12268: for "DisplayUpdated", announce display strings in braille.
		if activityId == "DisplayUpdated":
			braille.handler.message(displayString)
			resultElement = api.getForegroundObject().children[1].lastChild
			# In version 11, the actual display text and other controls live inside a toggle control window.
			# Therefore move one more level down compared to older Calculator releases.
			if calculatorVersion >= 11:
				resultElement = resultElement.firstChild
			# Redesigned in 2019 due to introduction of "always on top" i.e. compact overlay mode.
			if resultElement.UIAElement.cachedClassName != "LandmarkTarget":
				resultElement = resultElement.parent.children[1]
			# Display updated activity ID seen when entering calculations should be ignored
			# as as it is redundant if speak typed characters is on.
			if (
				resultElement
				and resultElement.firstChild
				and resultElement.firstChild.UIAAutomationId in noCalculatorEntryAnnouncements
			):
				return
		nextHandler()
