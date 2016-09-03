# WinTenApps/hxmail.py
# Part of Windows 10 App Essentials collection
# Copyright 2016 Joseph Lee, released under GPL.

# Fixes for certain issues with Windows 10 Mail app (based on Outlook 2016).

import appModuleHandler
import controlTypes
from NVDAObjects.UIA import UIA

# Suppress read-only state announcement (quite anoying).
class MessageBody(UIA):

	def _get_states(self):
		states = super(MessageBody, self).states
		states.discard(controlTypes.STATE_READONLY)
		return states

class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			# Very redundant to say "read-only" when we do know messages are read-only.
			if obj.UIAElement.cachedAutomationID == "Body":
					clsList.insert(0, MessageBody)
