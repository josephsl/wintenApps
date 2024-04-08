# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015-2024 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Workarounds for Windows 11 24H2 quick settings interface (ShellHost)

# Extends NVDA Core's Shell Experience Host app module.
from nvdaBuiltin.appModules.shellexperiencehost import AppModule
import winUser
from winAPI.types import HWNDValT


# App module class comes from built-in Shell Experience Host app module but Mypy doesn't know that.
class AppModule(AppModule):  # type: ignore[no-redef]

	def isGoodUIAWindow(self, hwnd: HWNDValT) -> bool:
		# NVDA Core issue 16348: reclassify control center window as UIA to allow mouse/touch interaction.
		# Resolved in NVDA 2024.2.
		if winUser.getClassName(hwnd) == "ControlCenterWindow":
			return True
		return False
