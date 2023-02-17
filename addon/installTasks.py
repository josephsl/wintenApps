# WinApps/installTasks.py
# Copyright 2016-2023 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Routines are partly based on other add-ons,
# particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
addonHandler.initTranslation()


def onInstall():
	import winVersion
	currentWinVer = winVersion.getWinVer()
	# Windows App Essentials requires supported Windows 10/11 feature updates.
	# Support duration is tied to consumer-level support (18 months for Windows 10, 2 years for Windows 11)
	# and the add-on may end support for a feature update prior to end of consumer support.
	# Applicable to Home, Pro, Pro Education, Pro for Workstations (see aka.ms/WindowsTargetVersioninfo).
	# Note that Windows Server 2022 (20348) reports itself as Windows 10 21H2,
	# thus add-on support duration is tied to the client (19044).
	supportedBuilds = {
		# Windows 10
		19045: "Windows 10 22H2",
		20348: "Windows Server 2022",
		# Windows 11
		22000: "Windows 11 21H2",
		22621: "22H2",
		# Latest Windows Insider beta channel build
		22623: "22H2 beta",
	}
	currentBuild = currentWinVer.build
	# Optimization: report success (return early) if running a supported release.
	if (
		currentBuild in supportedBuilds  # General availability channel
		or currentBuild >= max(supportedBuilds)  # Insider Preview
	):
		return
	import gui
	import wx
	import globalVars
	# Translators: title of the error dialog shown when trying to install the add-on in unsupported systems.
	# Unsupported systems include Windows versions earlier than 10 and unsupported feature updates.
	unsupportedWindowsReleaseTitle = _("Unsupported Windows release")
	# #78: obtain a list of all supported releases (and builds) from supported builds list.
	windowsReleasesList = [
		# Translators: an entry in supported Windows releases list (release (build)).
		_("{release} ({build})").format(release=release, build=build)
		for build, release in supportedBuilds.items()
	]
	windowsReleasesList.append("Windows Insider Preview")
	unsupportedWindowsReleaseText = _(
		# Translators: Dialog text shown when trying to install the add-on on an unsupported Windows release.
		# Release name and build refer to Windows release in use (example: Windows 10 21H2 (19044)).
		# Supported releases list shows releases supported by the add-on.
		"You are using {releaseName} ({build}), a Windows release not supported by this add-on.\n"
		"Supported releases: {supportedReleasesList}."
	).format(
		releaseName=currentWinVer.releaseName,
		build=currentBuild,
		supportedReleasesList=", ".join(windowsReleasesList)
	)
	# Do not present error dialog if minimal mode is set.
	if not globalVars.appArgs.minimal:
		gui.messageBox(unsupportedWindowsReleaseText, unsupportedWindowsReleaseTitle, wx.OK | wx.ICON_ERROR)
	raise RuntimeError(f"Windows App Essentials does not support {currentWinVer.releaseName} ({currentBuild})")
