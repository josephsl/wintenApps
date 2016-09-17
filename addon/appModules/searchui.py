#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2015 NV Access Limited
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
# Extended by Joseph Lee (copyright 2016, released under GPL)

# Extended to let NVDA cooperate with Cortana.

import sys
import ui
from nvdaBuiltin.appModules.searchui import *

class AppModule(AppModule):

	# Past responses from Cortana (cached to prevent repetition, initially an empty string).
	CortanaResponseCache = ""
	# Change Cortana's greeting line based on build.
	greetingLine = "GreetingLine1" if sys.getwindowsversion().build > 10586 else "GreetingLine2"

	def event_nameChange(self, obj, nextHandler):
		# NVDA, can you act as a mouthpiece for Cortana?
		if isinstance(obj, UIA) and isinstance(obj.next, UIA) and obj.next.UIAElement.cachedAutomationID != "SpeechButton" and obj.name != self.CortanaResponseCache:
			element = obj.UIAElement
			# There are two Cortana response lines. Usually line 2 is more reliable.
			# However, Redstone seems to favor line 1 better.
			# A specific automation ID is seen for reminders and others.
			if element.cachedAutomationID in ("SpeechContentLabel", "WeSaidTextBlock", self.greetingLine):
				ui.message(obj.name)
				self.CortanaResponseCache = obj.name
		nextHandler()
