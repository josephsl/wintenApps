# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015-2024 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for Shell Experience Host, part of Windows 10 and later.
Shell Experience Host is home to a number of things, including Action Center and other shell features.
In Windows 11 24H2 (2024 Update and Server 2025), quick settings component is part of ShellHost.exe.
"""

# Extends NVDA Core's Shell Experience Host app module.
from nvdaBuiltin.appModules.shellexperiencehost import AppModule
import winUser
from winAPI.types import HWNDValT


# App module class comes from built-in Shell Experience Host app module but Mypy doesn't know that.
class AppModule(AppModule):  # type: ignore[no-redef]

	def isGoodUIAWindow(self, hwnd: HWNDValT) -> bool:
		# NVDA Core issue 16348: reclassify control center window as UIA to allow mouse/touch interaction.
		if winUser.getClassName(hwnd) == "ControlCenterWindow":
			return True
		return False
