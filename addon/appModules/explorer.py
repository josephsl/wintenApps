# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2026 NV Access Limited, Joseph Lee, Łukasz Golonka, Julien Cochuyt
# This file may be used under the terms of the GNU General Public License, version 2 or later, as modified by the NVDA license.
# For full terms and any additional permissions, see the NVDA license file: https://github.com/nvaccess/nvda/blob/master/copying.txt

# Provides additional routines on top of the built-in File Explorer app module.

# Flake8 F403: detect other add-ons that overrode File Explorer app module.
from nvdaBuiltin.appModules.explorer import *  # NOQA: F403
from nvdaBuiltin.appModules.explorer import AppModule as CoreAppModule
import versionInfo
import winVersion


# Let NVDA work with its own File Explorer app module in 2025.2.
# Don't worry about "cls" type.
def nvda251applicable(cls):  # type: ignore
	return CoreAppModule if (versionInfo.version_year, versionInfo.version_major) >= (2025, 2) else cls


@nvda251applicable
class AppModule(CoreAppModule):
	def _setProductInfo(self) -> None:
		# NVDA Core issue 19802: customized for File Explorer as product version is wrong
		# (looks at explorer.exe.mui).
		# Resolved in NVDA 2026.2.
		if not self.processHandle:
			raise RuntimeError("processHandle is 0")
		# Even though product version is wrong, use product name supplied by File Explorer.
		productInfo = self._getExecutableFileInfo()
		self.productName = productInfo[0]
		# NVDA claims executable name is "explorer.exe" when in fact it is "explorer.exe.mui".
		# This means file information would not be accurate, returning the base Windows build.revision.
		# Therefore, set product version to Windows major.minor.build.revision.
		winVer = winVersion.getWinVer()
		self.productVersion = f"{winVer.major}.{winVer.minor}.{winVer.build}.{winVer.revision}"
