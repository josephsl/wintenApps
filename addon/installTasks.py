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
	# Unsupported systems include Windows versions earlier than 10 and unsupported feature updates.
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
	# This continues in 22H2 with Windows 10 (19045/vibranium) and Windows 11 (22621/nickel).
	# Therefore, display supported builds list across Windows releases.
	# Record supported builds.
	# Windows Server 2022 reports itself as 21H2, thus add-on support duration is tied to the client (19044).
	supportedBuilds = {
		"Windows 10": {
			19044: "21H2",
			19045: "22H2",
			20348: "Windows Server 2022",
		},
		"Windows 11": {
			22000: "21H2",
			22621: "22H2",
		}
	}
	windowsReleaseSeries = "Windows 10"
	if currentWinVer >= winVersion.WIN11:
		windowsReleaseSeries = "Windows 11"
	supportedBuilds = supportedBuilds[windowsReleaseSeries]
	# Optimization: report success (return early) if running a supported release.
	if (
		currentWinVer.build in supportedBuilds  # General availability channel
		or (windowsReleaseSeries == "Windows 11" and currentWinVer.build >= max(supportedBuilds))  # Insider Preview
	):
		return
	# #78: test the old and new (combined) install error messages, initially set to "False" for compatibility.
	presentCombinedErrorMessage = False
	windowsReleasesListText = ", ".join([
		"Windows 10 21H2 (19044)",
		"22H2 (19045)",
		"Windows Server 2022 (20348)",
		"Windows 11 21H2 (22000)",
		"22H2 (22621)",
		"Windows Insider Preview"
	])
	unsupportedWindowsReleaseText = _(
		# Translators: Dialog text shown when trying to install the add-on on an unsupported Windows release.
		# Release name and build refer to Windows release in use (example: Windows 10 21H2 (19044)).
		# Supported releases list shows releases supported by the add-on.
		"You are using {releaseName} ({build}), a Windows release not supported by Windows App Essentials add-on.\n"
		"Supported releases: {supportedReleasesList}."
	).format(
		releaseName=currentWinVer.releaseName,
		build=currentWinVer.build,
		supportedReleasesList=windowsReleasesListText
	)
	if not presentCombinedErrorMessage:
		unsupportedWindowsReleaseText = _(
			# Translators: Dialog text shown when trying to install the add-on on an unsupported Windows release.
			# winRelease can be Windows 10, Windows 11, or other release series name.
			# windowsReleasesList records supported releases for a given Windows release series.
			# For example, if 21H2 and 22H2 are supported, the text will list supported releases at the end.
			"You are using an unsupported {windowsRelease} release. "
			"Supported releases: {windowsReleasesList}."
		).format(windowsRelease=windowsReleaseSeries, windowsReleasesList=", ".join(supportedBuilds.values()))
	if not globalVars.appArgs.minimal:
		gui.messageBox(unsupportedWindowsReleaseText, unsupportedWindowsReleaseTitle, wx.OK | wx.ICON_ERROR)
	raise RuntimeError(
		"Attempting to install Windows App Essentials "
		f"on unsupported {windowsReleaseSeries} release"
	)
