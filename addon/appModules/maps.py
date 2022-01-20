# WinTenApps/maps.py
# Part of Windows App Essentials collection
# Copyright 2016-2022 Joseph Lee, released under GPL.

# Numerous enhancements for Bing Maps app.

import appModuleHandler
import api
import controlTypes
import config
from NVDAObjects.UIA import UIA
import tones


# Map locations
# A static text denoting where one is located on the map.
class MapLocation(UIA):
	"""Plays a tone indicating the current map position."""

	def event_becomeNavigatorObject(self):
		l, t, w, h = self.location
		x = l + (w / 2)
		y = t + (h / 2)
		screenWidth, screenHeight = api.getDesktopObject().location[2:]
		if x <= screenWidth or y <= screenHeight:
			minPitch = config.conf['mouse']['audioCoordinates_minPitch']
			maxPitch = config.conf['mouse']['audioCoordinates_maxPitch']
			curPitch = minPitch + ((maxPitch - minPitch) * ((screenHeight - y) / float(screenHeight)))
			brightness = config.conf['mouse']['audioCoordinates_maxVolume']
			leftVolume = int((85 * ((screenWidth - float(x)) / screenWidth)) * brightness)
			rightVolume = int((85 * (float(x) / screenWidth)) * brightness)
			tones.beep(curPitch, 40, left=leftVolume, right=rightVolume)
		super().event_becomeNavigatorObject()


class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			try:
				if (
					obj.role in (controlTypes.Role.STATICTEXT, controlTypes.Role.BUTTON)
					and obj.parent.parent.UIAElement.cachedClassName == "Map"
				):
					clsList.insert(0, MapLocation)
			except AttributeError:
				pass
