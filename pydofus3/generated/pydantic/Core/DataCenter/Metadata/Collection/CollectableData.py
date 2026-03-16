from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class CollectableData(D2oData):
	bundle_name: ClassVar[str] = "collectablesdataroot"

	entityId: int
	name: str
	typeId: int
	gfxId: int
	order: int
	rarity: int

