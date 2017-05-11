# WinTenApps/hxcalendarappimm.py
# Part of Windows 10 App Essentials collection
# Copyright 2016 Joseph Lee, released under GPL.

# Fixes for certain issues with Windows 10 Calendar app (based on Outlook 2016).

import appModuleHandler
import controlTypes
from NVDAObjects.UIA import UIA

# Suppress read-only state announcement (quite anoying).
class AppointmentSubject(UIA):

	def _get_states(self):
		states = super(AppointmentSubject, self).states
		states.discard(controlTypes.STATE_READONLY)
		return states

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		# It is quite anoying to hear the same text for name and description, so forget the description.
		if obj.name != "" and obj.description == obj.name:
			obj.description = None

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			# Very redundant to say "read-only" when we do know messages are read-only.
			if obj.UIAElement.cachedAutomationID == "QuickItemSubject":
				clsList.insert(0, AppointmentSubject)
