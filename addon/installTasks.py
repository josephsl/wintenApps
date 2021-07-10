# WinTenApps/installTasks.py
# Copyright 2016-2021 Joseph Lee, released under GPL.

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
	currentWinVer = winVersion.getWinVer()
	# Windows App Essentials requires Windows 10 or later.
	# Translators: title of the error dialog shown when trying to install the add-on in unsupported systems.
	# Unsupported systems include Windows versions earlier than 10 and old Windows 10 feature updates.
	unsupportedWindowsReleaseTitle = _("Unsupported Windows release")
	if currentWinVer < winVersion.WIN10:
		gui.messageBox(
			_(
				# Translators: Dialog text shown when trying to install the add-on on releases earlier than Windows 10.
				"You are using an older version of Windows. This add-on requires Windows 10 or later."
			), unsupportedWindowsReleaseTitle, wx.OK | wx.ICON_ERROR
		)
		raise RuntimeError("Attempting to install Windows App Essentials on Windows releases earlier than 10")
	# Windows App Essentials does not support old feature updates.
	# This is the case for Windows 10 (to be expanded to Windows 11 in the future).
	# For now only check Windows 10.
	windowsReleaseSeries = "Windows 10"
	minimumSupportedRelease = winVersion.WIN10_20H2
	minimumSupportedReleaseName = "Windows 10 20H2"
	addonInstallPossible = currentWinVer >= minimumSupportedRelease
	if not addonInstallPossible:
		gui.messageBox(
			_(
				# Translators: Dialog text shown when trying to install the add-on on an unsupported Windows release.
				# winRelease can be Windows 10, Windows 11, or other release series name.
				# minSupportedUpdate is the minimum update for a Windows release series required for this add-on.
				# Example: an add-on release requiring Windows 10 May 2021 Update
				# will set windowsRelease to Windows 10 and minSupportedUpdate to Windows 10 21H1.
				"You are using an unsupported {windowsRelease} release. "
				"This add-on requires {minSupportedUpdate} or later."
			).format(windowsRelease=windowsReleaseSeries, minSupportedUpdate=minimumSupportedReleaseName),
			unsupportedWindowsReleaseTitle, wx.OK | wx.ICON_ERROR
		)
		raise RuntimeError(
			"Attempting to install Windows App Essentials "
			f"on unsupported {windowsReleaseSeries} release"
		)
	# Although installation on server systems is possible, Windows App Essentials does not support it fully.
	# Namely Windows Server does not come with modern apps such as Microsoft Store.
	# Therefore display a warning message if running on servers.
	if currentWinVer.productType != "workstation":
		gui.messageBox(
			_(
				# Translators: warning text shown when trying to install the add-on on server computers.
				"This is a Windows Server system. Although you can install the add-on, "
				"not all features will work as Windows Server does not include modern apps such as Microsoft Store."
			),
			# Translators: title of the warning dialog shown when trying to install the add-on on server systems.
			_("Windows App Essentials and Windows Server"), wx.OK | wx.ICON_WARNING
		)
