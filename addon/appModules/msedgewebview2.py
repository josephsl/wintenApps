# Edge WebView2
# Copyright 2024 Joseph Lee, released under GPL

"""Support for apps employing Edge WebView2 runtime interface.
"""

import appModuleHandler


def getAppNameFromHost(processId):
	# Some apps have launcher executables which launch msedgewebview2.exe to display the interface.
	# In this case, the parent process will usually be the launcher.
	proc = appModuleHandler.getWmiProcessInfo(processId)
	# Unlikely but react to undefined parent process ID.
	if not (parent := proc.parentProcessId):
		raise LookupError
	return appModuleHandler.getAppNameFromProcessID(parent)
