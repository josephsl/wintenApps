# Cortana Conversations
# Part of Windows App Essentials collection
# Copyright 2019-2023 Joseph Lee, released under GPL

# Various workarounds for Cortana Conversations

from typing import Callable, Optional
import appModuleHandler
import api
import ui
import UIAHandler
from NVDAObjects import NVDAObject


class AppModule(appModuleHandler.AppModule):

	def event_UIA_notification(
			self, obj: NVDAObject, nextHandler: Callable[[], None], displayString: Optional[str] = None, **kwargs
	):
		# For some reason Cortana fires this event whenever user types and an answer is received.
		# Results are displayed inside a list.
		# Thus respond to both and see what should be announced.
		if displayString is None or "Cortana" not in displayString:
			return
		# Avoid duplicate speech, more so when Bing search results are returned.
		import speech
		speech.cancelSpeech()
		from . import appmodUtils
		# Thankfully, Cortana's response is part of a grouping object.
		# As long as conversation list uses the same UIA Automation Id,
		# traversal will work across versions (code credit: Abdel with modifications)
		try:
			responses = appmodUtils.findUIADescendant(
				api.getForegroundObject(), UIAHandler.UIA_AutomationIdPropertyId, "ConversationList"
			)
		except LookupError:
			return
		try:
			cortanaResponse = responses.children[-1]
			# Different Automation Id's are used for Cortana responses versus Bing searches.
			if cortanaResponse.UIAAutomationId.startswith("CortanaResponseText"):
				cortanaResponse = cortanaResponse.firstChild.name
			elif cortanaResponse.UIAAutomationId.startswith("CardResponse"):
				# When searching through Bing, summary text shows up.
				if cortanaResponse.firstChild.childCount > 1:
					cortanaResponse = ", ".join([response.name for response in cortanaResponse.firstChild.children])
		except IndexError:
			cortanaResponse = ""
		# Notification event is fired whenever conversations list changes.
		# When displaying results from Bing, Cortana's remark is on its own line (item)
		# followed by actual result (last item).
		try:
			ui.message(cortanaResponse)
		except (IndexError, TypeError):
			# IndexError deals with multi-part mesage,
			# while TypeError deals with a list item with users's message on it.
			pass
