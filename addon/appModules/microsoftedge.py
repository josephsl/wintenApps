# MicrosoftEdge.py
#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2018-2019 NV Access Limited, Joseph Lee

"""appModule for Microsoft Edge main process"""

# Core Edge support provided by NvDA Core (NVDAObjects/UIA package and a dedicated app module for Edge main process)
# Provides additional enhancements.

from nvdaBuiltin.appModules.microsoftedge import *
from NVDAObjects.UIA import UIA
import controlTypes
import ui

class AppModule(AppModule):

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
