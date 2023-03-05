# App module utilities
# Part of Windows App Essentials collection
# Copyright 2023 Joseph Lee, released under GPL

# Adds routines used by various app modules.

from typing import Callable, Optional
import appModuleHandler
import api
import ui
import UIAHandler
from NVDAObjects.UIA import UIA
from NVDAObjects import NVDAObject


def _detectEmptyFolder(self, obj: NVDAObject):
	import UIAHandler
	from comtypes import COMError
	clientObject = UIAHandler.handler.clientObject
	condition = clientObject.createPropertyCondition(UIAHandler.UIA_ClassNamePropertyId, "UIItemsView")
	walker = clientObject.createTreeWalker(condition)
	uiItemWindow = clientObject.elementFromHandle(obj.windowHandle)
	try:
		element = walker.getFirstChildElement(uiItemWindow)
		element = element.buildUpdatedCache(UIAHandler.handler.baseCacheRequest)
	except (ValueError, COMError):
		return
	lastUIItem = UIA(UIAElement=element).lastChild
	# NVDA Core issue 5759: announce empty folder text.
	if (
		isinstance(lastUIItem, UIA)
		and lastUIItem.role == controlTypes.Role.STATICTEXT
		and lastUIItem.UIAElement.currentClassName == "Element"
	):
		ui.message(lastUIItem.name)
