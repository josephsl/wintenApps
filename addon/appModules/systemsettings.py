# Windows 10 Settings
# Part of Windows 10 App Essentials collection
# Copyright 2016-2017 Joseph Lee, released under GPL

# Several hacks related to Settings app.

import sys
import appModuleHandler
import ui
import controlTypes
import UIAHandler
import api
from NVDAObjects.UIA import UIA, ListItem
import config

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
			# Yet another case is Devices/Bluetooth lists.
			if obj.name == "" and (obj.role in (controlTypes.ROLE_TOGGLEBUTTON, controlTypes.ROLE_COMBOBOX) and obj.UIAElement.cachedAutomationID
				or obj.role == controlTypes.ROLE_LIST and obj.UIAElement.cachedAutomationID in ("SystemSettings_Devices_AudioDeviceList_ListView", "SystemSettings_Devices_OtherDeviceList_ListView")):
				# But some combo boxes, such as Insider level combo box in Creators Update has the following problem.
				try:
					obj.name = obj.previous.name
				except AttributeError:
					obj.name = obj.parent.previous.name
			# Recognize groups of controls for contextual output (more prominent in Redstone 2).
			elif obj.UIAElement.cachedAutomationID.endswith("GroupTitleTextBlock"):
				obj.role = controlTypes.ROLE_GROUPING
			# From Redstone 1 onwards, update history shows status rather than the title.
			elif obj.role == controlTypes.ROLE_LINK and obj.UIAElement.cachedAutomationID.startswith("HistoryEvent") and obj.name != obj.previous.name:
				nameList = [obj.previous.name, obj.name]
				# But in build 16215 and later, the actual update title is next to the update success status text, so obj.previous.previous must be consulted.
				if sys.getwindowsversion().build >= 16215:
					nameList.insert(0, obj.previous.previous.name)
				obj.name = ", ".join(nameList)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# These are no longer needed with NVDA 2017.3.
		if "reportAutoSuggestionsWithSound" not in config.conf["presentation"] and isinstance(obj, UIA):
			if obj.role == controlTypes.ROLE_COMBOBOX and obj.UIAElement.getCurrentPropertyValue(UIAHandler.UIA_IsValuePatternAvailablePropertyId):
				clsList.insert(0, ComboBoxWithValuePattern)
			elif obj.role == controlTypes.ROLE_LISTITEM and isinstance(obj.parent, ComboBoxWithValuePattern):
				clsList.insert(0, ComboBoxItemWithValuePattern)

	# Live region changed event is treated as a name change for now.
	# Sometimes, the same text is announced, so consult this cache.
	_nameChangeCache = ""

	def event_nameChange(self, obj, nextHandler):
		# For now, all name change events will result in items being announced.
		if hasattr(obj, "event_liveRegionChange"):
			return
		if isinstance(obj, UIA) and obj.name != self._nameChangeCache:
			automationID = obj.UIAElement.cachedAutomationID
			try:
				# Don't repeat the fact that update download/installation is in progress if progress bar beep is on.
				if ((automationID == "SystemSettings_MusUpdate_UpdateStatus_DescriptionTextBlock" and obj.previous.value <= "0")
				# For search progress bar, do not repeat it.
				or (automationID == "ProgressBar")
				# Do not announce "result not found" error unless have to.
				or (automationID == "NoResultsFoundTextBlock" and obj.parent.UIAElement.cachedAutomationID == "StatusTextPopup")
				# But announce individual update progress in build 16215 and later.
				or ("ApplicableUpdate" in automationID and automationID.endswith("_ContextDescriptionTextBlock"))):
					# Until the spacing problem is fixed for update label...
					if "ApplicableUpdate" in automationID and automationID.endswith("_ContextDescriptionTextBlock"):
						self._nameChangeCache = " ".join([obj.parent.name, obj.name])
						ui.message(" ".join([obj.parent.name, obj.name]))
					else:
						self._nameChangeCache = obj.name
						ui.message(obj.name)
			except AttributeError:
				pass
		nextHandler()

	# Live region changed event is fired for property changes.
	event_UIA_liveRegionChanged = event_nameChange

	# And because announcing progress bar values via live region change is anoying...
	def event_liveRegionChange(self, obj, nextHandler):
		if isinstance(obj, UIA) and obj.name != self._nameChangeCache:
			automationID = obj.UIAElement.cachedAutomationID
			try:
				# Don't repeat the fact that update download/installation is in progress if progress bar beep is on.
				if ((automationID == "SystemSettings_MusUpdate_UpdateStatus_DescriptionTextBlock" and obj.previous.value <= "0")
				# For search progress bar, do not repeat it.
				or (automationID == "ProgressBar")
				# Do not announce "result not found" error unless have to.
				or (automationID == "NoResultsFoundTextBlock" and obj.parent.UIAElement.cachedAutomationID == "StatusTextPopup")
				# But announce individual update progress in build 16215 and later.
				or ("ApplicableUpdate" in automationID and automationID.endswith("_ContextDescriptionTextBlock"))):
					self._nameChangeCache = obj.name
					# Until the spacing problem is fixed for update label...
					if "ApplicableUpdate" in automationID and automationID.endswith("_ContextDescriptionTextBlock"):
						ui.message(" ".join([obj.parent.name, obj.name]))
					else:
						ui.message(obj.name)
					# And no, never allow double-speaking (an ugly hack).
					return
			except AttributeError:
				pass

	def event_UIA_controllerFor(self, obj, nextHandler):
		self._nameChangeCache = ""
		nextHandler()
