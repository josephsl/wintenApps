# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2020-2023 NV Access Limited, Joseph Lee
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""App module for Windows 10 Calculator.
This is also the base app module for Windows 11 Calculator."""

from nvdaBuiltin.appModules.calculator import AppModule as CoreAppModule
import scriptHandler


class AppModule(CoreAppModule):  # type: ignore[no-redef]

	@scriptHandler.script(gestures=CoreAppModule._calculatorResultGestures)
	def script_calculatorResult(self, gesture):
		# NVDA Core issue 15923/Microsoft Calcuilator issue 2097:
		# Force results announcement if results comamnds are performed.
		self._noCalculatorResultsGesturePressed = False
		super().script_calculatorResult(gesture)
