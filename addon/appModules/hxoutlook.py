# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2016-2021 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Extended in 2017 and 2019 by Joseph Lee

"""An appModule for the Mail app on Windows 10 and later"""

# Borrows heavily from built-in Mail and Calendar app module.
from nvdaBuiltin.appModules.hxoutlook import *  # NOQA: F403
import api
from NVDAObjects.UIA import UIA
from NVDAObjects.behaviors import RowWithFakeNavigation
import ui
import config
import nvwave


class MailItemRow(RowWithFakeNavigation, UIA):

	# Since 2019, columns are exposed as regular children, not simple children, breaking the below two scripts.
	def script_moveToNextColumn(self, gesture):
		cur = api.getNavigatorObject()
		if cur == self:
			new = self.firstChild
		elif cur.parent != self:
			new = self
		else:
			new = cur.next
		self._moveToColumn(new)

	def script_moveToPreviousColumn(self, gesture):
		cur = api.getNavigatorObject()
		if cur == self:
			new = None
		elif cur.parent != self or not cur.previous:
			new = self
		else:
			new = cur.previous
		self._moveToColumn(new)

	def _moveToRow(self, row):
		# Customized because there is no easy way to obtain column position info for this object yet.
		# Therefore report that this is not supported yet.
		ui.message(_("Cannot move between rows"))


# The below app module class inherits from built-in Mail and Calendar app module class, so inform Mypy.
# Also Flake8 and other linters should ignore this.
class AppModule(AppModule):  # type: ignore[misc]  # NOQA: F405

	def event_UIA_controllerFor(self, obj, nextHandler):
		if config.conf["presentation"]["reportAutoSuggestionsWithSound"]:
			# Obtain controller for property directly instead of relying on focused control.
			if len(obj.controllerFor) > 0:
				nvwave.playWaveFile(r"waves\suggestionsOpened.wav")
			else:
				nvwave.playWaveFile(r"waves\suggestionsClosed.wav")
		nextHandler()

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA) and obj.UIAAutomationId == "MailItem":
			clsList.insert(0, MailItemRow)
		# NVDA Core takes care of the rest.
		super(AppModule, self).chooseNVDAObjectOverlayClasses(obj, clsList)
