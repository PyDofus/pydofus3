from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class ItemSuperTypeData(D2oData):
	bundle_name: ClassVar[str] = "itemsupertypesdataroot"

	id: int
	possiblePositions: list[int]

