# WinApps/installTasks.py
# Copyright 2016-2024 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Routines are partly based on other add-ons,
# particularly Place Markers by Noelia Martinez (thanks add-on authors).

# Keep the following import until Python 3.11 (NVDA 2024.1) requirement is fully in effect.
from __future__ import annotations
import addonHandler
addonHandler.initTranslation()


# Windows App Essentials requires supported Windows 10/11 feature updates.
# Support duration is tied to consumer-level support (18 months for Windows 10, 2 years for Windows 11)
# and the add-on may end support for a feature update prior to end of consumer support.
# Applicable to Home, Pro, Pro Education, Pro for Workstations (see aka.ms/WindowsTargetVersioninfo).
# Windows 10 22H2 (19045) is supported until October 2025 as this is the final feature update.
# For Insider Preview builds, only the latest build for each channel (canary/dev/beta) are supported.
SUPPORTED_BUILDS: dict[int, str] = {
	# Windows 10
	19045: "10 22H2",
	# Windows 11
	22621: "11 22H2",
	22631: "11 23H2",
}


def onInstall() -> None:
	def canInstallWinAppsAddon() -> bool:
		currentWinVer = winVersion.getWinVer()
		currentBuild: int = currentWinVer.build
		return (
			currentBuild in SUPPORTED_BUILDS  # General availability channel and Insider release preview
			or currentBuild > max(SUPPORTED_BUILDS)  # Insider Preview canary/dev/beta
		)
	def presentInstallError() -> None:
		import gui
		import wx
		import gettext
		_ = gettext.gettext
		# Translators: title of the error dialog shown when trying to install the add-on in unsupported systems.
		# Unsupported systems include Windows versions earlier than 10 and unsupported feature updates.
		unsupportedWindowsReleaseTitle: str = _("Unsupported Windows release")
		# #78: obtain a list of all supported releases (and builds) from supported builds list.
		# Present builds above the current build if possible.
		# For example, present Windows 11 builds if this is a build above Windows 10 22H2 (19045).
		windowsReleasesList: list[str] = [
			# Translators: an entry in supported Windows releases list (release (build)).
			_("{release} ({build})").format(release=release, build=build)
			for build, release in SUPPORTED_BUILDS.items() if build > currentBuild
		]
		windowsReleasesList.append("Windows Insider Preview")
		unsupportedWindowsReleaseText: str = _(
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
	# Optimization: report success (return early) if running a supported release.
	if canInstallWinAppsAddon():
		return
	presentInstallError()
	raise RuntimeError(f"Windows App Essentials does not support {currentWinVer.releaseName} ({currentBuild})")
