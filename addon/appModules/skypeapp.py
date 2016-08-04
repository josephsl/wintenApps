# Skype Preview/UWP
# Part of Windows 10 App Essentials
# Copyright 2016 Joseph Lee, released under GPL

# Workarounds for Skype UWP, providing similar features to Skype for Desktop client support (skype.py found in NVDA Core).

import appModuleHandler
import ui
from NVDAObjects.UIA import UIA

class AppModule(appModuleHandler.AppModule):

	def event_nameChange(self, obj, nextHandler):
		if isinstance(obj, UIA):
			uiElement = obj.UIAElement
			if uiElement.cachedClassName == "TextBlock" and obj.next is not None:
				# Announce typing indicator (same as Skype for Desktop).
				nextElement = obj.next.UIAElement
				if nextElement.cachedClassName == "RichEditBox" and nextElement.cachedAutomationID == "ChatEditBox":
					ui.message(obj.name if obj.name != "" else "Typing stopped")
			elif uiElement.cachedAutomationID == "Message" and uiElement.cachedClassName == "ListViewItem" and obj == obj.parent.lastChild:
				ui.message(obj.name)
		nextHandler()
