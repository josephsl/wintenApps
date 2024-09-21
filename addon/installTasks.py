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
	# Windows App Essentials requires supported Windows releases (see minimum Windows version below).
	# For general availability channel (feature updates), support duration is tied to consumer-level support
	# (Home, Pro, Pro Education, Pro for Workstations, supported for 18 to 24 months with exceptions)
	# and the add-on may end support for a feature update prior to end of consumer support.
	# See aka.ms/WindowsTargetVersioninfo.
	# For Insider Preview, only the latest canary/dev/beta/release preview builds are supported
	# At a minimum, Windows App Essentials requires 64-bit Windows 10 22H2
	# (Version 22H2 (19045), the final Windows 10 feature update, is supported until October 2025).
	minimumWinVer = winVersion.WIN10_22H2
	if (currentWinVer := winVersion.getWinVer()) > minimumWinVer:
		# Windows App Essentials supports Windows 11 23H2 or later.
		minimumWinVer = winVersion.WIN11_23H2
	if currentWinVer < minimumWinVer:
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
