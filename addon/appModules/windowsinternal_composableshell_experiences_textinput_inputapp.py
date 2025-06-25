# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2017-2025 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# The add-on version of this module will extend the one that comes with NVDA Core.
# As of NVDA 2024.3, most parts of this module are part of NVDA Core.

# Yes, this app module is powered by built-in modern keyboard (TextInputHost) app module
# (formerly WindowsInternal.ComposableShell.Experiences.TextInput.InputApp).
# #70: NVDA Core pull requests are made using the core app module, not alias modules.
from nvdaBuiltin.appModules.windowsinternal_composableshell_experiences_textinput_inputapp import AppModule
from collections.abc import Callable
import api
from NVDAObjects import NVDAObject


# Built-in modern keyboard app module powers bulk of the below app module class, so inform Mypy.
class AppModule(AppModule):  # type: ignore[no-redef]
	def event_UIA_elementSelected(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# NVDA Core issue 18236: NVDA reports selected emoji panel twice in Windows 11.
		# Because base NVDA object will announce selected item, this causes speech repetition
		# if the event handler is allowed to run through its course.
		# Therefore, let the base implementation report selected item and no more.
		# Resolved in NVDA 2025.2.
		if api.getFocusObject().appModule == self:
			return nextHandler()
		super().event_UIA_elementSelected(obj, nextHandler)
