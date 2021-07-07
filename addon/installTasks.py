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
	requiredVer = "Windows 10 20H2"
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
	# Although installation on server systems is possible, Windows App Essentials does not support it fully.
	# Namely Windows Server does not come with modern apps such as Microsoft Store.
	# Therefore display a warning message if running on servers.
	productType = ("workstation", "domain controller", "server")[sys.getwindowsversion().product_type - 1]
	if productType != "workstation":
		gui.messageBox(
			_(
				# Translators: warning text shown when trying to install the add-on on server computers.
				"This is a Windows Server system. Although you can install the add-on, "
				"not all features will work as Windows Server does not include modern apps such as Microsoft Store."
			),
			# Translators: title of the warning dialog shown when trying to install the add-on on server systems.
			_("Windows App Essentials and Windows Server"), wx.OK | wx.ICON_WARNING
		)
	# Temporary: warn stable release users about experimental support for Windows 11
	# (dev channel subscribers will not receive warnings).
	if sys.getwindowsversion().build >= 22000:
		warnWin11Experimental = False
		for addon in addonHandler.getAvailableAddons():
			if addon.name == "wintenApps" and addon.isPendingInstall:
				warnWin11Experimental = not addon.version.endswith("-dev")
				break
		if warnWin11Experimental:
			# THIS WARNING DIALOG WILL NOT BE TRANSLATED!
			gui.messageBox(
				"You are using Windows 11 Insider Preview. Support for Windows 11 is experimental "
				"and features can change without notice prior to its general release.",
				"Windows 11 support notice", wx.OK | wx.ICON_WARNING
			)
