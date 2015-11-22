# Windows 10 controls repository
# Copyright 2015 Joseph Lee, released under GPL.

# Adds handlers for vairous UIA controls found in Windows 10.

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

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# Hack: Some executables, particular UWA apps have a dot in the middle.
		# Therefore coerce the app module handler to use the modified routine above.
		appModuleHandler.getAppModuleFromProcessID = getAppModuleFromProcessID

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# NVDA Core ticket 5231: Announce values in time pickers.
		if isinstance(obj, UIA):
			if obj.role==controlTypes.ROLE_LISTITEM and obj.UIAElement.cachedClassName == "LoopingSelectorItem":
				clsList.append(LoopingSelectorItem)
