# Windows 10 controls repository
# Copyright 2015-2016 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10.
# Also adds interceptors for certain keyboard commands.

import globalPluginHandler
import appModuleHandler # Huge workaround.
import controlTypes
from NVDAObjects.UIA import UIA
import api
import speech

# Until NVDA Core ticket 5323 is implemented, have our own find app mod from PID handy.
def getAppModuleFromProcessID(processID):
	"""Finds the appModule that is for the given process ID. The module is also cached for later retreavals.
	@param processID: The ID of the process for which you wish to find the appModule.
	@type processID: int
	@returns: the appModule, or None if there isn't one
	@rtype: appModule 
	"""
	with appModuleHandler._getAppModuleLock:
		mod=appModuleHandler.runningTable.get(processID)
		if not mod:
			appName=appModuleHandler.getAppNameFromProcessID(processID)
			# #5323: Certain executables contain dots as part of its file name.
			if "." in appName:
				appName = appName.replace(".","_")
			mod=appModuleHandler.fetchAppModule(processID,appName)
			if not mod:
				raise RuntimeError("error fetching default appModule")
			appModuleHandler.runningTable[processID]=mod
	return mod

# Looping selectors are used in apps such as Alarms and Clock and Windows Update to select time values.
class LoopingSelectorItem(UIA):

	def event_UIA_elementSelected(self):
		speech.cancelSpeech()
		api.setNavigatorObject(self)
		self.reportFocus()

# Certain UIA combo box items are no longer announced.
class ComboBoxItem(UIA):

	def event_UIA_elementSelected(self):
		api.setNavigatorObject(self)

# Tell Search UI app module to silence NVDA while the following is happenig.
letCortanaListen = False


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# Hack: Some executables, particular UWA apps have a dot in the middle.
		# Therefore coerce the app module handler to use the modified routine above.
		appModuleHandler.getAppModuleFromProcessID = getAppModuleFromProcessID

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# NVDA Core ticket 5231: Announce values in time pickers.
		if isinstance(obj, UIA):
			# Handle both Threshold and Redstone looping selector items.
			if obj.role==controlTypes.ROLE_LISTITEM and "LoopingSelectorItem" in obj.UIAElement.cachedClassName:
				clsList.append(LoopingSelectorItem)
			# Combo box items are not announced when using up or down arrows.
			elif obj.role==controlTypes.ROLE_LISTITEM and obj.UIAElement.cachedClassName == "ComboBoxItem":
				clsList.append(ComboBoxItem)

	# Focus announcement hacks.
	def event_gainFocus(self, obj, nextHandler):
		# Never allow WorkerW thread to send gain focus event (seen in Insider builds but was observed in release builds for some).
		if obj.role == controlTypes.ROLE_PANE and obj.appModule.appModuleName == "explorer" and obj.windowClassName == "WorkerW" and obj.name is None:
			return
		nextHandler()

	def script_voiceActivation(self, gesture):
		gesture.send()
		import sys
		if sys.getwindowsversion().major == 10:
			global letCortanaListen
			letCortanaListen = True


	__gestures={"kb:windows+c":"voiceActivation"}

