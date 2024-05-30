# Edge Web View 2
# Copyright 2024 Joseph Lee, released under GPL

"""Support for apps employing Edge Web View 2 runtime interface.
"""

import os
import shlex
import appModuleHandler
from appModuleHandler import AppModule


def getAppNameFromHost(processId):
	# Some apps have launcher executables which launch javaw.exe to run the app.
	# In this case, the parent process will usually be the launcher.
	proc = appModuleHandler.getWmiProcessInfo(processId)
	parent = proc.parentProcessId
	if parent:
		name = appModuleHandler.getAppNameFromProcessID(parent)
		if name and name not in ("explorer", "cmd"):
			# The parent isn't a shell, so it's probably a launcher.
			return name
