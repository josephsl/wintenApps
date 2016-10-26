# Windows 10 Settings
# Part of Windows 10 App Essentials
# Copyright 2016 Joseph Lee, released under GPL

# Several hacks related to Settings app.

import appModuleHandler
import ui
import controlTypes
from NVDAObjects.UIA import UIA

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		if isinstance(obj, UIA):
			# Despite repeated feedback, there's at least one unlabeled toggle button in Settings app.
			# One particular case is Settings/Update/Developer Mode with USB/LAN discovery toggle button in Redstone.
			if obj.name == "" and obj.role == controlTypes.ROLE_TOGGLEBUTTON:
				obj.name = obj.previous.name

	# Live region changed event is treated as a name change for now.
	# Sometimes, the same text is announced, so consult this cache.
	_nameChangeCache = ""

	def event_nameChange(self, obj, nextHandler):
		# For now, all name change events will result in items being announced.
		if isinstance(obj, UIA) and obj.name != self._nameChangeCache:
			automationID = obj.UIAElement.cachedAutomationID
			try:
				# Don't repeat the fact that update download/installation is in progress if progress bar beep is on.
				if ((automationID == "SystemSettings_MusUpdate_UpdateStatus_DescriptionTextBlock" and obj.previous.value <= "0")
				# For search progress bar, do not repeat it.
				or (automationID == "ProgressBar")
				# Do not announce "result not found" error unless have to.
				or (automationID == "NoResultsFoundTextBlock" and obj.parent.UIAElement.cachedAutomationID == "StatusTextPopup")):
					self._nameChangeCache = obj.name
					ui.message(obj.name)
			except AttributeError:
				pass
		nextHandler()

	def event_UIA_controllerFor(self, obj, nextHandler):
		self._nameChangeCache = ""
		nextHandler()
