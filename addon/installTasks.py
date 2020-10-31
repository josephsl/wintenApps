# WinTenApps/installTasks.py
# Copyright 2016-2019 Joseph Lee, released under GPL.

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
	requiredVer = "Windows 10 Version 2004"
	if not winVersion.isWin10(version=2004) and gui.messageBox(
		_(
			# Translators: Dialog text shown when attempting to install the add-on on an unsupported version of Windows
			# (minSupportedVersion is the minimum version required for this add-on).
			"You are using an older version of Windows. This add-on requires {minSupportedVersion} or later. "
			"Are you sure you wish to install this add-on anyway?"
		).format(minSupportedVersion=requiredVer),
		# Translators: title of the dialog shown when attempting to install the add-on on an old version of Windows.
		_("Old Windows version"), wx.YES | wx.NO | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION
	) == wx.NO:
		raise RuntimeError("Old Windows version detected")
