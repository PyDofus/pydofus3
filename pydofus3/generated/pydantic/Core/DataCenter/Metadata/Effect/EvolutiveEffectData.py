from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import WrappedList
from typing import ClassVar

class EvolutiveEffectData(D2oData):
	bundle_name: ClassVar[str] = "evolutiveeffectsdataroot"

	id: int
	actionId: int
	targetId: int
	progressionPerLevelRange: list[WrappedList[float_nan]]

