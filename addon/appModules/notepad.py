# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2022-2023 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for Windows Notepad.
While this app module also covers older Notepad releases,
this module provides workarounds for Windows 11 Notepad."""

from typing import Callable
from comtypes import COMError
import appModuleHandler
import api
import braille
import controlTypes
import eventHandler
import speech
import UIAHandler
from NVDAObjects.UIA import UIA
from NVDAObjects import NVDAObject


class AppModule(appModuleHandler.AppModule):

	def event_UIA_elementSelected(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# NVDA Core issue 14587/PR 14588: announce tab switches in Notepad 11.2212 and later.
		# Element selected event fires multiple times due to state changes.
		# Resolved in NVDA 2023.2 (remove this method completely).
		if (
			obj.role == controlTypes.Role.TAB
			# this is done because 2 selection events are sent for the same object, so to prevent double speaking.
			and not eventHandler.isPendingEvents("UIA_elementSelected")
			and controlTypes.State.SELECTED in obj.states
		):
			speech.cancelSpeech()
			speech.speakObject(obj, reason=controlTypes.OutputReason.FOCUS)
			braille.handler.message(
				braille.getPropertiesBraille(
					name=obj.name,
					role=obj.role,
					states=obj.states,
					positionInfo=obj.positionInfo
				)
			)
		nextHandler()
