from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class CompanionData(D2oData):
	bundle_name: ClassVar[str] = "companionsdataroot"

	id: int
	nameId: i18n
	look: str
	webDisplay: bool
	descriptionId: i18n
	startingSpellLevelId: int
	assetId: int
	characteristics: list[int]
	spells: list[int]
	creatureBoneId: int
	visibility: str

