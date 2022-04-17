# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2019-2022 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Originally copyright 2016-2021 Joseph Lee, released under GPL

# Several hacks related to Settings app, some of which are part of NVDA Core.

# Extends NVDA Core's System Settings app module.
from nvdaBuiltin.appModules.systemsettings import AppModule
import controlTypes
import winVersion
import speech
from NVDAObjects.UIA import UIA


# App module class comes from built-in System Settings app module but Mypy doesn't know that.
class AppModule(AppModule):  # type: ignore[no-redef]

	def event_NVDAObject_init(self, obj):
		if not isinstance(obj, UIA):
			return
		# Perform different things based on Windows releases series.
		# Windows 10 including Server 2022
		if winVersion.getWinVer() < winVersion.WIN11:
			# Workarounds for Windows Update links found in Windows 10.
			if obj.role == controlTypes.Role.LINK:
				nameList = [obj.name]
				# Since Windows 10 1709, latest feature update entry in update history adds "what's new" link.
				# Therefore fetch feature update title located two objects down.
				# Update history has changed completely in Windows 11.
				if obj.UIAAutomationId.startswith("HistoryEvent"):
					eventID = obj.UIAAutomationId.split("_")[0]
					possibleFeatureUpdateText = obj.previous.previous
					# This Automation Id may change in a future Windows release.
					if possibleFeatureUpdateText.UIAAutomationId == "_".join([eventID, "TitleTextBlock"]):
						nameList.insert(0, possibleFeatureUpdateText.name)
				# In later revisions of Windows 10 1803 and later, optional update download link is provided
				# and is initially called "download and install now", thus add the optional update title as well.
				elif obj.UIAAutomationId == "SystemSettings_MusUpdate_SeekerUpdateUX_HyperlinkButton":
					# Unconditionally locate the new optional update title, skipping the link description.
					# For feature updates, update title is next to description text,
					# and description text is next to the download link itself.
					# For optional cumulative updates, the actual update title is next to this link,
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
			# Developer mode label in Windows 10 2004/20H2/21H1/21H2.
			# The label itself is the name of the previous object.
			# Resolved in Windows 11.
			elif obj.name == "SystemSettings_Developer_Mode_Advanced_NarratorText":
				obj.name = obj.previous.name
		# Windows 11
		else:
			# Announce optional updates in Windows 11.
			# Same as Windows 10 except it uses a different Automation Id.
			if obj.UIAAutomationId == "SystemSettings_MusUpdate_SeekerUpdateUX_Button":
				obj.name = ", ".join([obj.previous.previous.name, obj.name])
			# Windows 11's breadcrumb bar item uses a custom localized control type text.
			# Although it is recognized as a heading, override role text to communicate what it actually is.
			# This allows item label to be kept intact.
			elif obj.UIAElement.cachedClassName.endswith("BreadcrumbBarItem"):
				obj.roleText = obj.UIAElement.currentLocalizedControlType

	# Sometimes, the same text is announced, so consult this cache.
	_nameChangeCache: str = ""

	def event_liveRegionChange(self, obj, nextHandler):
		# Only enter the below route if this is Windows 10.
		if isinstance(obj, UIA) and winVersion.getWinVer() < winVersion.WIN11:
			# Except for specific cases, announce all live regions.
			# Announce individual update progress in build 16215 and later preferably only once per update stage.
			if "ApplicableUpdate" in obj.UIAAutomationId:
				# Do not announce status text itself.
				if obj.UIAAutomationId.endswith("_ContextDescriptionTextBlock"):
					return
				# Update title repeats while the update is downloaded and installed.
				if obj.UIAAutomationId.endswith("_DescriptionTextBlock"):
					# #71: NVDA is told to announce live regions to the end by default,
					# which results in screen content and speech getting out of sync.
					# However do not cut off other live regions when action button appears next to updates list
					# which is the sibling of the grandparent object (actual updates list element).
					# Update action button appears if the system is up to date or an action is required.
					if "UpdateActionButton" not in obj.parent.parent.next.UIAAutomationId:
						speech.cancelSpeech()
					if obj.name and obj.name == self._nameChangeCache:
						return
				self._nameChangeCache = obj.name
		nextHandler()

	def event_appModule_loseFocus(self):
		self._nameChangeCache = ""
