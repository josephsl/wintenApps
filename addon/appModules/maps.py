# Microsoft Maps
# Part of Windows App Essentials collection
# Copyright 2016-2023 Joseph Lee, released under GPL.

# Numerous enhancements for Bing Maps app.

from typing import List, Callable, Optional
import appModuleHandler
import api
import config
from NVDAObjects.UIA import UIA
from NVDAObjects import NVDAObject
import tones


class AppModule(appModuleHandler.AppModule):

	def event_UIA_notification(
			self, obj: NVDAObject, nextHandler: Callable[[], None], displayString: Optional[str] = None, **kwargs
	):
		import queueHandler
		import ui
		if api.getFocusObject() != obj:
			queueHandler.queueFunction(queueHandler.eventQueue, ui.message, displayString)
			return
		nextHandler()
