# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2019-2021 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for modern Settings app (aka Immersive Control Panel)."""

# Originally copyright 2016-2021 Joseph Lee, released under GPL
# Several hacks related to Settings app, some of which are part of NVDA Core.

# Help Mypy and other static checkers for a time by importing uppercase versions of built-in types.
from typing import Any
# See the above note as to why the below procedure must be done.
from nvdaBuiltin.appModules.systemsettings import *  # NOQA: F403
import ui
import controlTypes
from NVDAObjects.UIA import UIA


# Controls with XAML class names as labels (SystemSettings_*).
# Thankfully labels are previous object names.
XAML_CLASS_ELEMENT_NAMES = [
	# Developer mode label in Windows 10 2004/20H2/21H1/21H2.
	# Resolved in Windows 11.
	"SystemSettings_Developer_Mode_Advanced_NarratorText",
	# Microsoft Account sign-in options in Windows 11.
	# Windows Hello recommendation.
	"SystemSettings_Users_PasswordLessSignInDesktopDescription",
	# Complete setup with account info after an update or restart.
	"SystemSettings_Users_AutomaticSignOnLock_UpdateV2"
]


# Support control types refactor (both before (2021.1) and after (2021.2) for a time).
try:
	ROLE_LINK = controlTypes.Role.LINK
	ROLE_LISTITEM = controlTypes.Role.LISTITEM
	ROLE_STATICTEXT = controlTypes.Role.STATICTEXT
	ROLE_GROUPING = controlTypes.Role.GROUPING
except AttributeError:
	ROLE_LINK = controlTypes.ROLE_LINK
	ROLE_LISTITEM = controlTypes.ROLE_LISTITEM
	ROLE_STATICTEXT = controlTypes.ROLE_STATICTEXT
	ROLE_GROUPING = controlTypes.ROLE_GROUPING


# App module class comes from built-in System Settings app module but Mypy doesn't know that.
# Also linters such as Flake8 should ignore this.
class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405

	def event_NVDAObject_init(self, obj):
		if isinstance(obj, UIA):
			# From Windows 10 1607 onwards, update history shows status rather than the title.
			# In build 16232, the title is shown but not the status,
			# so include this for sake of backward compatibility.
			# In later revisions of Windows 10 1803 and later, feature update download link is provided
			# and is initially called "download and install now", thus add the feature update title as well.
			if obj.role == ROLE_LINK:
				nameList = [obj.name]
				if obj.UIAAutomationId.startswith("HistoryEvent") and obj.name != obj.previous.name:
					# Add the status text in 1709 and later.
					# But since 16251, a "what's new" link has been added for feature updates,
					# so consult two previous objects.
					eventID = obj.UIAAutomationId.split("_")[0]
					possibleFeatureUpdateText = obj.previous.previous
					# This Automation Id may change in a future Windows release.
					if possibleFeatureUpdateText.UIAAutomationId == "_".join([eventID, "TitleTextBlock"]):
						nameList.insert(0, obj.previous.name)
						nameList.insert(0, possibleFeatureUpdateText.name)
					else:
						nameList.append(obj.next.name)
				elif obj.UIAAutomationId == "SystemSettings_MusUpdate_SeekerUpdateUX_HyperlinkButton":
					# Unconditionally locate the new feature update title, skipping the link description.
					# Note that for optional cumulative updates, the actual update title is next to this link,
					# so one must fetch all of these.
					# Ignore all this if there is "View all optional updates" link,
					# seen when there is one or more driver updates on top of feature/quality updates.
					if obj.previous.UIAElement.cachedClassName == "TextBlock":
						nameList.insert(0, obj.previous.name)
						nameList.insert(0, obj.previous.previous.name)
				obj.name = ", ".join(nameList)
			# In some cases, Active Directory style name is the name of the window,
			# so tell NVDA to use something more meaningful.
			elif obj.name == "CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington, C=US":
				obj.name = obj.firstChild.name
			# Some elements use XAML class name as their label (SystemSettings_*).
			# Thankfully labels are next door to these, specifically previous.name.
			elif obj.name in XAML_CLASS_ELEMENT_NAMES:
				obj.name = obj.previous.name
			# Some XAML controls are named SystemSettings.ViewModel.SettingEntry.
			# For list items, simple children records actual label.
			# For themes list, first child (grouping) holds the theme label.
			elif obj.name == "SystemSettings.ViewModel.SettingEntry":
				if obj.role == ROLE_LISTITEM:
					obj.name = "; ".join(
						[child.name for child in obj.children if child.role in (ROLE_STATICTEXT, ROLE_GROUPING)]
					)

	# Sometimes, the same text is announced, so consult this cache.
	_nameChangeCache: str = ""

	def announceLiveRegion(self, obj: Any, automationId: str) -> bool:
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

	def event_appModule_loseFocus(self):
		self._nameChangeCache = ""
