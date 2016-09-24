# WinTenApps/hxmail.py
# Part of Windows 10 App Essentials collection
# Copyright 2016 Joseph Lee, released under GPL.

# Fixes for certain issues with Windows 10 Mail app (based on Outlook 2016).

import appModuleHandler
import controlTypes
from NVDAObjects.UIA import UIA

# Suppress read-only state and edit role announcements (quite anoying).
class MessageBody(UIA):

	# So anoying to hear the word "edit" each time one presses up or down arrow, so force a role change.
	# Official fix included as part of NVDA Core pull request #6271.
	role = controlTypes.ROLE_DOCUMENT

	def _get_states(self):
		states = super(MessageBody, self).states
		states.discard(controlTypes.STATE_READONLY)
		return states

class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# The below route is taken if one is running old NVDA Core with no Edge RS1 applied.
		if isinstance(obj, UIA) and not hasattr(UIA, "getNormalizedUIATextRangeFromElement"):
			# Very redundant to say "read-only" when we do know messages are read-only.
			if obj.UIAElement.cachedAutomationID == "Body":
					clsList.insert(0, MessageBody)
