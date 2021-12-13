# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2019-2022 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Originally copyright 2016-2021 Joseph Lee, released under GPL

# Several hacks related to Settings app, some of which are part of NVDA Core.

# Help Mypy and other static checkers for a time by importing uppercase versions of built-in types.
from typing import Any
# See the above note as to why the below procedure must be done.
from nvdaBuiltin.appModules.systemsettings import *  # NOQA: F403
import ui
import controlTypes
from NVDAObjects.UIA import UIA


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
			if obj.role == controlTypes.Role.LINK:
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
			# Announce optional updates in Windows 11.
			# Same as above except it uses a different Automation Id.
			elif obj.UIAAutomationId == "SystemSettings_MusUpdate_SeekerUpdateUX_Button":
				obj.name = ", ".join([obj.previous.previous.name, obj.name])
			# In some cases, Active Directory style name is the name of the window,
			# so tell NVDA to use something more meaningful.
			elif obj.name == "CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington, C=US":
				obj.name = obj.firstChild.name
			# Developer mode label in Windows 10 2004/20H2/21H1/21H2.
			# The label itself is the name of the previous object.
			# Resolved in Windows 11.
			elif obj.name == "SystemSettings_Developer_Mode_Advanced_NarratorText":
				obj.name = obj.previous.name
			# Windows 11's breadcrumb bar item uses a custom localized control type text.
			# Although it is recognized as a heading, override role text to communicate what it actually is.
			# This allows item label to be kept intact.
			elif obj.UIAElement.cachedClassName.endswith("BreadcrumbBarItem"):
				obj.roleText = obj.UIAElement.currentLocalizedControlType

	# Sometimes, the same text is announced, so consult this cache.
	_nameChangeCache: str = ""

	def event_liveRegionChange(self, obj, nextHandler):
		if isinstance(obj, UIA) and obj.name and obj.name != self._nameChangeCache:
			automationId = obj.UIAAutomationId
			# Except for specific cases, announce all live regions.
			# Announce individual update progress in build 16215 and later preferably only once per update stage.
			if "ApplicableUpdate" in automationId and not automationId.endswith("_ContextDescriptionTextBlock"):
				return
			self._nameChangeCache = obj.name
			try:
				# Until the spacing problem is fixed for update label...
				if "ApplicableUpdate" in automationId and automationId.endswith("_ContextDescriptionTextBlock"):
					ui.message(" ".join([obj.parent.name, obj.name]))
				else:
					ui.message(obj.name)
				# And no, never allow double-speaking (an ugly hack).
				return
			except AttributeError:
				pass

	def event_appModule_loseFocus(self):
		self._nameChangeCache = ""
