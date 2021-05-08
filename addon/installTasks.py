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
	import sys
	requiredVer = "Windows 10 Version 20H2"
	if hasattr(winVersion, "getWinVer"):
		W10AddonSupported = winVersion.getWinVer() >= winVersion.WIN10_20H2
	else:
		W10AddonSupported = sys.getwindowsversion().build >= 19042
	if not W10AddonSupported:
		gui.messageBox(
			_(
				# Translators: Dialog text shown when trying to install the add-on on an unsupported version of Windows
				# (minSupportedVersion is the minimum version required for this add-on).
				"You are using an older version of Windows. This add-on requires {minSupportedVersion} or later."
			).format(minSupportedVersion=requiredVer),
			# Translators: title of the dialog shown when trying to install the add-on on an old version of Windows.
			_("Old Windows version"), wx.OK | wx.ICON_ERROR
		)
		raise RuntimeError("Old Windows version detected")
