# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015-2021 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# NVDA Core includes bulk of this app module.
from nvdaBuiltin.appModules.calculator import *  # NOQA: F403
from NVDAObjects.UIA import UIA


# Mypy should be reminded that this app module is powered by built-in Calculator app module.
# Inform Flake8 as well.
class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405

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
		# Call the built-in app module version of UIA notification event handler.
		super(AppModule, self).event_UIA_notification(
			obj, nextHandler, displayString=displayString, activityId=activityId, **kwargs
		)
