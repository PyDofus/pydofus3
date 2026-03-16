from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class ModsterData(D2oData):
	bundle_name: ClassVar[str] = "modstersdataroot"

	id: int
	itemId: int
	modsterId: int
	order: int
	parentsModsterId: list[int]
	modsterActiveSpells: list[int]
	modsterPassiveSpells: list[int]
	modsterHiddenAchievements: list[int]
	modsterAchievements: list[int]

