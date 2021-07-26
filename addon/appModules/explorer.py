# -*- coding: UTF-8 -*-
# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2020 NV Access Limited, Joseph Lee, Łukasz Golonka, Julien Cochuyt
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for Windows Explorer (aka Windows shell and renamed to File Explorer in Windows 8).
Provides workarounds for controls such as identifying Start button, notification area and others.
"""

# Specific workarounds for Windows 11.
from nvdaBuiltin.appModules.explorer import *  # NOQA: F403
import controlTypes
from NVDAObjects.UIA import UIA
from NVDAObjects.IAccessible import IAccessible


# The following buttons are really buttons, not toggle buttons
# unless the purpose of these buttons are different.
WIN11_RECLASSIFY_TOGGLE_BUTTONS = [
	"StartButton",
	"SearchButton",
	"TaskViewButton",
	"WidgetsButton",
	"MeetNowButton"
]


# Do not allow "pane" to be announced when switching apps in Windows 11.
class InputSiteWindow(UIA):
	shouldAllowUIAFocusEvent = False


# Do not allow "task switching" to be announced when switching apps in Windows 11.
class Win11TaskSwitchingWindow(IAccessible):
	event_gainFocus = None


# Support control types refactor (both before (2021.1) and after (2021.2) for a time).
# Note that pre-refactor attributes will be gone in NVDA 2022.1.


# Built-in File Explorer app module powers bulk of the below app module class, so inform Mypy.
# And Flake8 and other linters, to.
class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405

	def event_NVDAObject_init(self, obj):
		# No, these buttons should not be a toggle button, and discard checkable state, too.
		if isinstance(obj, UIA) and obj.UIAAutomationId in WIN11_RECLASSIFY_TOGGLE_BUTTONS:
			obj.role = controlTypes.ROLE_BUTTON
			obj.states.discard(controlTypes.STATE_CHECKABLE)
			return
		super(AppModule, self).event_NVDAObject_init(obj)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			# Suppress focus announcement for input site window as it is annoying.
			if obj.UIAElement.cachedClassName == "Windows.UI.Input.InputSite.WindowClass":
				clsList.insert(0, InputSiteWindow)
				return
		elif isinstance(obj, IAccessible):
			if obj.windowClassName == "XamlExplorerHostIslandWindow":
				clsList.insert(0, Win11TaskSwitchingWindow)
				return
		super(AppModule, self).chooseNVDAObjectOverlayClasses(obj, clsList)
