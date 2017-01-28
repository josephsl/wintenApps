# Windows 10 Settings
# Part of Windows 10 App Essentials collection
# Copyright 2016-2017 Joseph Lee, released under GPL

# Several hacks related to Settings app.

import appModuleHandler
import ui
import controlTypes
from NVDAObjects.UIA import UIA

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		if isinstance(obj, UIA):
			# Despite repeated feedback, there's at least one unlabeled toggle button in Settings app.
			# One particular case is Settings/Update/Developer Mode with USB/LAN discovery toggle button in Redstone (fixed in build 14986).
			if obj.name == "" and obj.role == controlTypes.ROLE_TOGGLEBUTTON:
				obj.name = obj.previous.name
			# Recognize groups of controls for contextual output (more prominent in Redstone 2).
			elif obj.UIAElement.cachedAutomationID.endswith("GroupTitleTextBlock"):
				obj.role = controlTypes.ROLE_GROUPING
			# Build 15019: Game bar shortcut fields are not labeled.)
			# Description and default shortcuts are next to each other.
			elif obj.name == "" and obj.UIAElement.cachedAutomationID == "ShortcutTextBox":
				# Add a colon just for output.
				obj.name = ": ".join([obj.previous.previous.name, obj.previous.name])

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
