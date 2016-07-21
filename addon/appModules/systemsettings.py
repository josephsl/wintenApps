# Windows 10 Settings
# Part of Windows 10 App Essentials
# Copyright 2016 Joseph Lee, released under GPL

# Several hacks related to Settings app.

import appModuleHandler
import ui
import controlTypes
from NVDAObjects.UIA import UIA

# Filter out name change event for the following objects.
noRepeatAnnouncement = ("ContentPresenter")

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		if isinstance(obj, UIA):
			# Despite repeated feedback, there's at least one unlabeled toggle button in Settings app.
			# One particular case is Settings/Update/Developer Mode with USB/LAN discovery toggle button in Redstone.
			if obj.name == "" and obj.role == controlTypes.ROLE_TOGGLEBUTTON:
				obj.name = obj.previous.name

	def event_nameChange(self, obj, nextHandler):
		# For now, all name change events will result in items being announced.
		# Prevent repeats, especially if it is part of a progress bar and for extraneous presentational objects.
		if isinstance(obj, UIA) and obj.role != controlTypes.ROLE_PROGRESSBAR and obj.UIAElement.cachedAutomationID not in noRepeatAnnouncement:
			ui.message(obj.name)
		nextHandler()
