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
	# Windows 10 22H2 (19045) is supported until October 2025 as this is the final feature update.
	supportedBuilds = {
		# Windows 10
		19045: "Windows 10 22H2",
		# Windows 11
		22621: "Windows 11 22H2",
	}
	currentBuild = currentWinVer.build
	# Optimization: report success (return early) if running a supported release.
	if (
		currentBuild in supportedBuilds  # General availability channel
		or currentBuild >= max(supportedBuilds)  # Insider Preview
	):
		return
	import globalVars
	# Do not present error dialog if minimal mode is set.
	if globalVars.appArgs.minimal:
		raise RuntimeError(f"Windows App Essentials does not support {currentWinVer.releaseName} ({currentBuild})")
	import gui
	import wx
	# Only present Windows 11 builds if this is a build above Windows 10 22H2.
	if currentBuild > 19045:
		del supportedBuilds[19045]
		# Insider builds released between stable Windows 11 builds are also unsupported by the add-on.
		# For now this includes nickel development builds (22000 < build < 22621).
		if 22000 < currentBuild < 22621:
			del supportedBuilds[22000]
			supportedBuilds[22621] = "Windows 11 22H2"
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
	gui.messageBox(unsupportedWindowsReleaseText, unsupportedWindowsReleaseTitle, wx.OK | wx.ICON_ERROR)
	raise RuntimeError(f"Windows App Essentials does not support {currentWinVer.releaseName} ({currentBuild})")
