from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class SpellHaloData(D2oData):
	bundle_name: ClassVar[str] = "spellhalodataroot"

	id: int
	spellGradeByPlayerLevel: bool
	shapesIds: list[int]
	entrySpellId: int
	entrySpellDefaultGrade: int
	exitSpellId: int
	exitSpellDefaultGrade: int

