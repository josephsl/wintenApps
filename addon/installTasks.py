# WinApps/installTasks.py
# Copyright 2016-2022 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Routines are partly based on other add-ons,
# particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
addonHandler.initTranslation()


def onInstall():
	import gui
	import wx
	import winVersion
	currentWinVer = winVersion.getWinVer()
	# Windows App Essentials requires Windows 10 or later.
	# Translators: title of the error dialog shown when trying to install the add-on in unsupported systems.
	# Unsupported systems include Windows versions earlier than 10 and old Windows 10 feature updates.
	unsupportedWindowsReleaseTitle = _("Unsupported Windows release")
	if currentWinVer < winVersion.WIN10:
		gui.messageBox(
			_(
				# Translators: Dialog text shown when trying to install the add-on on releases earlier than Windows 10.
				"You are using an older version of Windows. This add-on requires Windows 10 or later."
			), unsupportedWindowsReleaseTitle, wx.OK | wx.ICON_ERROR
		)
		raise RuntimeError("Attempting to install Windows App Essentials on Windows releases earlier than 10")
	# Windows App Essentials does not support old feature updates.
	# Until Windows 10 21H1 (19043), checking build range was acceptable because there was one to one mapping
	# between feature updates/milestones and builds across clients and servers such as 1809/17763 (RS5).
	# But 21H2 changes this: Windows 10 (19044), Windows Server 2022 (20348), and Windows 11 (22000)
	# As these releases come from vibranium (vb), iron (fe), and cobalt (co) branches, respectively.
	# Depending on the nature of Windows 10 22H2 and the build number of Windows 11 22H2,
	# a different strategy may need to be employed in 2022 to test feature update builds.
	# For now assume minimum supported version is the one listed below unless this is Windows 11.
	windowsReleaseSeries = "Windows 10"
	minimumSupportedRelease = winVersion.WIN10_21H1
	minimumSupportedReleaseName = minimumSupportedRelease.releaseName
	addonInstallPossible = currentWinVer >= minimumSupportedRelease
	if not addonInstallPossible:
		gui.messageBox(
			_(
				# Translators: Dialog text shown when trying to install the add-on on an unsupported Windows release.
				# winRelease can be Windows 10, Windows 11, or other release series name.
				# minSupportedUpdate is the minimum update for a Windows release series required for this add-on.
				# Example: an add-on release requiring Windows 10 May 2021 Update
				# will set windowsRelease to Windows 10 and minSupportedUpdate to Windows 10 21H1.
				"You are using an unsupported {windowsRelease} release. "
				"This add-on requires {minSupportedUpdate} or later."
			).format(windowsRelease=windowsReleaseSeries, minSupportedUpdate=minimumSupportedReleaseName),
			unsupportedWindowsReleaseTitle, wx.OK | wx.ICON_ERROR
		)
		raise RuntimeError(
			"Attempting to install Windows App Essentials "
			f"on unsupported {windowsReleaseSeries} release"
		)
