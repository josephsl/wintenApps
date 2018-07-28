#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2015-2018 NV Access Limited
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
# Borrowed directly from NVDA Core (2016-2018 Joseph Lee)

from nvdaBuiltin.appModules.shellexperiencehost import *
from NVDAObjects.UIA import UIA

class AppModule(AppModule):

	def event_NVDAObject_init(self, obj):
		if isinstance(obj, UIA):
			if obj.name == "" and obj.UIAElement.cachedAutomationID == "TextBoxPinEntry":
				obj.name = obj.previous.name

	def event_liveRegionChange(self, obj, nextHandler):
		# No, do not let Start menu size be announced.
		if isinstance(obj, UIA) and obj.UIAElement.cachedAutomationID == "FrameSizeAccessibilityField": return
		nextHandler()
