from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.i18n import i18n

class LegendaryTreasureHuntData(D2oData):
	bundle_name: ClassVar[str] = "legendarytreasurehuntsdataroot"

	id: int
	nameId: i18n
	level: int
	chestId: int
	monsterId: int
	mapItemId: int
	xpRatio: float_nan

