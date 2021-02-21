# WinTenApps/commsapps.py
# Part of Windows 10 App Essentials collection
# Copyright 2020-2021 Joseph Lee, released under GPL.

# In 2020, Mail and Calendar became one app, sharing an executable named commsapps.exe.
# This app module is based mostly on old Calendar app with workarounds from Mail included.

from .hxoutlook import *


# Bulk of the below class is defined in Mail and Calendar (hxoutlook) app module but Mypy doesn't know that.
class AppModule(AppModule):  # type: ignore[no-redef]

	def event_NVDAObject_init(self, obj):
		# It is quite anoying to hear the same text for name and description, so forget the description.
		if obj.name != "" and obj.description == obj.name:
			obj.description = None
