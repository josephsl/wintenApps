# Skype Preview/UWP
# Part of Windows 10 App Essentials
# Copyright 2016 Joseph Lee, released under GPL

# Workarounds for Skype UWP, providing similar features to Skype for Desktop client support (skype.py found in NVDA Core).

import re
import appModuleHandler
import ui
from NVDAObjects.UIA import UIA
import api

class AppModule(appModuleHandler.AppModule):

	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		for pos in xrange(10):
			self.bindGesture("kb:control+nvda+%s"%pos, "readMessage")

	# Borrowed from Skype for Desktop app module (NVDA Core).
	RE_MESSAGE = re.compile(r"^From (?P<from>.*), (?P<body>.*), sent on (?P<time>.*?)(?: Edited by .* at .*?)?(?: Not delivered|New)?$")

	def reportMessage(self, message):
		# Just like Desktop client, messages are quite verbose.
		m = self.RE_MESSAGE.match(message)
		if m:
			message = "%s, %s" % (m.group("from"), m.group("body"))
		ui.message(message)

	def event_nameChange(self, obj, nextHandler):
		if isinstance(obj, UIA):
			uiElement = obj.UIAElement
			if uiElement.cachedClassName == "TextBlock" and obj.next is not None:
				# Announce typing indicator (same as Skype for Desktop).
				nextElement = obj.next.UIAElement
				if nextElement.cachedClassName == "RichEditBox" and nextElement.cachedAutomationID == "ChatEditBox":
					# Translaotrs: Presented when someone stops typing in Skype app (same as Skype for Desktop).
					ui.message(obj.name if obj.name != "" else _("Typing stopped"))
			elif uiElement.cachedAutomationID == "Message" and uiElement.cachedClassName == "ListViewItem":
				self.reportMessage(obj.name)
		nextHandler()

	def script_readMessage(self, gesture):
		# Foreground isn't reliable, so need to locate the actual chat contents list.
		fg = api.getForegroundObject()
		if fg.getChild(1).childCount > 0:
			screenContent = fg.getChild(1)
		else:
			screenContent = fg.getChild(2)
		# Position of chat history in object hierarchy changes based on which tabv is active.
		# Wish there is a more elegant way to do this...
		for element in screenContent.children:
			if isinstance(element, UIA) and element.UIAElement.cachedAutomationID == "chatMessagesListView":
				pos = int(gesture.displayName[-1])
				if pos == 0: pos += 10
				try:
					message = element.getChild(0-pos)
					api.setNavigatorObject(message)
					self.reportMessage(message.name)
					return
				except IndexError:
					return
		# Translators: Presented when message history isn't found in Skype Preview app.
		ui.message(_("Chat history not found"))
	# Translators: Input help mode message for a command in Skype Preview app.
	script_readMessage.__doc__ = _("Reports and moves the review cursor to a recent message")
