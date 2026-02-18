from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.i18n import i18n

class InfiniteDreamIntensityData(D2oData):
	bundle_name: ClassVar[str] = "infinitedreamintensitiesdataroot"

	id: int
	intensity: int
	droplegend: bool
	dropBonus: float_nan
	xpBonus: float_nan
	money: int
	additionalLife: int
	nameId: i18n
	dreamFragments: int

