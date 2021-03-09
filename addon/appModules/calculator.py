# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015-2021 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for Windows 10 Calculator"""

# NVDA Core includes bulk of this app module.
from nvdaBuiltin.appModules.calculator import *  # NOQA: F403


class AppModule(AppModule):

	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		# Add additional Calculator result gestures until they are added to NVDA Core.
		self.bindGesture("kb:delete", "calculatorResult")
		self.bindGesture("kb:numpadDelete", "calculatorResult")

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
		super(AppModule, self).event_UIA_notification(obj, nextHandler, activityId=activityId, **kwargs)
