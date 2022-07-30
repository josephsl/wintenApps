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
	import globalVars
	# Do not present dialogs if minimal mode is set.
	currentWinVer = winVersion.getWinVer()
	# Windows App Essentials requires Windows 10 or later.
	# Translators: title of the error dialog shown when trying to install the add-on in unsupported systems.
	# Unsupported systems include Windows versions earlier than 10 and old Windows 10 feature updates.
	unsupportedWindowsReleaseTitle = _("Unsupported Windows release")
	if currentWinVer < winVersion.WIN10:
		if not globalVars.appArgs.minimal:
			gui.messageBox(
				_(
					# Translators: Dialog text shown when trying to install the add-on on releases earlier than Windows 10.
					"You are using an older version of Windows. This add-on requires Windows 10 or later."
				), unsupportedWindowsReleaseTitle, wx.OK | wx.ICON_ERROR
			)
		raise RuntimeError("Attempting to install Windows App Essentials on Windows releases earlier than 10")
	# Windows App Essentials does not support unsupported feature updates.
	# Until Windows 10 21H1 (19043), checking build range was acceptable because there was one to one mapping
	# between feature updates/milestones and builds across clients and servers such as 1809/17763 (RS5).
	# But 21H2 changed this: Windows 10 (19044), Windows Server 2022 (20348), and Windows 11 (22000)
	# As these releases come from vibranium (vb), iron (fe), and cobalt (co) branches, respectively.
	# This continues in 22H2 with Windows 10 (19045) and Windows 11 (22621).
	# Therefore, display supported builds list across Windows releases.
	# For compatibility, assume minimum supported version is the one listed below unless this is Windows 11.
	# Old NVDA versions do not include minimum Windows version defined.
	# Note that the add-on does support NVDA releases with Windows 10, 11, and Server 2022 defined.
	# Deprecated: switch from minimum release check to builds list.
	minWindowsRelease = winVersion.WinVersion(major=10, minor=0, build=19044, releaseName="Windows 10 21H2")
	windowsReleaseSeries = "Windows 10"
	minimumSupportedReleaseAttribute = "WIN10_21H2"
	# Windows 11
	# There is no known public release between Server 2022 (build 20348) and Windows 11 (build 22000).
	# Builds in this range (21000) are Insider builds and are branded as Windows 10 but later changed to 11.
	# For simplicity, treat these builds as Windows 11 builds and installation will fail.
	if currentWinVer > winVersion.WINSERVER_2022:
		minWindowsRelease = winVersion.WinVersion(major=10, minor=0, build=22000, releaseName="Windows 11 21H2")
		windowsReleaseSeries = "Windows 11"
		minimumSupportedReleaseAttribute = "WIN11"
	minimumSupportedRelease = getattr(winVersion, minimumSupportedReleaseAttribute, minWindowsRelease)
	minimumSupportedReleaseName = minimumSupportedRelease.releaseName
	addonInstallPossible = currentWinVer >= minimumSupportedRelease
	unsupportedWindowsReleaseText = _(
		# Translators: Dialog text shown when trying to install the add-on on an unsupported Windows release.
		# winRelease can be Windows 10, Windows 11, or other release series name.
		# minSupportedUpdate is the minimum update for a Windows release series required for this add-on.
		# Example: an add-on release requiring Windows 10 May 2021 Update
		# will set windowsRelease to Windows 10 and minSupportedUpdate to Windows 10 21H1.
		"You are using an unsupported {windowsRelease} release. "
		"This add-on requires {minSupportedUpdate} or later."
	).format(windowsRelease=windowsReleaseSeries, minSupportedUpdate=minimumSupportedReleaseName)
	# Record supported builds.
	# Windows Server 2022 (build 20348), despite a different code base, is still Windows 10.
	# But since it is labeled 21H2, add-on support duration is tied to the client (build 19044).
	supportedBuilds = {
		# Windows 10 (and Server 2022)
		19044: "21H2",
		19045: "22H2",
		20348: "Windows Server 2022",
		# Windows 11
		22000: "21H2",
		22621: "22H2"
	}
	addonInstallPossible = (
		currentWinVer.build in supportedBuilds  # General availability channel
		or currentWinVer.build >= max(supportedBuilds)  # Insider Preview
	)
	# Present different builds depending on Windows release.
	if currentWinVer > winVersion.WINSERVER_2022:
		supportedBuilds = {build: release for build, release in supportedBuilds.items() if build >= 22000}
	else:
		supportedBuilds = {build: release for build, release in supportedBuilds.items() if build < 22000}
	unsupportedWindowsReleaseText = _(
		# Translators: Dialog text shown when trying to install the add-on on an unsupported Windows release.
		# winRelease can be Windows 10, Windows 11, or other release series name.
		# windowsReleasesList records supported releases for a given Windows release series.
		# For example, if 21H2 and 22H2 are supported, the text will list supported releases at the end.
		"You are using an unsupported {windowsRelease} release. "
		"Supported releases: {windowsReleasesList}."
	).format(windowsRelease=windowsReleaseSeries, windowsReleasesList=", ".join(supportedBuilds.values()))
	if not addonInstallPossible:
		if not globalVars.appArgs.minimal:
			gui.messageBox(unsupportedWindowsReleaseText, unsupportedWindowsReleaseTitle, wx.OK | wx.ICON_ERROR)
		raise RuntimeError(
			"Attempting to install Windows App Essentials "
			f"on unsupported {windowsReleaseSeries} release"
		)
