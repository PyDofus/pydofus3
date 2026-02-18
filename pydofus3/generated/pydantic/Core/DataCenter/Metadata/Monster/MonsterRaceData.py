from pydofus3.generated.pydantic.Core.DataCenter.Interfaces.IAdminSelectionEntryType import IAdminSelectionEntryType
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.i18n import i18n

class MonsterRaceData(IAdminSelectionEntryType, D2oData):
	bundle_name: ClassVar[str] = "monsterracesdataroot"

	id: int
	superRaceId: int
	nameId: i18n
	aggressiveZoneSize: int
	aggressiveLevelDiff: int
	aggressiveImmunityCriterion: str
	aggressiveAttackDelay: int
	monsters: list[int]

