# WinApps/installTasks.py
# Copyright 2016-2024 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Routines are partly based on other add-ons,
# particularly Place Markers by Noelia Martinez (thanks add-on authors).

import winVersion
import addonHandler
addonHandler.initTranslation()


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
	winVersion.WinVersion(major=10, minor=0, build=26100, releaseName="Windows 11 24H2"),
]


def addonChannel() -> str | None:
	# Obtains the current add-on install channel (default is None, indicating stable channel).
	import os.path
	updateChannel = addonHandler.Addon(os.path.dirname(__file__)).manifest.get("updateChannel")
	return None if updateChannel == "None" else updateChannel


def canInstallWinAppsAddon(currentWinVer: winVersion.WinVersion) -> bool:
	return (
		currentWinVer in SUPPORTED_RELEASES  # General availability channel and Insider release preview
		or currentWinVer > max(SUPPORTED_RELEASES)  # Insider Preview canary/dev/beta
		# The next condition will be removed once Insider Preview beta channel moves to 24H2.
		or currentWinVer.build == 22635  # Windows 11 23H2 beta
	)


def presentInstallError(currentWinVer: winVersion.WinVersion) -> None:
	import gui
	import wx
	import gettext
	_ = gettext.gettext
	# Translators: title of the error dialog shown when trying to install the add-on in unsupported systems.
	# Unsupported systems include Windows versions earlier than 10, 32-bit Windows 10,
	# and unsupported feature updates.
	unsupportedWindowsReleaseTitle: str = _("Unsupported Windows release")
	# #78: obtain a list of all supported releases (and builds) from supported releases list.
	# Present releases above the current release if possible.
	# For example, present Windows 11 releases if this is a release above Windows 10 22H2 (19045).
	minimumWinVer: winVersion.WinVersion = min(entry for entry in SUPPORTED_RELEASES if entry > currentWinVer)
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


def onInstall() -> None:
	currentWinVer = winVersion.getWinVer()
	if not canInstallWinAppsAddon(currentWinVer):
		presentInstallError(currentWinVer)
		raise RuntimeError(
			f"Windows App Essentials does not support {currentWinVer.releaseName} ({currentWinVer.build})"
		)
	# Present a message if installing on 32-bit Windows 10 22H2 systems.
	if not currentWinVer.processorArchitecture.endswith("64"):
		import gui
		import wx
		gui.messageBox(
			"You are using 32-bit Windows 10. This add-on requires 64-bit Windows 10 or later.",
			"32-bit Windows 10 system detected", wx.OK | wx.ICON_INFORMATION
		)
