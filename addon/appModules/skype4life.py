#appModules/skype4life.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2018 NV Access Limited, Joseph Lee
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""Routines for universal app version of Skype, version 14."""

import appModuleHandler
import ui
from NVDAObjects.UIA import UIA
from nvdaBuiltin.appModules.skype import SCRCAT_SKYPE
import api
import addonHandler
addonHandler.initTranslation()

class AppModule(appModuleHandler.AppModule):

	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		# Used "range" function due to Python 3 compatibility.
		for pos in range(10):
			self.bindGesture("kb:control+nvda+%s"%pos, "readMessage")

	# Keep an eye on various elements.
	_skype14Elements = {}

	# Locate various elements, as this is one of the best ways to do this in Skype UWP.
	# In version 14, there are no automation ID's or class names for many elements, so tree traversal is the usual way for this.
	# A constant (past automation iD's) will be used to select which element to fetch, as it'll be pulled from an elements map for performance reasons
	def locateElement(self, element):
		if element in self._skype14Elements:
			return self._skype14Elements[element]
		# Foreground isn't reliable.
		fg = api.getForegroundObject()
		if fg.getChild(1).childCount > 0:
			screenContent = fg.getChild(1)
		else:
			screenContent = fg.getChild(2)
		# Thanks to My Peple in Fall Creators Update, screen content so far could actually be the title bar, and the actual foreground window is next door.
		# In other words, Skype window is embedded inside My People window.
		if screenContent.UIAElement.cachedAutomationID == "TitleBar":
			# The following traversal path may change in future builds.
			screenContent = screenContent.next.simpleLastChild.simpleFirstChild
		# Element placement (according to UIA changes from time to time.
		# Wish there is a more elegant way to do this...
		# In version 14, children isn't reliable (a lot of singletons and such), so resort to simple object navigation.
		obj = screenContent.simpleLastChild.simplePrevious.simplePrevious
		if element == "ChatEditBox":
			self._skype14Elements[element] = obj
		elif element == "chatMessagesListView":
			self._skype14Elements[element] = obj.simplePrevious.simplePrevious.parent
			obj = obj.simplePrevious.simplePrevious.parent
		else: obj = None
		return obj

	def script_readMessage(self, gesture):
		chatHistory = self.locateElement("chatMessagesListView")
		# Position of chat history in object hierarchy changes based on which tabv is active.
		# Wish there is a more elegant way to do this...
		if chatHistory is None:
			# Translators: Presented when message history isn't found in Skype Preview app.
			ui.message(_("Chat history not found"))
			return
		pos = int(gesture.displayName[-1])
		if pos == 0: pos += 10
		try:
			message = chatHistory.getChild(0-pos)
			api.setNavigatorObject(message)
			if hasattr(message, "getShortenedMessage"):
				ui.message(message.getShortenedMessage())
			else:
				ui.message(message.name)
			return
		except IndexError:
			return
	# Translators: Input help mode message for a command in Skype Preview app.
	script_readMessage.__doc__ = _("Reports and moves the review cursor to a recent message")

	def script_moveToChatEditField(self, gesture):
		element = self.locateElement("ChatEditBox")
		if element is not None:
			element.setFocus()
		else:
			# Translators: presented when chat edit box is not found.
			ui.message(_("Chat edit field not found"))

	__gestures={
		"kb:alt+4":"moveToChatEditField",
	}
