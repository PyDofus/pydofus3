from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class BreachBossData(D2oData):
	bundle_name: ClassVar[str] = "breachbossesdataroot"

	id: int
	monsterId: int
	category: int
	apparitionCriterion: str
	accessCriterion: str
	incompatibleBosses: list[int]
	rewardId: int

