#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2015-2017 NV Access Limited
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
# Borrowed directly from NVDA Core (2016-2017 Joseph Lee)

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

	# Until fixed in Fall Creators Update stable build...
	def script_tab(self, gesture):
		# In build 162xx, pressing TAB while Action Center is empty gives no feedback whatsoever.
		gesture.send()
		import sys, api
		if sys.getwindowsversion().build > 15063:
			focus = api.getFocusObject()
			if isinstance(focus, UIA):
				automationID = focus.UIAElement.cachedAutomationID
				if automationID == "ExpandCollapseButton":
					notificationList = focus.previous
				elif automationID.startswith("Microsoft.QuickAction"):
					notificationList = focus.parent.parent.parent.previous.previous
				if isinstance(notificationList, UIA) and notificationList.UIAElement.cachedAutomationID == "MainListView" and notificationList.childCount == 0:
					if automationID == "ExpandCollapseButton":
						focus.simpleNext.setFocus()
					elif automationID.startswith("Microsoft.QuickAction"):
						focus.parent.parent.parent.previous.setFocus()

	__gestures={
		"kb:tab":"tab",
		"kb:shift+tab":"tab",
	}
