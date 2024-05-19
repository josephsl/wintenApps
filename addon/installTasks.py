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
	# Windows App Essentials requires supported Windows feature updates (see minimum Windows version below).
	# For each feature update, support duration is tied to consumer-level support
	# (Home, Pro, Pro Education, Pro for Workstations, supported for 18 to 24 months with exceptions)
	# and the add-on may end support for a feature update prior to end of consumer support.
	# See aka.ms/WindowsTargetVersioninfo.
	# Windows 10 22H2 (19045) is supported until October 2025 as this is the final Windows 10 feature update.
	# Note that Windows App Essentials add-on does not support 32-bit Windows 10 systems.
	# For Insider Preview builds, only the latest build for each channel (canary/dev/beta) are supported.
	currentWinVer = winVersion.getWinVer()
	# At a minimum, Windows App Essentials requires Windows 10 22H2.
	minimumWinVer = winVersion.WIN10_22H2
	# Windows App Essentials supports Windows 11 23H2 or later.
	if currentWinVer > minimumWinVer:
		minimumWinVer = winVersion.WIN11_23H2
	if currentWinVer < minimumWinVer:
		# Translators: title of the error dialog shown when trying to install the add-on in unsupported systems.
		# Unsupported systems include Windows versions earlier than 10, 32-bit Windows 10,
		# and unsupported feature updates.
		unsupportedWindowsReleaseTitle: str = _("Unsupported Windows release")
		unsupportedWindowsReleaseText: str = _(
			# Translators: Dialog text shown when trying to install the add-on on an unsupported Windows release.
			# Release name and build refer to Windows release in use (example: Windows 10 21H2 (19044)).
			"You are using {releaseName} ({build}), a Windows release not supported by this add-on.\n"
			"This add-on requires {supportedReleaseName} ({supportedBuild}) or later."
		).format(
			releaseName=currentWinVer.releaseName,
			build=currentWinVer.build,
			supportedReleaseName=minimumWinVer.releaseName,
			supportedBuild=minimumWinVer.build
		)
		gui.messageBox(unsupportedWindowsReleaseText, unsupportedWindowsReleaseTitle, wx.OK | wx.ICON_ERROR)
		raise RuntimeError(
			f"Windows App Essentials does not support {currentWinVer.releaseName} ({currentWinVer.build})"
		)
