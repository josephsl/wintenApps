#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2015-2019 NV Access Limited, Joseph Lee
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
# Borrowed directly from NVDA Core (2016-2018 Joseph Lee)

from nvdaBuiltin.appModules.shellexperiencehost import *
from NVDAObjects.UIA import UIA
import controlTypes
import ui

class ActionCenterToggleButton(UIA):

	def _get_value(self):
		return self.UIAElement.currentItemStatus

	def event_valueChange(self):
		self.event_UIA_itemStatus()

	# Somehow, item status property repeats when Action Center is opened more than once.
	_itemStatusMessageCache = None

	def event_UIA_itemStatus(self):
		# Do not repeat item status multiple times.
		currentItemStatus = self.value
		if currentItemStatus and currentItemStatus != self._itemStatusMessageCache:
			ui.message(currentItemStatus)
			self._itemStatusMessageCache = currentItemStatus


class AppModule(AppModule):

	def event_NVDAObject_init(self, obj):
		if isinstance(obj, UIA):
			if obj.name == "" and obj.UIAElement.cachedAutomationID == "TextBoxPinEntry":
				obj.name = obj.previous.name
			# NVDA Core issue 8845: Brightness button in Action Center is a button, not a toggle button.
			# Brightness control is now a slider in build 18277.
			if obj.UIAElement.cachedAutomationID == "Microsoft.QuickAction.Brightness":
				obj.role = controlTypes.ROLE_BUTTON
				obj.states.discard(controlTypes.STATE_CHECKABLE)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA) and obj.role == controlTypes.ROLE_TOGGLEBUTTON and obj.UIAElement.cachedClassName == "ToggleButton":
			clsList.insert(0, ActionCenterToggleButton)
