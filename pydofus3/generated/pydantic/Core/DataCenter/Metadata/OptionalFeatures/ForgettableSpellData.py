from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class ForgettableSpellData(D2oData):
	bundle_name: ClassVar[str] = "forgettablespellsdataroot"

	id: int
	pairId: int
	itemId: int

