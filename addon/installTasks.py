# WinApps/installTasks.py
# Copyright 2016-2024 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Routines are partly based on other add-ons,
# particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
addonHandler.initTranslation()


def onInstall() -> None:
	import winVersion
	import gui
	import wx
	# Windows App Essentials requires supported Windows feature updates (see the list below).
	# Support duration is tied to consumer-level support (Home, Pro, Pro Education, Pro for Workstations)
	# and the add-on may end support for a feature update prior to end of consumer support.
	# See aka.ms/WindowsTargetVersioninfo.
	# Windows 10 22H2 (19045) is supported until October 2025 as this is the final Windows 10 feature update.
	# Note that Windows App Essentials add-on does not support 32-bit Windows 10 systems.
	# For Insider Preview builds, only the latest build for each channel (canary/dev/beta) are supported.
	SUPPORTED_RELEASES: list[winVersion.WinVersion] = [
		winVersion.WIN10_22H2,
		winVersion.WIN11_22H2,
		winVersion.WIN11_23H2,
		# Windows 11 24H2 (10.0.26100) is supported.
	]
	currentWinVer = winVersion.getWinVer()
	# At a minimum, Windows App Essentials requires Windows 10 22H2.
	minimumWinVer = winVersion.WIN10_22H2
	# Windows App Essentials support Windows 11 22H2 or later.
	if currentWinVer > minimumWinVer:
		minimumWinVer = winVersion.WIN11_22H2
	if not (
		currentWinVer in SUPPORTED_RELEASES  # General availability channel and Insider release preview
		or currentWinVer > max(SUPPORTED_RELEASES)  # Insider Preview canary/dev/beta
	):
		# #78: present the supported version above the current release.
		minimumWinVer: winVersion.WinVersion = min(entry for entry in SUPPORTED_RELEASES if entry > currentWinVer)
		gui.messageBox(
			_(
				# Translators: Dialog text shown when trying to install the add-on on
				# releases earlier than minimum supported release.
				"You are using {releaseName} ({build}), a Windows release not supported by this add-on.\n"
				"This add-on requires {supportedReleaseName} ({supportedBuild}) or later."
			).format(
				releaseName=currentWinVer.releaseName,
				build=currentWinVer.build,
				supportedReleaseName=minimumWinVer.releaseName,
				supportedBuild=minimumWinVer.build
			),
			# Translators: title of the error dialog shown when trying to install the add-on in
			# unsupported Windows systems (earlier than 10, 32-bit Windows 10, unsupported feature updates).
			_("Unsupported Windows release"), wx.OK | wx.ICON_ERROR
		)
		raise RuntimeError(
			f"Windows App Essentials does not support {currentWinVer.releaseName} ({currentWinVer.build})"
		)
