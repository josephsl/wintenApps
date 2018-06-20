# MicrosoftEdge.py
#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
# Copyright 2016-2018 Joseph Lee, released under GPL
# Additional: copyright (C) 2018 NV Access Limited, Joseph Lee

# Core Edge support provided by NvDA Core (NVDAObjects/UIA package)
# Provides additional enhancements.

import appModuleHandler
from NVDAObjects.UIA import UIA
import controlTypes
import ui


class AppModule(appModuleHandler.AppModule):

	def event_liveRegionChange(self, obj, nextHandler):
		if isinstance(obj, UIA):
			# Accessibility message alerts.
			# For some messages, system alert event is raised along with this event, so return.
			if obj.role == controlTypes.ROLE_ALERT and obj.UIAElement.cachedAutomationID == "a11y-announcements-message":
				return
		nextHandler()

	# For message alerts, system alert and live region changed are fired at the same time.
	def event_UIA_systemAlert(self, obj, nextHandler):
		if isinstance(obj, UIA):
			if obj.role == controlTypes.ROLE_ALERT and obj.UIAElement.cachedAutomationID == "a11y-announcements-message":
				# Mick Curran says use last child in case a series of live texts are part of this control.
				ui.message(obj.lastChild.name)
		nextHandler()

	def event_UIA_notification(self, obj, nextHandler, displayString=None, activityId=None, **kwargs):
		# NVDA Core issue 8423: even though content process is focused, notifications are fired by main Edge process.
		# The base object will simply ignore this, so notifications must be announced here and no more.
		ui.message(displayString)
