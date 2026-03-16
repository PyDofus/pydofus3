from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class LegendaryPowerCategoryData(D2oData):
	bundle_name: ClassVar[str] = "legendarypowerscategoriesdataroot"

	id: int
	categoryName: str
	categoryOverridable: bool
	categorySpells: list[int]

