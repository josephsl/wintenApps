# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2015-2023 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for Shell Experience Host, part of Windows 10 and later.
Shell Experience Host is home to a number of things, including Action Center and other shell features.
"""

# Extends NVDA Core's Shell Experience Host app module.
from nvdaBuiltin.appModules.shellexperiencehost import AppModule
from NVDAObjects.UIA import UIA
import controlTypes


class AppModule(AppModule):

	def event_NVDAObject_init(self, obj):
		if isinstance(obj, UIA):
			# #8845: Brightness button in Action Center is a button, not a toggle button.
			# Brightness control is now a slider in build 18277.
			if obj.UIAAutomationId == "Microsoft.QuickAction.Brightness":
				obj.role = controlTypes.Role.BUTTON
				obj.states.discard(controlTypes.State.CHECKABLE)
			# Volume mixer list items in canary build 25300 series have no label.
			# There is no Automation Id but a generic class name is used, so locate items via its children.
			# Interestingly, item label is the description text for volume slider control.
			if (
				obj.role == controlTypes.Role.LISTITEM
				and not obj.name
				and obj.lastChild.UIAAutomationId == "AppVolumeLevel"
			):
				obj.name = obj.lastChild.description
