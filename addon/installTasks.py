# WinApps/installTasks.py
# Copyright 2016-2025 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Routines are partly based on other add-ons,
# particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
import winVersion
import gui

addonHandler.initTranslation()


def onInstall() -> None:
	# Windows App Essentials requires supported Windows releases on or above the minimum version.
	# For general availability channel (feature updates), support duration is tied to consumer-level support
	# (Home, Pro, Pro Education, Pro for Workstations, supported for 18 to 24 months with exceptions)
	# and the add-on may end support for a feature update prior to end of consumer support.
	# See aka.ms/WindowsTargetVersioninfo.
	# For Insider Preview, only the latest canary/dev/beta/release preview builds are supported.
	minimumWinVer = (
		winVersion.WIN11_23H2
		if (
			(currentWinVer := winVersion.getWinVer()) > winVersion.WIN10_22H2
			# Detect add-on update channels (specifically to prevent dev channel installation on Windows 10).
			# To be removed once add-on stable channel asks for Windows 11.
			or addonHandler.getCodeAddon().manifest.get("updateChannel") != "None"
		)
		else winVersion.WIN10_22H2  # 64-bit only, final feature update (supported until October 2025)
	)
	if currentWinVer < minimumWinVer:
		gui.MessageDialog.alert(
			# Tell mypy that it is okay to ignore gettext calls.
			_(  # type: ignore[name-defined]
				# Translators: Dialog text shown when trying to install the add-on on
				# releases earlier than minimum supported release.
				"You are using {releaseName} ({build}), a Windows release not supported by this add-on.\n"
				"This add-on requires {supportedReleaseName} ({supportedBuild}) or later."
			).format(
				releaseName=currentWinVer.releaseName,
				build=currentWinVer.build,
				supportedReleaseName=minimumWinVer.releaseName,
				supportedBuild=minimumWinVer.build,
			),
			# Translators: dialog title shown when trying to install the add-on on
			# unsupported Windows systems (earlier than 10, 32-bit Windows 10, unsupported feature updates).
			_("Unsupported Windows release"),  # type: ignore[name-defined]
		)
		raise RuntimeError(
			f"Windows App Essentials does not support {currentWinVer.releaseName} ({currentWinVer.build})"
		)
