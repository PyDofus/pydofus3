from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class EmblemSymbolData(D2oData):
	bundle_name: ClassVar[str] = "emblemsymbolsdataroot"

	id: int
	skinId: int
	iconId: int
	order: int
	categoryId: int
	colorizable: bool

