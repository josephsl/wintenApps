# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2019 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for Windows 10 Settings app (aka Immersive Control Panel)."""

# Originally copyright 2016-2019 Joseph Lee, released under GPL
# Several hacks related to Settings app, some of which are part of NVDA Core.

from nvdaBuiltin.appModules.systemsettings import *
import ui
import controlTypes
from NVDAObjects.UIA import ComboBoxWithoutValuePattern
import winVersion


class AppModule(AppModule):

	def event_NVDAObject_init(self, obj):
		if isinstance(obj, UIA):
			# From Redstone 1 onwards, update history shows status rather than the title.
			# In build 16232, the title is shown but not the status,
			# so include this for sake of backward compatibility.
			# In later revisions of build 17134 and later, feature update download link is provided
			# and is initially called "download and install now", thus add the feature update title as well.
			if obj.role == controlTypes.ROLE_LINK:
				nameList = [obj.name]
				if obj.UIAAutomationId.startswith("HistoryEvent") and obj.name != obj.previous.name:
					# Add the status text in 1709 and later.
					# But since 16251, a "what's new" link has been added for feature updates,
					# so consult two previous objects.
					eventID = obj.UIAAutomationId.split("_")[0]
					possibleFeatureUpdateText = obj.previous.previous
					# This automation ID may change in a future Windows 10 release.
					if possibleFeatureUpdateText.UIAAutomationId == "_".join([eventID, "TitleTextBlock"]):
						nameList.insert(0, obj.previous.name)
						nameList.insert(0, possibleFeatureUpdateText.name)
					else:
						nameList.append(obj.next.name)
				elif obj.UIAAutomationId == "SystemSettings_MusUpdate_SeekerUpdateUX_HyperlinkButton":
					# Unconditionally locate the new feature update title, skipping the link description.
					# Note that for optional cumulative updates, the actual update title is next to this link,
					# so one must fetch all of these.
					nameList.insert(0, obj.previous.name)
					nameList.insert(0, obj.previous.previous.name)
				obj.name = ", ".join(nameList)
			# In some cases, Active Directory style name is the name of the window,
			# so tell NVDA to use something more meaningful.
			elif obj.name == "CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington, C=US":
				obj.name = obj.firstChild.name
			# Developer mode label in Version 2004 and 20H2/2009 is wrong.
			# It shows class name rather than the actual label.
			# 2020 releases are build 19041 and an enablement package (no for 2004, yes for 20H2/2009).
			# This is resolved in build 19536 and later.
			elif obj.name == "SystemSettings_Developer_Mode_Advanced_NarratorText":
				obj.name = obj.previous.name

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Although there will be duplication below, call super method first.
		super(AppModule, self).chooseNVDAObjectOverlayClasses(obj, clsList)
		if isinstance(obj, UIA):
			# In 18200 series and above, various Storage Sense option combo boxes have
			# values but are not exposed as such, so treated it as combo box without value pattern.
			# Resolved in 18800 and above, which means Version 1903 (build 18362)
			# and 1909 (build 18363) will still carry this problem.
			# Note that 1909 is still 18362 internally, so just check platform version tuple (Python 3.7 and later).
			if (
				winVersion.winVersion.platform_version == (10, 0, 18362)
				and obj.role == controlTypes.ROLE_COMBOBOX
				and obj.UIAAutomationId.startswith("SystemSettings_StorageSense_SmartPolicy_")
			):
				clsList.insert(0, ComboBoxWithoutValuePattern)

	# Sometimes, the same text is announced, so consult this cache.
	_nameChangeCache = ""

	def announceLiveRegion(self, obj, automationId):
		# Announce update status no matter what it is.
		# This is more relevant in build 17063 and later where a subtitle has been added.
		if "MusUpdate_UpdateStatus" in automationId:
			# Don't repeat the fact that update download/installation is in progress if progress bar beep is on.
			return not (
				automationId == "SystemSettings_MusUpdate_UpdateStatus_DescriptionTextBlock"
				and obj.previous.value and obj.previous.value > "0"
			)
		# Except for specific cases, announce all live regions.
		if (
			# Do not announce "result not found" error unless have to.
			(
				automationId == "NoResultsFoundTextBlock"
				and obj.parent.UIAAutomationId != "StatusTextPopup"
			)
			# Announce individual update progress in build 16215 and later preferably only once per update stage.
			or ("ApplicableUpdate" in automationId and not automationId.endswith("_ContextDescriptionTextBlock"))
		):
			return False
		return True

	def event_liveRegionChange(self, obj, nextHandler):
		if isinstance(obj, UIA) and obj.name and obj.name != self._nameChangeCache:
			automationId = obj.UIAAutomationId
			try:
				if self.announceLiveRegion(obj, automationId):
					self._nameChangeCache = obj.name
					# Until the spacing problem is fixed for update label...
					if "ApplicableUpdate" in automationId and automationId.endswith("_ContextDescriptionTextBlock"):
						ui.message(" ".join([obj.parent.name, obj.name]))
					else:
						ui.message(obj.name)
					# And no, never allow double-speaking (an ugly hack).
					return
			except AttributeError:
				pass

	def event_nameChange(self, obj, nextHandler):
		if isinstance(obj, UIA):
			# Storage/disk cleanup progress bar raises name change event.
			if (
				# Because "Purging:" is announced multiple times,
				# coerce this to live region change event, which does handle this case.
				obj.UIAAutomationId == "SystemSettings_StorageSense_TemporaryFiles_InstallationProgressBar"
				# Announce result text for Storage Sense/cleanup.
				or obj.UIAAutomationId.startswith("SystemSettings_StorageSense_SmartPolicy_ExecuteNow")
			):
				self.event_liveRegionChange(obj, nextHandler)
		nextHandler()

	def event_UIA_controllerFor(self, obj, nextHandler):
		self._nameChangeCache = ""
		nextHandler()
