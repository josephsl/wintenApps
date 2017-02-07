# Windows 10 Settings
# Part of Windows 10 App Essentials collection
# Copyright 2016-2017 Joseph Lee, released under GPL

# Several hacks related to Settings app.

import appModuleHandler
import ui
import controlTypes
import UIAHandler
import api
from NVDAObjects.UIA import UIA, ListItem

# Some Settings app combo boxes do expose value selection pattern but requires focus to be reminded of value changes.

# A placeholder combo box object with value pattern (for some settings app combo boxes).
class ComboBoxWithValuePattern(UIA):
	pass

class ComboBoxItemWithValuePattern(ListItem):

	def event_stateChange(self):
		# Borrowed from NVDA Core.
		if not self.hasFocus:
			parent = self.parent
			focus=api.getFocusObject()
			if parent and isinstance(parent, ComboBoxWithValuePattern) and parent==focus: 
				# Sometimes, focus needs to be reminded that state change has occured.
				focus.event_valueChange()
		super(ComboBoxItemWithValuePattern, self).event_stateChange()

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		if isinstance(obj, UIA):
			# Despite repeated feedback, there's at least one unlabeled toggle button in Settings app.
			# One particular case is Settings/Update/Developer Mode with USB/LAN discovery toggle button in Redstone (fixed in build 14986).
			# Another case is with various combo boxes in Redstone 2 with no labels.
			if obj.name == "" and obj.role in (controlTypes.ROLE_TOGGLEBUTTON, controlTypes.ROLE_COMBOBOX) and obj.UIAElement.cachedAutomationID:
				obj.name = obj.previous.name
			# Recognize groups of controls for contextual output (more prominent in Redstone 2).
			elif obj.UIAElement.cachedAutomationID.endswith("GroupTitleTextBlock"):
				obj.role = controlTypes.ROLE_GROUPING
			# Build 15019: Game bar shortcut fields are not labeled.)
			# Description and default shortcuts are next to each other.
			elif obj.name == "" and obj.UIAElement.cachedAutomationID == "ShortcutTextBox":
				# Add a colon just for output.
				obj.name = ": ".join([obj.previous.previous.name, obj.previous.name])

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			if obj.role == controlTypes.ROLE_COMBOBOX and obj.UIAElement.getCurrentPropertyValue(UIAHandler.UIA_IsValuePatternAvailablePropertyId):
				clsList.insert(0, ComboBoxWithValuePattern)
			elif obj.role == controlTypes.ROLE_LISTITEM and isinstance(obj.parent, ComboBoxWithValuePattern):
				clsList.insert(0, ComboBoxItemWithValuePattern)

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
