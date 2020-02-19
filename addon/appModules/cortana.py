# Cortana Conversations (beta)
# Part of Windows 10 App Essentials collection
# Copyright 2019-2020 Joseph Lee, released under GPL

# Various workarounds for Cortana Conversations (beta in build 18922 and later)

import appModuleHandler
import api
import ui
import controlTypes

class AppModule(appModuleHandler.AppModule):

	# Sometimes, Cortana's textual response is announced twice.
	_cortanaResponse = ""

	def event_UIA_notification(self, obj, nextHandler, displayString=None, **kwargs):
		# For some reason Cortana fires this event whenever user types and answer is received.
		# Results are displayed inside a list.
		# Thus respond to both and see what should be announced.
		if displayString != "Cortana message received.": return
		# Version 1.1910 (beta) changed UIA tree for responses list.
		# 1.1911 (beta) and version 2 changed the tree yet again.
		# Thankfully, Cortana's response is part of a grouping object.
		responses = api.getForegroundObject().children[1].firstChild.firstChild
		try:
			cortanaResponse = responses.children[-1]
			if cortanaResponse.firstChild.role == controlTypes.ROLE_GROUPING:
				cortanaResponse = cortanaResponse.firstChild.firstChild
				# When searching through Bing, summary text shows up.
				if cortanaResponse.childCount > 1:
					cortanaResponse = ", ".join([response.name for response in cortanaResponse.children])
				else: cortanaResponse = cortanaResponse.name
		except IndexError:
			cortanaResponse = ""
		if cortanaResponse != self._cortanaResponse:
			try:
				ui.message(cortanaResponse)
				self._cortanaResponse = cortanaResponse
			except IndexError:
				pass
