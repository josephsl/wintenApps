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


# NVDA Core doesn't know about Windows 11 22H2 yet.
WIN11_22H2 = winVersion.WinVersion(major=10, minor=0, build=22621, releaseName="Windows 11 22H2")


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
				# Latest feature update entry in update history adds "what's new" link.
				# Therefore fetch feature update title located two objects down.
				# Update history has changed completely in Windows 11.
				if obj.UIAAutomationId.startswith("HistoryEvent"):
					eventID = obj.UIAAutomationId.split("_")[0]
					possibleFeatureUpdateText = obj.previous.previous
					# Automation Id is of the form "HistoryEvent_eventID_TitleTextBlock".
					if possibleFeatureUpdateText.UIAAutomationId == "_".join([eventID, "TitleTextBlock"]):
						nameList.insert(0, possibleFeatureUpdateText.name)
				# Download link for an optional update is provided when preview updates are released.
				# It is initially called "download and install now", thus add the optional update title as well.
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
			# Developer mode label in Windows 10 Vibranium (2004 and later).
			# The label itself is the name of the previous object.
			# Resolved in Windows 11 and Server 2022.
			elif obj.name == "SystemSettings_Developer_Mode_Advanced_NarratorText":
				obj.name = obj.previous.name
		# Windows 11
		else:
			# Announce optional updates in Windows 11.
			# Same as Windows 10 except it uses different Automation Id's.
			if obj.UIAAutomationId in (
				"SystemSettings_MusUpdate_SeekerUpdateUX_Button",
				"SystemSettings_MusUpdate_SeekerUpdateUX2_Button"
			):
				obj.name = " ".join([obj.previous.previous.name, obj.name])
			# Windows 11's breadcrumb bar item uses a custom localized control type text.
			# Although it is recognized as a heading, override role text to communicate what it actually is.
			# This allows item label to be kept intact.
			elif obj.UIAElement.cachedClassName.endswith("BreadcrumbBarItem"):
				obj.roleText = obj.UIAElement.currentLocalizedControlType

	# Workaronds for Windows 10 and Server 2022
	if winVersion.getWinVer() < winVersion.WIN11:
		# Sometimes, the same text is announced, so consult this cache.
		_nameChangeCache: str = ""

		def event_liveRegionChange(self, obj, nextHandler):
			if isinstance(obj, UIA):
				# Except for specific cases, announce all live regions.
				# Announce individual update progress in build 16215 and later preferably only once per update stage.
				if "ApplicableUpdate" in obj.UIAAutomationId:
					# Do not announce status text itself.
					if obj.UIAAutomationId.endswith("_ContextDescriptionTextBlock"):
						return
					# Update title repeats while the update is downloaded and installed.
					if obj.UIAAutomationId.endswith("_DescriptionTextBlock"):
						# Keep announcing last status as long as object name is cached.
						if obj.name and obj.name == self._nameChangeCache:
							return
						# #71: NVDA is told to announce live regions to the end by default,
						# which results in screen content and speech getting out of sync.
						# However do not cut off other live regions when action button appears next to updates list
						# which is the sibling of the grandparent object (actual updates list element).
						# Update action button appears if the system is up to date or an action is required.
						# However attribute error may result if "update action" button is not a UIA element.
						try:
							if "UpdateActionButton" not in obj.parent.parent.next.UIAAutomationId:
								speech.cancelSpeech()
						except AttributeError:
							pass
					self._nameChangeCache = obj.name
			nextHandler()

		def event_appModule_loseFocus(self):
			self._nameChangeCache = ""

	# Workarounds for Windows 11 22H2 or later.
	elif winVersion.getWinVer() >= WIN11_22H2:
		def event_nameChange(self, obj, nextHandler):
			if isinstance(obj, UIA):
				if "ApplicableUpdate" in obj.UIAAutomationId:
					import ui
					try:
						# Announce updated screen content as long as update action control is not shown.
						# Simple previous object must be used as previous object returns an unusable button.
						if "UpdateActionButton" not in obj.parent.parent.parent.simplePrevious.UIAAutomationId:
							speech.cancelSpeech()
						ui.message(" ".join([element.name for element in obj.parent.children]))
					except AttributeError:
						pass
			nextHandler()

		def event_focusEntered(self, obj, nextHandler):
			if isinstance(obj, UIA):
				if obj.UIAAutomationId == "SystemSettings_MusUpdate_AvailableUpdatesList2_ListView":
					import UIAHandler
					for updateEntry in obj.children:
						updateStatus = updateEntry.simpleFirstChild.simpleLastChild
						try:
							UIAHandler.handler.removeEventHandlerGroup(
								updateStatus.UIAElement, UIAHandler.handler.localEventHandlerGroup
							)
							UIAHandler.handler.addEventHandlerGroup(
								updateStatus.UIAElement, UIAHandler.handler.localEventHandlerGroup
							)
						except NotImplementedError:
							pass
			nextHandler()
