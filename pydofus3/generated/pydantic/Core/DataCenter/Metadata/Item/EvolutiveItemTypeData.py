from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import float_nan

class EvolutiveItemTypeData(D2oData):
	bundle_name: ClassVar[str] = "evolutiveitemtypesdataroot"

	id: int
	maxLevel: int
	experienceBoost: float_nan
	experienceByLevel: list[int]

