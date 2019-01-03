#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2012 NV Access Limited

"""App module host for Windows 8.x WinRT apps hosted by wwahost.exe.
"""

# Extended in 2019 to add additoinal properties and fixes.

from nvdaBuiltin.appModules.wwahost import *
import ctypes
import winKernel

class AppModule(AppModule):

	def _setProductInfo(self):
		# Default implementation is too generic - returns Windows version information.
		# Therefore, probe package full name and parse the serialized representation of package info structure.
		if not self.processHandle:
			raise RuntimeError("processHandle is 0")
		length = ctypes.c_uint()
		buf = winKernel.kernel32.GetPackageFullName(self.processHandle, ctypes.byref(length), None)
		packageFullName = ctypes.create_unicode_buffer(buf)
		winKernel.kernel32.GetPackageFullName(self.processHandle, ctypes.byref(length), packageFullName)
		packageInfo = packageFullName.value.split("_")
		# Product name is of the form publisher.name.
		self.productName = packageInfo[0]
		self.productVersion = packageInfo[1]
