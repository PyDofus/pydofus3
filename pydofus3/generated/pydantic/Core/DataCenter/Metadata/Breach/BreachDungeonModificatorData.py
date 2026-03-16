from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import float_nan
from typing import ClassVar

class BreachDungeonModificatorData(D2oData):
	bundle_name: ClassVar[str] = "breachdungeonmodificatorsdataroot"

	id: int
	modificatorId: int
	criterion: str
	additionalRewardPercent: float_nan
	score: float_nan
	isPositiveForPlayers: bool
	tooltipBaseline: str

