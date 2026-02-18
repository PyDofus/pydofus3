from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class ProgressingAchievementStepData(D2oData):
	bundle_name: ClassVar[str] = "progressingachievementstepsdataroot"

	id: int
	progressId: int
	score: int
	isCosmetic: bool
	achievementId: int
	isBuyable: bool

