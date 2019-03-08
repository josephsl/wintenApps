#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2016 NV Access Limited
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
# Extended in 2017 by Joseph Lee

"""An appModule for the Windows 10 Mail app"""

from nvdaBuiltin.appModules.hxoutlook import *
from comtypes import COMError
import api
from NVDAObjects.UIA import UIA
from NVDAObjects.behaviors import RowWithFakeNavigation
import ui

class MailItemRow(RowWithFakeNavigation, UIA):

	def script_moveToPreviousColumn(self, gesture):
		cur = api.getNavigatorObject()
		if cur == self:
			new = None
		elif cur.parent != self:
			new = self
		else:
			new = cur.previous
		self._moveToColumn(new)
	script_moveToPreviousColumn.canPropagate = True
	script_moveToPreviousColumn.__doc__ = RowWithFakeNavigation.script_moveToPreviousColumn.__doc__

	def _moveToRow(self, row):
		# Customized because there is no easy way to obtain column position info for this object yet.
		# Therefore report that this is not supported yet.
		ui.message(_("Cannot move between rows"))

# NVDA Core issue 9341: temporary workaround for COM error exception found in NVDA.
class MailWordDocument(WordDocument):

	treeInterceptorClass=MailWordDocumentTreeInterceptor
	def _get_shouldCreateTreeInterceptor(self):
		# Locate the Reading pane in the ancestors
		condition=UIAHandler.handler.clientObject.createPropertyCondition(UIAHandler.UIA_ClassNamePropertyId,"ReadingPaneModern")
		walker=UIAHandler.handler.clientObject.createTreeWalker(condition)
		try:
			parent=walker.NormalizeElement(self.UIAElement)
		except COMError:
			parent=None
		if not parent:
			return False
		# If we can find the message headers, then it is read-only and therefore needs browseMode
		# An editable document contains draft headers instead
		condition=UIAHandler.handler.clientObject.createPropertyCondition(UIAHandler.UIA_AutomationIdPropertyId,"MessageHeader")
		header=parent.findFirst(UIAHandler.TreeScope_Descendants,condition)
		return bool(header)


class AppModule(AppModule):

	def chooseNVDAObjectOverlayClasses(self,obj,clsList):
		if WordDocument in clsList:
			clsList.insert(0,MailWordDocument)
		elif isinstance(obj, UIA) and obj.UIAElement.cachedAutomationID == "MailItem":
			clsList.insert(0, MailItemRow)
