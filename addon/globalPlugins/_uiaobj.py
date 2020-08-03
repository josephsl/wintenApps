# Windows 10 controls repository
# Copyright 2015-2020 Joseph Lee, released under GPL.

# Temporary module to add a patched version of UIA.findOverlayClasses to avoid COM errors when fetching Automation Id property.

import controlTypes
import NVDAObjects.UIA
from NVDAObjects.UIA import *
import config
import UIAHandler
from logHandler import log


# Temporary patch: catch COM error exception when automation ID cannot be fetched.
def findOverlayClassesEx(self,clsList):
	UIAControlType=self.UIAElement.cachedControlType
	UIAClassName=self.UIAElement.cachedClassName
	try:
		UIAAutomationID=self._getUIACacheablePropertyValue(UIAHandler.UIA_AutomationIdPropertyId)
	except COMError:
		UIAAutomationID=""
	if UIAClassName=="NetUITWMenuItem" and UIAControlType==UIAHandler.UIA_MenuItemControlTypeId and not self.name and not self.previous:
		# Bounces focus from a netUI dead placeholder menu item when no item is selected up to the menu itself.
		clsList.append(PlaceholderNetUITWMenuItem)
	elif UIAClassName=="WpfTextView":
		clsList.append(WpfTextView)
	elif UIAClassName=="NetUIDropdownAnchor":
		clsList.append(NetUIDropdownAnchor)
	elif self.TextInfo==UIATextInfo and (UIAClassName=='_WwG' or self.windowClassName=='_WwG' or UIAAutomationID.startswith('UIA_AutomationId_Word_Content')):
		from NVDAObjects.UIA.wordDocument import WordDocument, WordDocumentNode
		if self.role==controlTypes.ROLE_DOCUMENT:
			clsList.append(WordDocument)
		else:
			clsList.append(WordDocumentNode)
	# #5136: Windows 8.x and Windows 10 uses different window class and other attributes for toast notifications.
	elif UIAClassName=="ToastContentHost" and UIAControlType==UIAHandler.UIA_ToolTipControlTypeId: #Windows 8.x
		clsList.append(Toast_win8)
	elif self.windowClassName=="Windows.UI.Core.CoreWindow" and UIAControlType==UIAHandler.UIA_WindowControlTypeId and "ToastView" in UIAAutomationID: # Windows 10
		clsList.append(Toast_win10)
	# #8118: treat UIA tool tips (including those found in UWP apps) as proper tool tips, especially those found in Microsoft Edge and other apps.
	# Windows 8.x toast, although a form of tool tip, is covered separately.
	elif UIAControlType==UIAHandler.UIA_ToolTipControlTypeId:
		clsList.append(ToolTip)
	elif(
		self.UIAElement.cachedFrameworkID in ("InternetExplorer", "MicrosoftEdge")
		# But not for Internet Explorer
		and not self.appModule.appName == 'iexplore'
	):
		from NVDAObjects.UIA import edge
		if UIAClassName in ("Internet Explorer_Server","WebView") and self.role==controlTypes.ROLE_PANE:
			clsList.append(edge.EdgeHTMLRootContainer)
		elif (self.UIATextPattern and
			# #6998: Edge normally gives its root node a controlType of pane, but ARIA role="document"  changes the controlType to document
			self.role in (controlTypes.ROLE_PANE,controlTypes.ROLE_DOCUMENT) and 
			self.parent and (isinstance(self.parent,edge.EdgeHTMLRootContainer) or not isinstance(self.parent,edge.EdgeNode))
		): 
			clsList.append(edge.EdgeHTMLRoot)
		elif self.role==controlTypes.ROLE_LIST:
			clsList.append(edge.EdgeList)
		else:
			clsList.append(edge.EdgeNode)
	elif self.role==controlTypes.ROLE_DOCUMENT and UIAAutomationID=="Microsoft.Windows.PDF.DocumentView":
		# PDFs
		from NVDAObjects.UIA import edge
		clsList.append(edge.EdgeHTMLRoot)
	elif (
		"DevExpress.XtraRichEdit" in self.UIAElement.cachedProviderDescription
		and UIAAutomationID == "RichEditControl"
	):
		clsList.insert(0, DevExpressXtraRichEdit)
	if UIAControlType == UIAHandler.UIA_ProgressBarControlTypeId:
		clsList.append(ProgressBar)
	if UIAClassName=="ControlPanelLink":
		clsList.append(ControlPanelLink)
	if UIAClassName=="UIColumnHeader":
		clsList.append(UIColumnHeader)
	elif UIAClassName=="UIItem":
		clsList.append(UIItem)
	elif UIAClassName=="SensitiveSlider":
		clsList.append(SensitiveSlider) 
	if UIAControlType==UIAHandler.UIA_TreeItemControlTypeId:
		clsList.append(TreeviewItem)
	if UIAControlType==UIAHandler.UIA_MenuItemControlTypeId:
		clsList.append(MenuItem)
	# Some combo boxes and looping selectors do not expose value pattern.
	elif (UIAControlType==UIAHandler.UIA_ComboBoxControlTypeId
	# #5231: Announce values in time pickers by "transforming" them into combo box without value pattern objects.
	or (UIAControlType==UIAHandler.UIA_ListControlTypeId and "LoopingSelector" in UIAClassName)):
		try:
			if not self._getUIACacheablePropertyValue(UIAHandler.UIA_IsValuePatternAvailablePropertyId):
				clsList.append(ComboBoxWithoutValuePattern)
		except COMError:
			pass
	elif UIAControlType==UIAHandler.UIA_ListItemControlTypeId:
		clsList.append(ListItem)
	# #5942: In Windows 10 build 14332 and later, Microsoft rewrote various dialog code including that of User Account Control.
	# #8405: there are more dialogs scattered throughout Windows 10 and various apps.
	# Dialog detection is a bit easier on build 17682 and later thanks to IsDialog property.
	try:
		isDialog = self._getUIACacheablePropertyValue(UIAHandler.UIA_IsDialogPropertyId)
	except COMError:
		# We can fallback to a known set of dialog classes for window elements.
		isDialog = (self.UIAIsWindowElement and UIAClassName in UIAHandler.UIADialogClassNames)
	if isDialog:
		clsList.append(Dialog)
	# #6241: Try detecting all possible suggestions containers and search fields scattered throughout Windows 10.
	try:
		if UIAAutomationID in ("SearchTextBox", "TextBox"):
			clsList.append(SearchField)
	except COMError:
		log.debug("Failed to locate UIA search field", exc_info=True)
	try:
		# Nested block here in order to catch value error and variable binding error when attempting to access automation ID for invalid elements.
		try:
			# #6241: Raw UIA base tree walker is better than simply looking at self.parent when locating suggestion list items.
			# #10329: 2019 Windows Search results require special handling due to UI redesign.
			parentElement=UIAHandler.handler.baseTreeWalker.GetParentElementBuildCache(self.UIAElement,UIAHandler.handler.baseCacheRequest)
			# Sometimes, fetching parent (list control) via base tree walker fails, especially when dealing with suggestions in Windows10 Start menu.
			# Oddly, we need to take care of context menu for Start search suggestions as well.
			if parentElement.cachedAutomationId.lower() in ("suggestionslist", "contextmenu"):
				clsList.append(SuggestionListItem)
		except COMError:
			pass
	except ValueError:
		pass

	# Support Windows Console's UIA interface
	if (
		self.windowClassName == "ConsoleWindowClass"
		and config.conf['UIA']['winConsoleImplementation'] == "UIA"
	):
		from NVDAObjects.UIA import winConsoleUIA
		winConsoleUIA.findExtraOverlayClasses(self, clsList)
	elif UIAClassName == "TermControl":
		from NVDAObjects.UIA import winConsoleUIA
		clsList.append(winConsoleUIA.WinTerminalUIA)

	# Add editableText support if UIA supports a text pattern
	if self.TextInfo==UIATextInfo:
		if UIAHandler.autoSelectDetectionAvailable:
			clsList.append(EditableTextWithAutoSelectDetection)
		else:
			clsList.append(EditableTextWithoutAutoSelectDetection)

	clsList.append(UIA)

	if self.UIAIsWindowElement:
		super(UIA,self).findOverlayClasses(clsList)
		if self.UIATextPattern:
			#Since there is a UIA text pattern, there is no need to use the win32 edit support at all
			import NVDAObjects.window.edit
			for x in list(clsList):
				if issubclass(x,NVDAObjects.window.edit.Edit):
					clsList.remove(x)
