# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2011-2023 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

from nvdaBuiltin.appModules.openwith import AppModule
import winUser


class AppModule(AppModule):

	def isGoodUIAWindow(self, hwnd):
		# NVDA Core issue 11335: Open With dialog isn't read in Windows 10 Version 2004 (May 2020 Update).
		# Note that treating the below window as a UIA window will make NVDA no longer announce "pane".
		# Add support for Windows 11 Version 22H2 as well.
		if winUser.getClassName(hwnd) in (
			"Shell_Flyout",  # Windows 10
			"Open With",  # Windows 11 22H2
		):
			return True
		return False
