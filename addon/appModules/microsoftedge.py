# MicrosoftEdge.py
# Part of Windows 10 App Essentials collection
# Copyright 2016 Joseph Lee, released under GPL

# Core Edge support provided by NvDA Core (NVDAObjects/UIA package)
# Provides additional enhancements.

import appModuleHandler
from NVDAObjects.UIA import UIA
import controlTypes
import ui


class AppModule(appModuleHandler.AppModule):

	def event_nameChange(self, obj, nextHandler):
		# Some objects do raise live region change event as well as name change.
		if isinstance(obj, UIA) and not hasattr(obj, "event_liveRegionChange"):
			# Notifications such as file download prompt.
			if obj.role == controlTypes.ROLE_STATICTEXT and obj.parent.UIAElement.cachedClassName == "NotificationBar":
				ui.message(obj.name)
			# Accessibility message alerts.
			elif obj.role == controlTypes.ROLE_ALERT and obj.UIAElement.cachedAutomationID == "a11y-announcements-message":
				ui.message(obj.firstChild.name)
		nextHandler()

	event_UIA_liveRegionChanged = event_nameChange
	# Live region change is part of NVDA 2017.3, so try catching this as well.
	def event_liveRegionChange(self, obj, nextHandler):
		if isinstance(obj, UIA):
			# Accessibility message alerts.
			# Return immediately after doing the following, otherwise double spekaing results.
			if obj.role == controlTypes.ROLE_ALERT and obj.UIAElement.cachedAutomationID == "a11y-announcements-message":
				ui.message(obj.firstChild.name)
				return
		nextHandler()
