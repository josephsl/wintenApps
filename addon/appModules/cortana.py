# Cortana Conversations
# Part of Windows App Essentials collection
# Copyright 2019-2023 Joseph Lee, released under GPL

# Various workarounds for Cortana Conversations

from typing import Callable, Optional
import appModuleHandler
import api
import ui
import UIAHandler
from NVDAObjects.UIA import UIA
from NVDAObjects import NVDAObject


class AppModule(appModuleHandler.AppModule):

	# Responses will be announced twice if returning results from Bing
	# as NVDA looks for last item in conversations list.
	_cortanaResponse: str = ""

	def event_UIA_notification(
			self, obj: NVDAObject, nextHandler: Callable[[], None], displayString: Optional[str] = None, **kwargs
	):
		# For some reason Cortana fires this event whenever user types and an answer is received.
		# Results are displayed inside a list.
		# Thus respond to both and see what should be announced.
		if displayString is None or "Cortana" not in displayString:
			return
		from comtypes import COMError
		# Thankfully, Cortana's response is part of a grouping object.
		# As long as conversation list uses the same UIA Automation Id,
		# traversal will work across versions (code credit: Abdel with modifications)
		clientObject = UIAHandler.handler.clientObject
		condition = clientObject.createPropertyCondition(UIAHandler.UIA_AutomationIdPropertyId, "ConversationList")
		walker = clientObject.createTreeWalker(condition)
		cortanaWindow = clientObject.elementFromHandle(api.getForegroundObject().windowHandle)
		# (value error is seen when Cortana window closes).
		try:
			element = walker.getFirstChildElement(cortanaWindow)
			element = element.buildUpdatedCache(UIAHandler.handler.baseCacheRequest)
		except (ValueError, COMError):
			return
		responses = UIA(UIAElement=element)
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
		if cortanaResponse != self._cortanaResponse:
			try:
				ui.message(cortanaResponse)
				self._cortanaResponse = cortanaResponse
			except (IndexError, TypeError):
				# IndexError deals with multi-part mesage,
				# while TypeError deals with a list item with users's message on it.
				pass
