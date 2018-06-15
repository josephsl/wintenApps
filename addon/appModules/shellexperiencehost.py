#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2015-2018 NV Access Limited
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
# Borrowed directly from NVDA Core (2016-2018 Joseph Lee)

import appModuleHandler
from NVDAObjects.IAccessible import IAccessible, ContentGenericClient
from NVDAObjects.UIA import UIA
import controlTypes

# Submenus in Start menu tiles context menu are not recognized as such (at least in WinTen Version 1511).
# Also, make sure to get rid of position info announcement, as it's quite anoying.
class TileSubMenu(UIA):

	def _get_states(self):
		# Borrowed from NVDA Core issue 5178 code (fixed provided by the same author).
		states = super(TileSubMenu, self).states
		states.add(controlTypes.STATE_HASPOPUP)
		return states

	def _get_positionInfo(self):
		return {}

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

	def event_NVDAObject_init(self, obj):
		if isinstance(obj, UIA):
			if obj.name == "" and obj.UIAElement.cachedAutomationID == "TextBoxPinEntry":
				obj.name = obj.previous.name

	def event_liveRegionChange(self, obj, nextHandler):
		# No, do not let Start menu size be announced.
		if isinstance(obj, UIA) and obj.UIAElement.cachedAutomationID == "FrameSizeAccessibilityField": return
		nextHandler()
