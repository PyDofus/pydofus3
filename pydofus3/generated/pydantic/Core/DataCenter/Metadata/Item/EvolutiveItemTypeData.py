from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import float_nan
from typing import ClassVar

class EvolutiveItemTypeData(D2oData):
	bundle_name: ClassVar[str] = "evolutiveitemtypesdataroot"

	id: int
	maxLevel: int
	experienceBoost: float_nan
	experienceByLevel: list[int]

