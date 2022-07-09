# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2016-2022 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Extended in 2017 and 2019 by Joseph Lee

# Borrows heavily from built-in Mail and Calendar app module.
# #70: NVDA Core pull requests are made using the core app module, not alias modules.
from nvdaBuiltin.appModules.hxmail import AppModule


# The below app module class inherits from built-in Mail and Calendar app module class, so inform Mypy.
class AppModule(AppModule):  # type: ignore[no-redef]

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# NVDA Core takes care of the rest.
		super().chooseNVDAObjectOverlayClasses(obj, clsList)
