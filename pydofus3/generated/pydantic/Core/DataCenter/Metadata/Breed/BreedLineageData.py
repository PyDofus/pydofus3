from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Breed.LineageSpellData import LineageSpellData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class BreedLineageData(D2oData):
	bundle_name: ClassVar[str] = "breedlineagesdataroot"

	id: int
	nameId: int
	descriptionId: int
	breedId: int
	subEntityLook: str
	maxLevel: int
	xpFormulaId: int
	illustrationId: int
	gfxId: int
	indexedColors: str
	lineageSpells: list[LineageSpellData]

