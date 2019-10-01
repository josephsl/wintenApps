# Cortana Conversations (beta)
# Part of Windows 10 App Essentials collection
# Copyright 2019 Joseph Lee, released under GPL

# Various workarounds for Cortana Conversations (beta in build 18922 and later)

import appModuleHandler
import api
import ui

class AppModule(appModuleHandler.AppModule):

	# Sometimes, Cortana's textual response is announced twice.
	_cortanaResponse = ""
	
	def event_UIA_notification(self, obj, nextHandler, displayString=None, **kwargs):
		# For some reason Cortana fires this event whenever user types and answer is received.
		# Results are displayed inside a list.
		# Thus respond to both and see what should be announced.
		if displayString != "Cortana message received.": return
		responses = api.getForegroundObject().firstChild.firstChild.firstChild
		try:
			cortanaResponse = responses.children[-2].name
		except IndexError:
			cortanaResponse = ""
		if cortanaResponse != self._cortanaResponse:
			try:
				ui.message(cortanaResponse)
				self._cortanaResponse = cortanaResponse
			except IndexError:
				pass
