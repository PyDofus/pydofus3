from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class CompanionSpellData(D2oData):
	bundle_name: ClassVar[str] = "companionspellsdataroot"

	id: int
	spellId: int
	companionId: int
	gradeByLevel: str

