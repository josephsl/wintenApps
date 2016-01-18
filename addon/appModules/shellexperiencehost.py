#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2015 NV Access Limited
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

# Borrowed directly from NVDA Core (2016 Joseph Lee)

import appModuleHandler
from NVDAObjects.IAccessible import IAccessible, ContentGenericClient
from NVDAObjects.UIA import UIA
import controlTypes

# Submenus in Start menu tiles context menu are not recognized as such (at least in WinTen Version 1511).
class TileSubMenu(UIA):

	def _get_states(self):
		# Borrowed from NVDA Core issue 5178 code (fixed provided by the same author).
		states = super(TileSubMenu, self).states
		states.add(controlTypes.STATE_HASPOPUP)
		return states

class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self,obj,clsList):
		if isinstance(obj, IAccessible):
			try:
				# #5288: Never use ContentGenericClient, as this uses displayModel
				# which will freeze if the process is suspended.
				clsList.remove(ContentGenericClient)
			except ValueError:
				pass
		elif isinstance(obj, UIA):
			if obj.UIAElement.cachedClassName == "MenuFlyoutSubItem":
				clsList.insert(0, TileSubMenu)

