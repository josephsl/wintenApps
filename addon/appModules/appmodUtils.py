# App module utilities
# Part of Windows App Essentials collection
# Copyright 2023 Joseph Lee, released under GPL

# Adds routines used by various app modules.

from typing import Any
import UIAHandler
from NVDAObjects.UIA import UIA
from NVDAObjects import NVDAObject


def findUIADescendant(self, obj: NVDAObject, uiaProperty: Any, uiaCondition: Any):
	from comtypes import COMError
	clientObject = UIAHandler.handler.clientObject
	condition = clientObject.createPropertyCondition(uiaProperty, uiaCondition)
	walker = clientObject.createTreeWalker(condition)
	uiItemWindow = clientObject.elementFromHandle(obj.windowHandle)
	try:
		element = walker.getFirstChildElement(uiItemWindow)
		element = element.buildUpdatedCache(UIAHandler.handler.baseCacheRequest)
	except (ValueError, COMError):
		raise LookupError("winapps: no UIA descendant found")
	return UIA(UIAElement=element)
