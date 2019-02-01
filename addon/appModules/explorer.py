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
import winVersion
import ui

class AppModule(AppModule):

	def isGoodUIAWindow(self,hwnd):
		# In build 18305 and later, it is the shell that raises window open event for emoji panel (the below check is subject to change).
		if winVersion.winVersion.build > 17763 and winUser.getClassName(hwnd) == "ApplicationFrameWindow":
			return True
		return False

	def event_UIA_window_windowOpen(self, obj, nextHandler):
		# Send UIA window open event to input app window.
		if isinstance(obj, UIA) and obj.UIAElement.cachedClassName == "ApplicationFrameWindow":
			inputPanelWindow = obj.firstChild
			if inputPanelWindow and inputPanelWindow.appModule.appName == "windowsinternal_composableshell_experiences_textinput_inputapp":
				eventHandler.executeEvent("UIA_window_windowOpen", inputPanelWindow)
				return
		nextHandler()

	# Handle notification event oddities in build 18323 and later.
	_sliderValueEvent = False

	def event_valueChange(self, obj, nextHandler):
		if isinstance(obj, UIA) and obj.UIAElement.cachedAutomationID in ("AudioSliderContainer", "BrightnessSliderContainer"):
			self._sliderValueEvent = True
		nextHandler()

	def event_UIA_notification(self, obj, nextHandler, displayString=None, **kwargs):
		# In build 18323, volume and brightness changes are reported via this event.
		# Similar to Microsoft Edge, other programs will be in use for majority of the time.
		if self._sliderValueEvent:
			ui.message(displayString)
			self._sliderValueEvent = False
