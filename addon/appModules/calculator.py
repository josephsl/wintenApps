# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2020-2024 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Additional hacks on top of NVDA Core Calculator app module.

# Import the base app module as something else to avoid runtime issues.
from nvdaBuiltin.appModules.calculator import AppModule as CoreAppModule
import scriptHandler


class AppModule(CoreAppModule):

	@scriptHandler.script(gestures=CoreAppModule._calculatorResultGestures)
	def script_calculatorResult(self, gesture):
		# NVDA Core issue 15923/Microsoft Calcuilator issue 2097:
		# Force results announcement if results commands are performed.
		self._noCalculatorResultsGesturePressed = False
		super().script_calculatorResult(gesture)
