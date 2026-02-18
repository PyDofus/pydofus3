from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class MonsterMiniBossData(D2oData):
	bundle_name: ClassVar[str] = "monsterminibossesdataroot"

	id: int
	monsterReplacingId: int

