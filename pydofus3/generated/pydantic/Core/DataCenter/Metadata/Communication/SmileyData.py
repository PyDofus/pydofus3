from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class SmileyData(D2oData):
	bundle_name: ClassVar[str] = "smileysdataroot"

	id: int
	order: int
	gfxId: str
	forPlayers: bool
	referenceId: int
	categoryId: int

