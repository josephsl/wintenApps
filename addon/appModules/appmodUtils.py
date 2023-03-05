# App module utilities
# Part of Windows App Essentials collection
# Copyright 2023 Joseph Lee, released under GPL

# Adds routines used by various app modules.

import UIAHandler
from NVDAObjects.UIA import UIA
from NVDAObjects import NVDAObject


def _detectEmptyFolder(self, obj: NVDAObject):
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
	return UIA(UIAElement=element)
