from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class GuildRaidsGoalData(D2oData):
	bundle_name: ClassVar[str] = "guildraidsgoalsdataroot"

	id: int
	raidId: int
	nameId: i18n
	value: int
	requisiteForDisplay: list[int]
	impactProgress: bool
	score: int

