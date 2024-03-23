# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2019-2024 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Originally copyright 2016-2024 Joseph Lee, released under GPL

# Several hacks related to Settings app
# Settings app is a UIA world, hence no instance checks.

from typing import Callable
# Extends NVDA Core's System Settings app module.
from nvdaBuiltin.appModules.systemsettings import AppModule
import speech
from NVDAObjects import NVDAObject


# App module class comes from built-in System Settings app module but Mypy doesn't know that.
class AppModule(AppModule):  # type: ignore[no-redef]

	def event_liveRegionChange(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# Applies mostly to Windows 10
		# In Windows 11, name change event raised by individual update entry announces update status,
		# and the updates list stays up once completed so they can be reviewed via object navigation.
		# In Windows 10, updates list is gone once applied, so update history must be used to review updates.
		# The overall update progress is reported in Windows 11 just as in 10.
		# In Windows 10, announce individual update progress except as noted below.
		if "ApplicableUpdate" in obj.UIAAutomationId:
			# Do not announce status text itself.
			if obj.UIAAutomationId.endswith("_ContextDescriptionTextBlock"):
				return
			# Update title repeats while the update is downloaded and installed.
			# #71: NVDA is told to announce live regions to the end by default,
			# which results in screen content and speech getting out of sync.
			# However do not cut off other live regions when action button appears next to updates list
			# which is the sibling of the grandparent object (actual updates list element).
			# Update action button appears if the system is up to date or an action is required.
			# However attribute error may result if "update action" button is not a UIA element.
			try:
				if "UpdateActionButton" not in obj.parent.parent.next.UIAAutomationId:
					speech.cancelSpeech()
			except AttributeError:
				pass
		nextHandler()
