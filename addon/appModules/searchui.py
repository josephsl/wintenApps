# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015-2025 NV Access Limited, Joseph Lee, James Teh
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Reintroduced in 2025, extends SearchUI ap module from NVDA Core

from nvdaBuiltin.appModules.searchui import AppModule
import controlTypes
from NVDAObjects.UIA import UIA
from NVDAObjects.IAccessible import IAccessible, ContentGenericClient
from NVDAObjects import NVDAObject
import winUser
from logHandler import log


# Code credit: Jamie Teh (Mozilla)
# Resolved in NVDA 2025.2.
class StartChromiumObj(IAccessible):
	def _get_shouldAllowIAccessibleFocusEvent(self) -> bool:
		if self.role == controlTypes.Role.DOCUMENT:
			# #17951: Sometimes, the results Chromium document fires a focus event and
			# reports as focused, even though the search box still has focus. We can
			# tell whether it is *really* focused by checking whether its
			# Windows.UI.Core.CoreComponentInputSource ancestor has focus.
			try:
				return self.parent.parent.parent.hasFocus
			except AttributeError:
				log.debugWarning("Couldn't find CoreInput ancestor of Chromium doc")
		return super().shouldAllowIAccessibleFocusEvent

	def isDescendantOf(self, obj: NVDAObject) -> bool:
		# #17951: We use IA2 for the Chromium document. However, this method will be
		# called with the UIA object being controlled by the search box to check
		# whether it is a suggestion.
		return (
			isinstance(obj, UIA) and obj.UIAElement.CurrentClassName == "WebView2Standalone.Controls.WebView2"
		)


# Mypy should be reminded that this app module is powered by built-in SearchUI app module.
class AppModule(AppModule):  # type: ignore[no-redef]
	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[NVDAObject]) -> None:
		if isinstance(obj, IAccessible):
			try:
				# #5288: Never use ContentGenericClient, as this uses displayModel
				# which will freeze if the process is suspended.
				clsList.remove(ContentGenericClient)
			except ValueError:
				pass
			if obj.windowClassName.startswith("Chrome_"):
				clsList.insert(0, StartChromiumObj)
				return
		super().chooseNVDAObjectOverlayClasses(obj, clsList)

	def isBadUIAWindow(self, hwnd: int) -> bool:
		# #17951: Never use UIA for the Chromium document in the Start menu because
		# SetFocus freezes. Without this explicit code, NVDA would try to use UIA:
		# 1. If we haven't injected yet. This can happen before focus is fired
		# within the Chromium document. Since it is in a different process, it
		# doesn't fire foreground and focus events as soon as the Start Menu opens.
		# 2. If we can't inject at all, which happens if we don't have the uiAccess
		# privilege.
		return winUser.getClassName(hwnd) == "Chrome_RenderWidgetHostHWND"
