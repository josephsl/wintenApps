#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2015-2019 NV Access Limited, Joseph Lee
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""App module for Shell Experience Host, part of Windows 10.
Shell Experience Host is home to a number of things, including Action Center and other shell features.
"""

from nvdaBuiltin.appModules.shellexperiencehost import *
from NVDAObjects.UIA import Toast_win10


class AppModule(AppModule):

	def event_NVDAObject_init(self, obj):
		# Temporary hack for 20H2 build 19042.421 (beta): toasts have no name.
		if isinstance(obj, Toast_win10) and obj.name == "":
			try:
				obj.name = f"New notification from {obj.children[1].name}, {obj.children[4].name}, {obj.children[5].name}. {obj.children[1].name}"
			except IndexError:
				pass
		super(AppModule, self).event_NVDAObject_init(obj)
