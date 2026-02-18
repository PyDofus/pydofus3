from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class SpellVariantData(D2oData):
	bundle_name: ClassVar[str] = "spellvariantsdataroot"

	id: int
	breedId: int
	spellIds: list[int]

