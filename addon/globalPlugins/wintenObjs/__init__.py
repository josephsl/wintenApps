# Windows 10 controls repository
# Copyright 2015-2018 Joseph Lee, released under GPL.

# Adds handlers for various UIA controls found in Windows 10.

import os
import globalPluginHandler
import controlTypes
import ui
from NVDAObjects.UIA import UIA, SearchField, Dialog
from NVDAObjects.behaviors import EditableTextWithSuggestions, ToolTip
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
# RS5/IUIAutomation6
UIA_ActiveTextPositionChangedEventId = 20036
# RS4/IUIAutomationElement8
UIA_HeadingLevelPropertyId = 30173
# RS5/IUIAutomationElement9
UIA_IsDialogPropertyId = 30174 # Let NVDA and others detect a dialog element and read element content.

# For convenience.
W10Events = {
	UIA_Drag_DragStartEventId: "UIA_dragStart",
	UIA_Drag_DragCancelEventId: "UIA_dragCancel",
	UIA_Drag_DragCompleteEventId: "UIA_dragComplete",
}

# UIA COM constants
TreeScope_Subtree = 7

# We know the following elements are dialogs.
wintenDialogs=("Shell_Dialog", "Popup", "Shell_Flyout", "Shell_SystemDialog")

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
# An ugly hack to prevent suggestion sounds from repeating.
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


# For tool tips from universal apps and Edge.
class ToolTip(ToolTip, UIA):

	event_UIA_toolTipOpened=ToolTip.event_show


class XAMLHeading(UIA):

	def _get_role(self):
		return self._getUIACacheablePropertyValue(30173) - 80010


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# #20: don't even think about proceeding in secure screens (especially add-on updates).
		if globalVars.appArgs.secure: return
		# #40: skip over the rest if appx is in effect.
		if config.isAppX: return
		import UIAHandler
		import sys
		# Add a series of events instead of doing it one at a time.
		# Some events are only available in a specific build range.
		log.debug("W10: adding additional events")
		if sys.getwindowsversion().build >= 17692:
			log.debug("W10: adding additional events for RS5")
			W10Events[UIA_ActiveTextPositionChangedEventId] = "UIA_activeTextPositionChanged"
		for event, name in W10Events.items():
			if event not in UIAHandler.UIAEventIdsToNVDAEventNames:
				UIAHandler.UIAEventIdsToNVDAEventNames[event] = name
				UIAHandler.handler.clientObject.addAutomationEventHandler(event,UIAHandler.handler.rootElement,TreeScope_Subtree,UIAHandler.handler.baseCacheRequest,UIAHandler.handler)
				log.debug("W10: added event ID %s, assigned to %s"%(event, name))
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
			# NVDA Core ticket 5231: Announce values in time pickers, especially when focus moves to looping selector list.
			if obj.role==controlTypes.ROLE_LIST and "LoopingSelector" in obj.UIAElement.cachedClassName:
				clsList.insert(0, LoopingSelectorList)
			# Windows that are really dialogs.
			# NVDA Core issue 8405: in build 17682 and later, IsDialog property has been added, making comparisons easier.
			# However, don't forget that many users are still using old Windows 10 releases.
			isDialog = False
			try:
				if obj._getUIACacheablePropertyValue(UIA_IsDialogPropertyId):
					isDialog = True
					import tones
					tones.beep(200, 50)
			except:
				pass
			# For build 17134 and earlier.
			if not isDialog and obj.UIAElement.cachedClassName in wintenDialogs:
				# But some are not dialogs despite what UIA says (for example, search popup in Store).
				if obj.UIAElement.cachedAutomationID != "SearchPopUp":
					isDialog = True
			if isDialog:
				self.uiaDebugLogging(obj, "isDialog")
			if isDialog and Dialog not in clsList:
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
			# #44: Recognize XAML/UWP tool tips.
			elif obj.UIAElement.cachedClassName == "ToolTip" and obj.UIAElement.cachedFrameworkID == "XAML":
				# Just in case XAML tool tip support is part of NVDA...
				import NVDAObjects.UIA
				if not hasattr(NVDAObjects.UIA, "ToolTip"):
					clsList.insert(0, ToolTip)
			# Recognize headings as reported by XAML (build 17134 and later).
			try:
				if obj._getUIACacheablePropertyValue(30173) > 80050:
					clsList.insert(0, XAMLHeading)
			except:
				pass

	# Record UIA property info about an object if debug logging is enabled.
	def uiaDebugLogging(self, obj, event=None):
		if isinstance(obj, UIA) and globalVars.appArgs.debugLogging:
			info = ["object: %s"%repr(obj)]
			info.append("name: %s"%obj.name)
			if not event:
				event = "no event specified"
			info.append("event: %s"%event)
			info.append("app module: %s"%obj.appModule)
			element = obj.UIAElement
			info.append("automation Id: %s"%element.cachedAutomationID)
			info.append("class name: %s"%element.cachedClassName)
			if event == "controllerFor":
				info.append("controller for count: %s"%len(obj.controllerFor))
			elif event == "tooltipOpened":
				info.append("framework Id: %s"%element.cachedFrameworkId)
			log.debug(u"W10: UIA {debuginfo}".format(debuginfo = ", ".join(info)))

	# Focus announcement hacks.
	def event_gainFocus(self, obj, nextHandler):
		# Non-English locales does not fire item selected event for looping selector unless navigator is first set to it.
		if isinstance(obj, UIA) and obj.UIAElement.cachedClassName == "CustomLoopingSelector":
			api.setNavigatorObject(obj.simpleFirstChild)
		nextHandler()

	def event_nameChange(self, obj, nextHandler):
		# NVDA Core issue 5641: try catching virtual desktop switch event, which will result in name change for the desktop object.
		# To be taken care of by NVDA Core, and for older releases, let the add-on handle it for a time.
		if obj.windowClassName == "#32769":
			import eventHandler
			if not hasattr(eventHandler, "handlePossibleDesktopNameChange"):
				wx.CallLater(500, ui.message, obj.name)
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
		if isinstance(obj, UIA):
			# #50 (NVDA Core issue 8466): certain aria-alert messages.
			if obj.role == controlTypes.ROLE_ALERT:
				if obj.name == "" and obj.treeInterceptor is not None:
					obj.name = obj.treeInterceptor.makeTextInfo(obj).text
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
		nextHandler()

	def event_UIA_activeTextPositionChanged(self, obj, nextHandler):
		self.uiaDebugLogging(obj, "activeTextPositionChanged")
		import tones
		# For debugging purposes.
		tones.beep(250, 100)
		nextHandler()
