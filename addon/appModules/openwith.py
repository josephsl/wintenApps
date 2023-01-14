# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2011-2023 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

from nvdaBuiltin.appModules.openwith import AppModule
import winUser


# App module class comes from built-in Open With app module but Mypy doesn't know that.
class AppModule(AppModule):  # type: ignore[no-redef]

	def isGoodUIAWindow(self, hwnd: int) -> bool:
		if winUser.getClassName(hwnd) in (
			# NVDA Core issue 11335: Open With dialog isn't read in Windows 10 Version 2004 (May 2020 Update).
			# Note that treating the below window as a UIA window will make NVDA no longer announce "pane".
			"Shell_Flyout",
			# NVDA Core issue 14538: Windows 11 22H2 comes with a modernized Open With dialog
			# but prevents proper mouse and touch interaction.
			"Open With",
		):
			return True
		return False
