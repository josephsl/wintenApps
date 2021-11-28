# -*- coding: UTF-8 -*-
# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2020 NV Access Limited, Joseph Lee, Łukasz Golonka, Julien Cochuyt
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Specific workarounds for Windows 11.
from nvdaBuiltin.appModules.explorer import *  # NOQA: F403
from NVDAObjects.UIA import UIA


# Built-in File Explorer app module powers bulk of the below app module class, so inform Mypy.
# And Flake8 and other linters, to.
class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405

	def event_gainFocus(self, obj, nextHandler):
		if obj.windowClassName == "XamlExplorerHostIslandWindow":
			# Do not allow "task switching" to be announced when switching apps in Windows 11.
			try:
				isTaskSwitchingWindow = obj.firstChild.firstChild.firstChild.UIAAutomationId == "TaskSwitchingWindow"
			except AttributeError:
				isTaskSwitchingWindow = False
			# Suppress "pane" announcement when Windows 11 Snap Layouts opens.
			# As this is a name check, do this before checking Task Switching window for performance.
			if obj.name is None or isTaskSwitchingWindow:
				return
		super(AppModule, self).event_gainFocus(obj, nextHandler)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Do not allow "pane" to be announced when switching apps in Windows 11.
		# Caused by UIA focus event coming from input site window.
		# Thankfully this behavior is similar to Windows 10's multitasking view frame window.
		# Resolved in NVDA 2021.3.
		if isinstance(obj, UIA):
			if obj.UIAElement.cachedClassName == "Windows.UI.Input.InputSite.WindowClass":
				clsList.insert(0, MultitaskingViewFrameWindow)  # NOQA: F405
				return
		super(AppModule, self).chooseNVDAObjectOverlayClasses(obj, clsList)
