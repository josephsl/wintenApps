# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2017-2024 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# The add-on version of this module will extend the one that comes with NVDA Core.
# As of NVDA 2024.3, most parts of this module are part of NVDA Core.

# Yes, this app module is powered by built-in modern keyboard (TextInputHost) app module
# (formerly WindowsInternal.ComposableShell.Experiences.TextInput.InputApp).
# #70: NVDA Core pull requests are made using the core app module, not alias modules.
from nvdaBuiltin.appModules.windowsinternal_composableshell_experiences_textinput_inputapp import AppModule
import api
from NVDAObjects import NVDAObject


# Built-in modern keyboard app module powers bulk of the below app module class, so inform Mypy.
class AppModule(AppModule):  # type: ignore[no-redef]

	def event_NVDAObject_init(self, obj: NVDAObject) -> None:
		# NVDA Core issue 17308: recent Windows 11 builds raise live region change event when
		# clipboard history closes, causing NVDA to report data item text such as clipboard history entries.
		# Therefore, tell NVDA to veto this event at the object level, otherwise focus change handling breaks
		# due to live region change event being recorded as an impending event.
		obj._shouldAllowUIALiveRegionChangeEvent = api.getForegroundObject().appModule == self
