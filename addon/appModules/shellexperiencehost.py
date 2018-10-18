#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2015-2018 NV Access Limited
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
# Borrowed directly from NVDA Core (2016-2018 Joseph Lee)

from nvdaBuiltin.appModules.shellexperiencehost import *
from NVDAObjects.UIA import UIA
import controlTypes
import ui

class AppModule(AppModule):

	def event_NVDAObject_init(self, obj):
		if isinstance(obj, UIA):
			if obj.name == "" and obj.UIAElement.cachedAutomationID == "TextBoxPinEntry":
				obj.name = obj.previous.name
			# NVDA Core issue 8845: Brightness button in Action Center is a button, not a toggle button.
			if obj.UIAElement.cachedAutomationID == "Microsoft.QuickAction.Brightness":
				obj.role = controlTypes.ROLE_BUTTON

	def event_liveRegionChange(self, obj, nextHandler):
		# No, do not let Start menu size be announced.
		if isinstance(obj, UIA) and obj.UIAElement.cachedAutomationID == "FrameSizeAccessibilityField": return
		nextHandler()

	# Argh, somehow, item status property repeats when Action Center is opened more than once.
	_itemStatusMessage = None

	def event_UIA_itemStatus(self, obj, nextHandler):
		if isinstance(obj, UIA):
			itemStatus = obj.UIAElement.currentItemStatus
			# And no, I don't want to hear repetitions.
			if itemStatus != self._itemStatusMessage:
				ui.message("{0}: {1}".format(obj.name, itemStatus))
				self._itemStatusMessage = itemStatus
		nextHandler()
