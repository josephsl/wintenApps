# Windows 10 Settings
# Part of Windows 10 App Essentials collection
# Copyright 2016-2018 Joseph Lee, released under GPL

# Several hacks related to Settings app.

import sys
import appModuleHandler
import ui
import controlTypes
from NVDAObjects.UIA import UIA
from NVDAObjects.behaviors import ProgressBar

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
			# No longer necessary in Version 1803 and later because it is now a heading.
			elif obj.UIAElement.cachedAutomationID.endswith("GroupTitleTextBlock") and sys.getwindowsversion().build < 17134:
				obj.role = controlTypes.ROLE_GROUPING
			# From Redstone 1 onwards, update history shows status rather than the title.
			# In build 16232, the title is shown but not the status, so include this for sake of backward compatibility.
			elif obj.role == controlTypes.ROLE_LINK and obj.UIAElement.cachedAutomationID.startswith("HistoryEvent") and obj.name != obj.previous.name:
				nameList = [obj.name]
				# Add the status text in 1709 and later.
				# But since 16251, a "what's new" link has been added for feature updates, so consult two previous objects.
				automationID = obj.UIAElement.cachedAutomationID
				eventID = automationID.split("_")[0]
				possibleFeatureUpdateText = obj.previous.previous
				# This automation ID may change in a future Windows 10 release.
				if possibleFeatureUpdateText.UIAElement.cachedAutomationID == "_".join([eventID, "TitleTextBlock"]):
					nameList.insert(0, obj.previous.name)
					nameList.insert(0, possibleFeatureUpdateText.name)
				else:
					nameList.append(obj.next.name)
				obj.name = ", ".join(nameList)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# In build 17035, Settings/System/Sound has been added, but has an anoying volume progress bar.
		# Still not fixed in build 17115, now the volume slider is another element.
		if isinstance(obj, UIA) and obj.UIAElement.cachedClassName == "ProgressBar" and isinstance(obj.next, UIA):
			if obj.next.UIAElement.cachedAutomationID.startswith("SystemSettings_Audio_Output_VolumeValue_") or obj.simplePrevious.UIAElement.cachedAutomationID.startswith("SystemSettings_Audio_Input_VolumeValue_"):
				try:
					clsList.remove(ProgressBar)
				except ValueError:
					pass

	# Sometimes, the same text is announced, so consult this cache.
	_nameChangeCache = ""

	def announceLiveRegion(self, obj, automationID):
		# Announce update status no matter what it is.
		# This is more relevant in build 17063 and later where a subtitle has been added.
		if "MusUpdate_UpdateStatus" in automationID:
			# Don't repeat the fact that update download/installation is in progress if progress bar beep is on.
			return False if automationID == "SystemSettings_MusUpdate_UpdateStatus_DescriptionTextBlock" and obj.previous.value > "0" else True
		else:
			# For search progress bar, do not repeat it.
			return ((automationID == "ProgressBar")
			# Do not announce "result not found" error unless have to.
			or (automationID == "NoResultsFoundTextBlock" and obj.parent.UIAElement.cachedAutomationID == "StatusTextPopup")
			# But announce individual update progress in build 16215 and later.
			or ("ApplicableUpdate" in automationID and automationID.endswith("_ContextDescriptionTextBlock"))
			# Don't forget update error text.
			or (automationID in ("SystemSettings_MusUpdate_UpdateError_DescriptionTextBlock", "SystemSettings_MusUpdate_PayloadErrorDetails_HolisticErrorDescriptionTextBlock")))

	def event_liveRegionChange(self, obj, nextHandler):
		if isinstance(obj, UIA) and obj.name and obj.name != self._nameChangeCache:
			automationID = obj.UIAElement.cachedAutomationID
			try:
				if self.announceLiveRegion(obj, automationID):
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
