from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import float_nan
from typing import ClassVar

class AchievementRewardData(D2oData):
	bundle_name: ClassVar[str] = "achievementrewardsdataroot"

	id: int
	achievementId: int
	criterions: str
	kamasRatio: float_nan
	experienceRatio: float_nan
	kamasScaleWithPlayerLevel: bool
	itemsReward: list[int]
	itemsQuantityReward: list[int]
	emotesReward: list[int]
	spellsReward: list[int]
	titlesReward: list[int]
	ornamentsReward: list[int]
	alterationsReward: list[int]
	guildPoints: int

