# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2016-2022 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Extended in 2017 and 2019 by Joseph Lee

# Borrows heavily from built-in Mail and Calendar app module.
# #70: NVDA Core pull requests are made using the core app module, not alias modules.
from nvdaBuiltin.appModules.hxmail import AppModule
from NVDAObjects.UIA import UIA
from NVDAObjects.behaviors import RowWithFakeNavigation
import ui


# Deprecated: for consistency with other lists and Narrator, table navigation commands are deprecated.
class MailItemRow(RowWithFakeNavigation, UIA):

	def _moveToRow(self, row):
		# Customized because there is no easy way to obtain column position info for this object yet.
		# Therefore report that this is not supported yet.
		ui.message(_("Cannot move between rows"))


# The below app module class inherits from built-in Mail and Calendar app module class, so inform Mypy.
class AppModule(AppModule):  # type: ignore[no-redef]

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# NVDA Core takes care of the rest.
		super().chooseNVDAObjectOverlayClasses(obj, clsList)
