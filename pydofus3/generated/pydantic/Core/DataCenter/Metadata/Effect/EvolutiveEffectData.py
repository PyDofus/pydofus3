from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import WrappedList
from pydofus3.not_generated.base import float_nan

class EvolutiveEffectData(D2oData):
	bundle_name: ClassVar[str] = "evolutiveeffectsdataroot"

	id: int
	actionId: int
	targetId: int
	progressionPerLevelRange: list[WrappedList[float_nan]]

