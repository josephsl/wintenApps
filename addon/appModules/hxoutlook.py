#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2016-2019 NV Access Limited, Joseph Lee
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
# Extended in 2017 and 2019 by Joseph Lee

"""An appModule for the Windows 10 Mail app"""

from nvdaBuiltin.appModules.hxoutlook import *
import api
from NVDAObjects.UIA import UIA
from NVDAObjects.behaviors import RowWithFakeNavigation
import ui

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


class AppModule(AppModule):

	def chooseNVDAObjectOverlayClasses(self,obj,clsList):
		if WordDocument in clsList:
			clsList.insert(0,MailWordDocument)
		elif isinstance(obj, UIA) and obj.UIAElement.cachedAutomationID == "MailItem":
			clsList.insert(0, MailItemRow)
