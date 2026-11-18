from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Breed.LineageSpellData import LineageSpellData
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class BreedLineageData(D2oData):
	bundle_name: ClassVar[str] = "breedlineagesdataroot"

	id: int
	nameId: i18n
	descriptionId: i18n
	breedId: int
	subEntityLook: str
	maxLevel: int
	xpFormulaId: int
	illustrationId: int
	gfxId: int
	indexedColors: str
	lineageSpells: list[LineageSpellData]

