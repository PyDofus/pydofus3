from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class MonsterRaceData(D2oData):
	bundle_name: ClassVar[str] = "monsterracesdataroot"

	id: int
	superRaceId: int
	nameId: i18n
	aggressiveZoneSize: int
	aggressiveLevelDiff: int
	aggressiveImmunityCriterion: str
	aggressiveAttackDelay: int
	monsters: list[int]

