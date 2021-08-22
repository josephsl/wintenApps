# -*- coding: UTF-8 -*-
# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2020 NV Access Limited, Joseph Lee, Łukasz Golonka, Julien Cochuyt
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Specific workarounds for Windows 11.
from nvdaBuiltin.appModules.explorer import *  # NOQA: F403
import controlTypes
from NVDAObjects.UIA import UIA


# The following buttons are really buttons, not toggle buttons
# unless the purpose of these buttons are different.
WIN11_RECLASSIFY_TOGGLE_BUTTONS = [
	"StartButton",
	"SearchButton",
	"TaskViewButton",
	"WidgetsButton",
	"MeetNowButton"
]


# Built-in File Explorer app module powers bulk of the below app module class, so inform Mypy.
# And Flake8 and other linters, to.
class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405

	def event_NVDAObject_init(self, obj):
		# No, these buttons should not be a toggle button, and discard checkable state, too.
		if isinstance(obj, UIA) and obj.UIAAutomationId in WIN11_RECLASSIFY_TOGGLE_BUTTONS:
			obj.role = controlTypes.Role.BUTTON
			obj.states.discard(controlTypes.State.CHECKABLE)
			return
		super(AppModule, self).event_NVDAObject_init(obj)

	def event_gainFocus(self, obj, nextHandler):
		# Do not allow "task switching" to be announced when switching apps in Windows 11.
		if obj.windowClassName == "XamlExplorerHostIslandWindow":
			return
		super(AppModule, self).event_gainFocus(obj, nextHandler)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Do not allow "pane" to be announced when switching apps in Windows 11.
		# Caused by UIA focus event coming from input site window.
		# Thankfully this behavior is similar to Windows 10's multitasking view frame window.
		if isinstance(obj, UIA):
			if obj.UIAElement.cachedClassName == "Windows.UI.Input.InputSite.WindowClass":
				clsList.insert(0, MultitaskingViewFrameWindow)  # NOQA: F405
				return
		super(AppModule, self).chooseNVDAObjectOverlayClasses(obj, clsList)
