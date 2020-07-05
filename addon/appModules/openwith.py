#appModules/openWith.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2011 NVDA Contributors <http://www.nvda-project.org/>
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

from nvdaBuiltin.appModules.openwith import *
import winUser
import winVersion


class AppModule(AppModule):

	def isGoodUIAWindow(self, hwnd):
		# NVDA Core issue 11335: Open With dialog isn't read in version 2004.
		# For maximum compatibility, use build number directly because NVDA 2020.1 does not recognize build 19041 as Version 2004.
		if winVersion.winVersion.build >= 19041 and winUser.getClassName(hwnd) == "Shell_Flyout":
			return True
		return False
