# WinTenApps/installTasks.py
# Copyright 2016 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Routines are partly based on other add-ons, particularly Place Markers by Noelia Martinez (thanks add-on authors).

import sys
import gui
import wx

def onInstall():
	if sys.getwindowsversion().build < 7601 and gui.messageBox("You are using an older version of Windows. This add-on requires Windows 7 Service Pack 1 or later. Are you sure you wish to install this add-on anyway?", "Old Windows version", wx.YES | wx.NO | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION) == wx.NO:
		raise RuntimeError("Old Windows version detected")
