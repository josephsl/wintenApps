# Microsoft Maps
# Part of Windows App Essentials collection
# Copyright 2016-2023 Joseph Lee, released under GPL.

# Numerous enhancements for Bing Maps app.

from typing import Callable, Optional
import appModuleHandler
import api
from NVDAObjects import NVDAObject


class AppModule(appModuleHandler.AppModule):

	def event_UIA_notification(
			self, obj: NVDAObject, nextHandler: Callable[[], None], displayString: Optional[str] = None, **kwargs
	):
		import queueHandler
		import ui
		# Seen when navigating "see more" menu while the app window is snapped to the side.
		if api.getFocusObject() != obj:
			queueHandler.queueFunction(queueHandler.eventQueue, ui.message, displayString)
			return
		nextHandler()
