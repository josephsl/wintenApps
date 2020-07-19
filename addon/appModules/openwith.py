# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2011-2020 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

from nvdaBuiltin.appModules.openwith import *
import winUser


class AppModule(AppModule):

	def isGoodUIAWindow(self, hwnd):
		# NVDA Core issue 11335: Open With dialog isn't read in version 2004.
		# For consistency, apply this fix to earlier Windows 10 releases.
		if winUser.getClassName(hwnd) == "Shell_Flyout":
			return True
		return False
