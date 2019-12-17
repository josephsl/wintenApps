# A part of NonVisual Desktop Access (NVDA)
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Copyright (C) 2012 NV Access Limited

"""App module host for Windows 8.x WinRT apps hosted by wwahost.exe.
"""

# Extended in 2019 to add additoinal properties and fixes.

from nvdaBuiltin.appModules.wwahost import *
import ctypes
import winKernel

def getAppNameFromHost(processId):
	# Some apps that come with Windows 8 and 8.1 are hosted by wwahost.exe.
	# App modules for these are named after the hosted app name.
	processHandle = winKernel.openProcess(winKernel.SYNCHRONIZE|winKernel.PROCESS_QUERY_INFORMATION,False,processId)
	length = ctypes.c_uint()
	buf = winKernel.kernel32.GetApplicationUserModelId(processHandle, ctypes.byref(length), None)
	appModel = ctypes.create_unicode_buffer(buf)
	winKernel.kernel32.GetApplicationUserModelId(processHandle, ctypes.byref(length), appModel)
	winKernel.closeHandle(processHandle)
	# Sometimes app model might be empty, so raise errors and fall back to wwahost.
	if not appModel.value:
		raise LookupError
	# Convert this into lowercase to make the file name consistent with other NVDA app modules.
	return appModel.value.split("!")[-1].lower()
