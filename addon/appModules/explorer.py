#appModules/explorer.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2018 NV Access Limited, Joseph Lee
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""App module for Windows Explorer (aka Windows shell).
Provides workarounds for controls such as identifying Start button, notification area and others.
"""

# The add-on version of this module will extend the one that comes with NVDA Core.

from nvdaBuiltin.appModules.explorer import *

class AppModule(AppModule):

	def isGoodUIAWindow(self,hwnd):
		# In build 18305 and later, it is the shell that raises window open event for emoji panel (the below check is subject to change).
		if winVersion.isWin10(version=1903) and winUser.getClassName(hwnd) == "ApplicationFrameWindow":
			return True
		return False

	def event_UIA_window_windowOpen(self, obj, nextHandler):
		# Send UIA window open event to input app window.
		if isinstance(obj, UIA) and obj.UIAElement.cachedClassName == "ApplicationFrameWindow":
			inputPanelWindow = obj.firstChild
			# In build 18963, executable name for modern keyboard has changed, so support both executables.
			if inputPanelWindow and inputPanelWindow.appModule.appName in ("windowsinternal_composableshell_experiences_textinput_inputapp", "textinputhost"):
				eventHandler.executeEvent("UIA_window_windowOpen", inputPanelWindow)
				return
		nextHandler()
