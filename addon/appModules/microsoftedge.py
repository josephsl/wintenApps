# MicrosoftEdge.py
#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2018 NV Access Limited, Joseph Lee

"""appModule for Microsoft Edge main process"""

# Core Edge support provided by NvDA Core (NVDAObjects/UIA package and a dedicated app module for Edge main process)
# Provides additional enhancements.

from nvdaBuiltin.appModules.microsoftedge import *
from NVDAObjects.UIA import UIA, SearchField
import controlTypes
import ui
import api
from NVDAObjects.behaviors import EditableTextWithoutAutoSelectDetection, EditableTextWithAutoSelectDetection

# Specifically designed to prevent odd controller for events from being fired when moving focus away from address omnibar.
class EdgeAddressOmnibar(EditableTextWithAutoSelectDetection, SearchField, UIA):

	def event_suggestionsClosed(self):
		# Work around broken/odd controller for event implementation in Edge's address omnibar (don't even announce suggestion disappearance when focus moves).
		if self != api.getFocusObject():
			return
		super(EdgeAddressOmnibar, self).event_suggestionsClosed()


class AppModule(AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Detect selection changes in address omnibar.
		if isinstance(obj, UIA) and obj.UIAElement.cachedAutomationID == "addressEditBox":
			clsList.remove(EditableTextWithoutAutoSelectDetection)
			clsList.insert(0, EdgeAddressOmnibar)

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
