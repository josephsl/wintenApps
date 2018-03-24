# Windows 10 controls repository
# Copyright 2015-2018 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10.
# Since May 2017, suggestions sounds are based on wave files produced by NV Access (copyright 2017).

import os
import globalPluginHandler
import controlTypes
import ui
from NVDAObjects.UIA import UIA, SearchField
from NVDAObjects.behaviors import Dialog, EditableTextWithSuggestions
import api
import speech
import braille
import nvwave
import gui
import wx
import config
import queueHandler
import globalVars
from logHandler import log
import w10config
import addonHandler
addonHandler.initTranslation()

# Extra UIA constants
UIA_Drag_DragStartEventId = 20026
UIA_Drag_DragCancelEventId = 20027
UIA_Drag_DragCompleteEventId = 20028

# For convenience.
W10Events = {
	UIA_Drag_DragStartEventId: "UIA_dragStart",
	UIA_Drag_DragCancelEventId: "UIA_dragCancel",
	UIA_Drag_DragCompleteEventId: "UIA_dragComplete",
}

# UIA COM constants
TreeScope_Subtree = 7

# We know the following elements are dialogs.
wintenDialogs=("Shell_Dialog", "Popup", "Shell_Flyout")

# Looping selectors are used in apps such as Alarms and Clock and Windows Update to select time values.
class LoopingSelectorItem(UIA):

	def event_UIA_elementSelected(self):
		# #19: since February 2017, some looping selectors such as Alarms and Clock exposes correct UIA routines, which results in double announcement.
		# Specifically, looping selector items expose focusable state.
		if 0x1000000 not in self.states:
			speech.cancelSpeech()
			self.reportFocus()

# Looping selector lists.
# Announce selected value if told to do so.
class LoopingSelectorList(UIA):

	def _get_value(self):
		loopingValue = self.simpleFirstChild
		while loopingValue:
			if 4 in loopingValue.states:
				return loopingValue.name
				break
			loopingValue = loopingValue.next
		return None


# General UIA controller for edit field.
# Used as a base class for controls such as Mail's composition window, search fields and such.
class UIAEditableTextWithSuggestions(EditableTextWithSuggestions, UIA):

	def event_UIA_controllerFor(self):
		# Obtain controller for property directly instead of relying on focused control.
		if len(self.controllerFor)>0:
			self.event_suggestionsOpened()
		else:
			self.event_suggestionsClosed()

# Search fields.
# Unlike the Core implementation, this class announces suggestion count, to be incorporated into NVDA later.
class SearchField(SearchField):

	def event_suggestionsOpened(self):
		super(SearchField, self).event_suggestionsOpened()
		# Announce number of items found (except in Start search box where the suggestions are selected as user types).
		# Oddly, Edge's address omnibar returns 0 for suggestion count when there are clearly suggestions (implementation differences).
		# Because inaccurate count could be announced (when users type, suggestion count changes), thus announce this if position info reporting is enabled.
		if config.conf["presentation"]["reportObjectPositionInformation"]:
			if self.UIAElement.cachedAutomationID == "TextBox" or self.UIAElement.cachedAutomationID == "SearchTextBox" and self.appModule.appName != "searchui":
				# Item count must be the last one spoken.
				suggestionsCount = self.controllerFor[0].childCount
				suggestionsMessage = "1 suggestion" if suggestionsCount == 1 else "%s suggestions"%suggestionsCount
				queueHandler.queueFunction(queueHandler.eventQueue, ui.message, suggestionsMessage)

	def event_suggestionsClosed(self):
		# Work around broken/odd controller for event implementation in Edge's address omnibar (don't even announce suggestion disappearance when focus moves).
		if self.UIAElement.cachedAutomationID == "addressEditBox" and self != api.getFocusObject():
			return
		nvwave.playWaveFile(r"waves\suggestionsClosed.wav")

# Contacts search field in People app and other places.
# An ugly hack to prevent suggestion founds from repeating.
_playSuggestionsSounds = False

# For UIA search fields that does not raise any controller for at all.
class QueryInputTextBox(EditableTextWithSuggestions, UIA):

	def event_valueChange(self):
		global _playSuggestionsSounds
		if len(self.value) and self.simpleNext.firstChild.role == controlTypes.ROLE_LISTITEM:
			if not _playSuggestionsSounds:
				super(QueryInputTextBox, self).event_suggestionsOpened()
				_playSuggestionsSounds = True
		elif len(self.value) == 0:
			_playSuggestionsSounds = False


# Some context menu items expose position info, which is quite anoying.
class MenuItemNoPosInfo(UIA):

	def _get_positionInfo(self):
		return {}


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# #20: don't even think about proceeding in secure screens (especially add-on updates).
		if globalVars.appArgs.secure: return
		# #40: skip over the rest if appx is in effect.
		if hasattr(config, "isAppX") and config.isAppX: return
		# Add extra things for UIA support if required.
		import UIAHandler
		# UIA 5 is part of build 16299 and later.
		# #42: and is also part of NVDA 2018.1 and later.
		if hasattr(UIAHandler, "IUIAutomation5") and not isinstance(UIAHandler.handler.clientObject, UIAHandler.IUIAutomation5):
			log.debug("W10: older UIA interface is in use, attempting to upgrade to latest interface for this session via handler object replacement")
			if hasattr(UIAHandler, "IUIAutomation5"):
				UIAHandler.terminate()
				# Hack: add extra events and such via an extended UIAHandler class.
				from . import _UIAHandlerEx
				try:
					UIAHandler.handler=_UIAHandlerEx.UIAHandlerEx()
				except:
					UIAHandler.handler=None
			else:
				log.debug("W10: IUIAutomation5 not found, falling back to IUIAutomation3")
		# Add a series of events instead of doing it one at a time.
		log.debug("W10: adding additional events")
		for event, name in W10Events.items():
			if event not in UIAHandler.UIAEventIdsToNVDAEventNames:
				UIAHandler.UIAEventIdsToNVDAEventNames[event] = name
				UIAHandler.handler.clientObject.addAutomationEventHandler(event,UIAHandler.handler.rootElement,TreeScope_Subtree,UIAHandler.handler.baseCacheRequest,UIAHandler.handler)
		self.prefsMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.w10Settings = self.prefsMenu.Append(wx.ID_ANY, _("&Windows 10 App Essentials..."), _("Windows 10 App Essentials add-on settings"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, w10config.onConfigDialog, self.w10Settings)
		if w10config.canUpdate and config.conf["wintenApps"]["autoUpdateCheck"]:
			# But not when NVDA itself is updating.
			if not (globalVars.appArgs.install and globalVars.appArgs.minimal):
				wx.CallAfter(w10config.autoUpdateCheck)

	def terminate(self):
		super(GlobalPlugin, self).terminate()
		try:
			self.prefsMenu.RemoveItem(self.w10Settings)
		except (RuntimeError, AttributeError, wx.PyDeadObjectError):
			pass
		if w10config.updateChecker and w10config.updateChecker.IsRunning():
			w10config.updateChecker.Stop()
		w10config.updateChecker = None

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			# NVDA Core ticket 5231: Announce values in time pickers.
			if obj.role==controlTypes.ROLE_LISTITEM and "LoopingSelectorItem" in obj.UIAElement.cachedClassName:
				clsList.append(LoopingSelectorItem)
			# Also announce values when focus moves to it.
			elif obj.role==controlTypes.ROLE_LIST and "LoopingSelector" in obj.UIAElement.cachedClassName:
				clsList.insert(0, LoopingSelectorList)
			# Windows that are really dialogs.
			elif obj.UIAElement.cachedClassName in wintenDialogs:
				# But some are not dialogs despite what UIA says (for example, search popup in Store).
				if obj.UIAElement.cachedAutomationID != "SearchPopUp":
					clsList.insert(0, Dialog)
			# Search field that does raise controller for event.
			# Also take care of Edge address omnibar and Start search box.
			# This is no longer necessary in NVDA 2017.3 (incubating as of May 2017).
			elif obj.UIAElement.cachedAutomationID in ("SearchTextBox", "TextBox", "addressEditBox"):
				# NVDA 2017.3 includes a dedicated search box over class in searchui to deal with search term announcement problem.
				if obj.UIAElement.cachedAutomationID in ("SearchTextBox", "TextBox") and obj.appModule.appName != "searchui":
					clsList.insert(0, SearchField)
			# A dedicated version for Mail app's address/mention suggestions.
			elif obj.UIAElement.cachedAutomationID == "RootFocusControl":
				clsList.insert(0, UIAEditableTextWithSuggestions)
			# Some search fields does not raise controller for but suggestions are next to them.
			elif obj.UIAElement.cachedAutomationID == "QueryInputTextBox":
				clsList.insert(0, QueryInputTextBox)
			# Menu items should never expose position info (seen in various context menus such as in Edge).
			elif obj.UIAElement.cachedClassName == "MenuFlyoutItem":
				clsList.insert(0, MenuItemNoPosInfo)

	# Record UIA property info about an object if debug logging is enabled.
	def uiaDebugLogging(self, obj, event=None):
		if isinstance(obj, UIA) and globalVars.appArgs.debugLogging:
			element = obj.UIAElement
			if not obj.name:
				obj.name = "unavailable"
			automationID = element.cachedAutomationID
			if not automationID: automationID = "unavailable"
			className = element.cachedClassName
			if not className: className = "unavailable"
			if not event:
				event = "no event specified"
			if event != "controllerFor":
				log.debug("W10: UIA object name: %s, event: %s, app module: %s, automation Id: %s, class name: %s"%(obj.name, event, obj.appModule, automationID, className))
			else:
				log.debug("W10: UIA object name: %s, event: %s, app module: %s, automation Id: %s, class name: %s, controller for count: %s"%(obj.name, event, obj.appModule, automationID, className, len(obj.controllerFor)))

	# Focus announcement hacks.
	def event_gainFocus(self, obj, nextHandler):
		# Non-English locales does not fire item selected event for looping selector unless navigator is first set to it.
		if isinstance(obj, UIA) and obj.UIAElement.cachedClassName == "CustomLoopingSelector":
			api.setNavigatorObject(obj.simpleFirstChild)
		nextHandler()

	def event_nameChange(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "nameChange")
		nextHandler()

	def event_valueChange(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "valueChange")
		nextHandler()

	def event_UIA_controllerFor(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "controllerFor")
		nextHandler()

	def event_liveRegionChange(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "liveRegionChange")
		nextHandler()

	def event_UIA_elementSelected(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "elementSelected")
		nextHandler()

	def event_UIA_systemAlert(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "systemAlert")
		nextHandler()

	def event_UIA_window_windowOpen(self, obj, nextHandler):
		# Specifically in order to debug multiple toast announcements.
		self.uiaDebugLogging(obj, "windowOpen")
		nextHandler()

	def event_UIA_notification(self, obj, nextHandler, notificationKind=None, notificationProcessing=None, displayString=None, activityId=None):
		# Introduced in Version 1709, to be treated as a notification event.
		self.uiaDebugLogging(obj, "notification")
		if isinstance(obj, UIA) and globalVars.appArgs.debugLogging:
			log.debug("W10: UIA notification: sender: %s, notification kind: %s, notification processing: %s, display string: %s, activity ID: %s"%(obj.UIAElement,notificationKind,notificationProcessing,displayString,activityId))
			import tones
			# For debugging purposes.
			tones.beep(500, 100)
		# Some apps still fire both live region change and notification events, including Calculator.
		if isinstance(obj, UIA) and not hasattr(obj, "event_UIA_notification"):
			# As long as this add-on supports Version 1703, keep a notification blacklist handy.
			# Also, do not announce notifications from background apps.
			# Work around anoying notifications from Feedback Hub whenever category is selected.
			if obj.appModule.appName in ("calculator",) or activityId in ("CategoryChangedContext",): return
			if obj.appModule == api.getFocusObject().appModule:
				ui.message(displayString)
		nextHandler()

	def event_UIA_dragStart(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragStart")
		nextHandler()

	def event_UIA_dragCancel(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragCancel")
		nextHandler()

	def event_UIA_dragComplete(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "dragComplete")
		nextHandler()

	def event_UIA_toolTipOpened(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "tooltipOpened")
		# Only XAML tooltips will be announced at this time.
		if obj.UIAElement.cachedFrameworkID == "XAML": ui.message(obj.name)
