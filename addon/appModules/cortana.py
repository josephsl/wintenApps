# Cortana Conversations
# Part of Windows 10 App Essentials collection
# Copyright 2019-2020 Joseph Lee, released under GPL

# Various workarounds for Cortana Conversations (in build 18922 and later)

import appModuleHandler
import api
import ui
import controlTypes
import UIAHandler
from NVDAObjects.UIA import UIA


class AppModule(appModuleHandler.AppModule):

	# Sometimes, Cortana's textual response is announced twice.
	_cortanaResponse = ""

	def event_UIA_notification(self, obj, nextHandler, displayString=None, **kwargs):
		# For some reason Cortana fires this event whenever user types and an answer is received.
		# Results are displayed inside a list.
		# Thus respond to both and see what should be announced.
		if displayString is None or "Cortana" not in displayString:
			return
		# Version 1.1910 (beta) changed UIA tree for responses list.
		# 1.1911 (beta) and version 2 changed the tree yet again.
		# Thankfully, Cortana's response is part of a grouping object.
		# As long as conversation list uses the same UIA automation ID,
		# traversal will work across versions (code credit: Abdel)
		clientObject = UIAHandler.handler.clientObject
		condition = clientObject.CreatePropertyCondition(UIAHandler.UIA_AutomationIdPropertyId, "ConversationList")
		cortanaWindow = clientObject.ElementFromHandleBuildCache(
			api.getForegroundObject().windowHandle, UIAHandler.handler.baseCacheRequest
		)
		# Instantiate UIA object directly.
		# In order for this to work, a valid UIA pointer must be returned
		# (value error is seen when Cortana window closes).
		try:
			responses = UIA(
				UIAElement=cortanaWindow.FindFirstBuildCache(
					UIAHandler.TreeScope_Descendants, condition, UIAHandler.handler.baseCacheRequest
				)
			)
		except ValueError:
			return
		try:
			cortanaResponse = responses.children[-1]
			# Since August 2020, different Automation Id's are used for Cortana responses versus Bing searches.
			if cortanaResponse.UIAElement.cachedAutomationId.startswith("CortanaResponseText"):
				cortanaResponse = cortanaResponse.firstChild.name
			elif cortanaResponse.UIAElement.cachedAutomationId.startswith("CardResponse"):
				# When searching through Bing, summary text shows up.
				if cortanaResponse.firstChild.childCount > 1:
					cortanaResponse = ", ".join([response.name for response in cortanaResponse.firstChild.children])
		except IndexError:
			cortanaResponse = ""
		if cortanaResponse != self._cortanaResponse:
			try:
				ui.message(cortanaResponse)
				self._cortanaResponse = cortanaResponse
			except (IndexError, TypeError):
				# IndexError deals with multi-part mesage,
				# while TypeError deals with a list item with users's message on it.
				pass
