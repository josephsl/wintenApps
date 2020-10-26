# WinTenApps/commsapps.py
# Part of Windows 10 App Essentials collection
# Copyright 2020 Joseph Lee, released under GPL.

# In 2020, Mail and Calendar became one app, sharing an executable named commsapps.exe.
# This app module is based mostly on old Calendar app with workarounds from Mail included.

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

	def event_NVDAObject_init(self, obj):
		# It is quite anoying to hear the same text for name and description, so forget the description.
		if obj.name != "" and obj.description == obj.name:
			obj.description = None

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if WordDocument in clsList:
			clsList.insert(0, MailWordDocument)
		elif isinstance(obj, UIA) and obj.UIAAutomationId == "MailItem":
			clsList.insert(0, MailItemRow)
