# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2019-2025 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Originally copyright 2016-2025 Joseph Lee, released under GPL

# Several hacks related to Settings app
# Settings app is a UIA world, hence no instance checks.

# Extends NVDA Core's System Settings app module.
from nvdaBuiltin.appModules.systemsettings import AppModule
import typing
import speech
import NVDAObjects


# App module class comes from built-in System Settings app module but Mypy doesn't know that.
class AppModule(AppModule):  # type: ignore[no-redef]
	def event_liveRegionChange(self, obj: NVDAObjects.NVDAObject, nextHandler: typing.Callable[[], None]):
		# Windows 10 Settings/Update and Security/Windows Update
		# Announce individual update progress except as noted below.
		if "ApplicableUpdate" in obj.UIAAutomationId:
			# NVDA Core issue 14931: update title/status repeats while downloading and installing updates.
			# #71: NVDA is told to announce live regions to the end by default,
			# which results in screen content and speech getting out of sync.
			# Therefore, announce live region changes whenever possible despite constant speech interruption.
			speech.cancelSpeech()
		nextHandler()
