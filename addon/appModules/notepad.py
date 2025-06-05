# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2022-2025 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for Windows Notepad.
While this app module also covers older Notepad releases,
this module provides workarounds for Windows 11 Notepad."""

# Import the base Notepad app module as something else to avoid runtime issues.
from nvdaBuiltin.appModules.notepad import AppModule as CoreAppModule
import controlTypes
from NVDAObjects.UIA import UIA
from NVDAObjects import NVDAObject


class AppModule(CoreAppModule):
	def event_NVDAObject_init(self, obj: NVDAObject):
		# NVDA Core issue 18208: "go to line" edit field is classified as a dialog.
		if isinstance(obj, UIA) and obj.UIAAutomationId == "LineNumberBox":
			obj.role = controlTypes.Role.EDITABLETEXT
