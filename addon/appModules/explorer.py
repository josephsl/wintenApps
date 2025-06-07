# -*- coding: UTF-8 -*-
# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2025 NV Access Limited, Joseph Lee, Łukasz Golonka, Julien Cochuyt
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Provides additional routines on top of the built-in File Explorer app module.

from typing import Callable
# Flake8 F403: detect other add-ons that overrode File Explorer app module.
from nvdaBuiltin.appModules.explorer import *  # NOQA: F403
import controlTypes
from NVDAObjects import NVDAObject


# App module class comes from built-in File Explorer app module but Mypy doesn't know that.
# Also tell Flake8 that the base AppModule class comes from NVDA Core.
class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405
	def event_UIA_elementSelected(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# NVDA Core issue 14388: announce File Explorer tab switches (Windows 11 22H2 and later).
		# Resolved in NVDA 2023.2 (remove this method completely).
		import speech
		import braille
		import eventHandler
		# Element selected event fires multiple times due to state changes.
		if (
			obj.role == controlTypes.Role.TAB
			and controlTypes.State.SELECTED in obj.states
			and obj.parent.UIAAutomationId == "TabListView"
			# this is done because 2 selection events are sent for the same object, so to prevent double speaking.
			and not eventHandler.isPendingEvents(eventName="UIA_elementSelected")
		):
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
