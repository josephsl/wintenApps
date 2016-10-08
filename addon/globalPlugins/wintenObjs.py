# Windows 10 controls repository
# Copyright 2015-2016 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10.

import sys
import os
import globalPluginHandler
import appModuleHandler # Huge workaround.
import controlTypes
import UIAHandler
import ui
from NVDAObjects.UIA import UIA
from NVDAObjects.behaviors import Dialog
import api
import speech
import braille
import nvwave

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
			# #5323: Certain executables contain dots as part of its file name.
			appName=appModuleHandler.getAppNameFromProcessID(processID).replace(".","_")
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

# We know the following elements are dialogs.
wintenDialogs=("Shell_Dialog", "Popup", "Shell_Flyout")

# Extra UIA constants
UIA_LiveRegionChangedEventId = 20024 # Coerce this to name change event for now.
UIA_ControllerForPropertyId = 30104 # Auto-suggestions.

# UIA COM constants
TreeScope_Subtree = 7

# Search fields.
# Some of them raise controller for event, an event fired if another UI element depends on this control.
class SearchField(UIA):

	def event_UIA_controllerFor(self):
		# Only useful if suggestions appear and disappear.
		# Obtain controller for property directly instead of relying on focused control.
		if len(self.controllerFor)>0:
			nvwave.playWaveFile(os.path.join(os.path.dirname(__file__), "suggestion.wav"))
			# For deaf-blind users
			braille.handler.message("suggestions")
		else:
			# Work around broken/odd controller for event implementation in Edge's address omnibar (don't even announce suggestion disappearance when focus moves).
			if self.UIAElement.cachedAutomationID == "addressEditBox" and self != api.getFocusObject():
				return
			# Manually locate live region until NVDA Core implements this.
			obj = self
			while obj is not None:
				if isinstance(obj, UIA) and obj.UIAElement.cachedClassName == "Popup":
					ui.message(obj.description)
					return
				obj = obj.next
			nvwave.playWaveFile(os.path.join(os.path.dirname(__file__), "suggestion1.wav"))

# General suggestions item handler
# A testbed for NVDA Core ticket 6241.
class SuggestionsListItem(UIA):

	def event_UIA_elementSelected(self):
		focusControllerFor=api.getFocusObject().controllerFor
		if len(focusControllerFor)>0 and focusControllerFor[0].appModule is self.appModule and self.name:
			speech.cancelSpeech()
			api.setNavigatorObject(self)
			self.reportFocus()
			# Based on work on NvDA core ticket 6414.
			braille.handler.message(braille.getBrailleTextForProperties(name=self.name, role=self.role, positionInfo=self.positionInfo))

# Some context menu items expose position info, which is quite anoying.
class MenuItemNoPosInfo(UIA):

	def _get_positionInfo(self):
		return {}

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# Hack: Some executables, particularly UWP apps have a dot in the middle.
		# Therefore coerce the app module handler to use the modified routine above.
		# This is no longer the case as of 2016.4 (check if version build var is present, and if not, coerce).
		import versionInfo
		if not hasattr(versionInfo, "version_build"):
			appModuleHandler.getAppModuleFromProcessID = getAppModuleFromProcessID
		# Listen for additional events (to be removed once NVDA Core itself supports them.
		if UIA_ControllerForPropertyId not in UIAHandler.UIAPropertyIdsToNVDAEventNames:
			UIAHandler.UIAPropertyIdsToNVDAEventNames[UIA_ControllerForPropertyId] = "UIA_controllerFor"
			UIAHandler.handler.clientObject.AddPropertyChangedEventHandler(UIAHandler.handler.rootElement,TreeScope_Subtree,UIAHandler.handler.baseCacheRequest,UIAHandler.handler,[UIA_ControllerForPropertyId])
		if UIA_LiveRegionChangedEventId not in UIAHandler.UIAEventIdsToNVDAEventNames:
			UIAHandler.UIAEventIdsToNVDAEventNames[UIA_LiveRegionChangedEventId] = "nameChange"
			UIAHandler.handler.clientObject.addAutomationEventHandler(UIA_LiveRegionChangedEventId,UIAHandler.handler.rootElement,TreeScope_Subtree,UIAHandler.handler.baseCacheRequest,UIAHandler.handler)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			# NVDA Core ticket 5231: Announce values in time pickers.
			# Handle both Threshold and Redstone looping selector items.
			if obj.role==controlTypes.ROLE_LISTITEM and "LoopingSelectorItem" in obj.UIAElement.cachedClassName:
				clsList.append(LoopingSelectorItem)
			# Windows that are really dialogs.
			elif obj.UIAElement.cachedClassName in wintenDialogs:
				# But some are not dialogs despite what UIA says (for example, search popup in Store).
				if obj.UIAElement.cachedAutomationID != "SearchPopUp":
					clsList.insert(0, Dialog)
			# Search field that does raise controller for event.
			# Also take care of Edge address omnibar.
			elif obj.UIAElement.cachedClassName in ("TextBox", "RichEditBox") and obj.UIAElement.cachedAutomationID in ("TextBox", "addressEditBox"):
				clsList.insert(0, SearchField)
			# Suggestions themselves.
			elif obj.role == controlTypes.ROLE_LISTITEM and isinstance(obj.parent, UIA) and obj.parent.UIAElement.cachedAutomationID == "SuggestionsList":
				clsList.insert(0, SuggestionsListItem)
			# Menu items should never expose position info (seen in various context menus such as in Edge).
			elif obj.UIAElement.cachedClassName == "MenuFlyoutItem":
				clsList.insert(0, MenuItemNoPosInfo)

	# Focus announcement hacks.
	def event_gainFocus(self, obj, nextHandler):
		# Never allow WorkerW thread to send gain focus event (seen in Insider builds but was observed in release builds for some).
		if obj.role == controlTypes.ROLE_PANE and obj.appModule.appModuleName == "explorer" and obj.windowClassName == "WorkerW" and obj.name is None:
			return
		# Non-English locales does not fire item selected event for looping selector unless navigator is first set to it.
		if isinstance(obj, UIA) and obj.UIAElement.cachedClassName == "CustomLoopingSelector":
			api.setNavigatorObject(obj.simpleFirstChild)
		nextHandler()
