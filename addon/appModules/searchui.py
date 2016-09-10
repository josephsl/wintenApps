#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2015 NV Access Limited
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
# Extended by Joseph Lee (released under GPL)

import sys
import ui
from nvdaBuiltin.appModules.searchui import *

class AppModule(AppModule):

	# Past responses from Cortana (cached to prevent repetition, initially an empty string).
	CortanaResponseCache = ""
	# NVDA should not speak while Cortana is speaking.
	CortanaIsListening = False 
	# Change Cortana's greeing line based on build.
	greetingLine = "GreetingLine1" if sys.getwindowsversion().build > 10586 else "GreetingLine2"

	def event_nameChange(self, obj, nextHandler):
		# NVDA, can you act as a mouthpiece for Cortana?
		if isinstance(obj, UIA) and obj.next is not None and obj.next.role == controlTypes.ROLE_EDITABLETEXT and obj.name != self.CortanaResponseCache:
			element = obj.UIAElement
			# There are two Cortana response lines. Usually line 2 is more reliable.
			# However, Redstone seems to favor line 1 better.
			if element.cachedAutomationID in ("SpeechContentLabel", self.greetingLine):
				ui.message(obj.name)
				self.CortanaResponseCache = obj.name
		nextHandler()

	"""def event_appModule_gainFocus(self):
		import globalPlugins
		if globalPlugins.wintenObjs.letCortanaListen:
			self.CortanaIsListening = True

	def event_appModule_loseFocus(self):
		if self.CortanaIsListening:
			self.CortanaIsListening = False
			import globalPlugins
			globalPlugins.wintenObjs.letCortanaListen = False"""
