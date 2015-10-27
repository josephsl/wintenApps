# Joseph Lee
# Windows 10 contorls repository
# Copyright 2015 Joseph Lee, released under GPL.

# Adds handlers for vairous UIA controls found in Windows 10.

import globalPluginHandler
import controlTypes
from NVDAObjects.UIA import UIA
import api
import speech
import addonHandler
addonHandler.initTranslation()

# Looping selectors are used in apps such as Alarms and Clock and Windows Update to select time values.
class LoopingSelectorItem(UIA):

	def event_UIA_elementSelected(self):
		speech.cancelSpeech()
		api.setNavigatorObject(self)
		self.reportFocus()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# NVDA Core ticket 5231: Announce values in time pickers.
		if isinstance(obj, UIA):
			if obj.role==controlTypes.ROLE_LISTITEM and obj.UIAElement.cachedClassName == "LoopingSelectorItem":
				clsList.append(LoopingSelectorItem)
