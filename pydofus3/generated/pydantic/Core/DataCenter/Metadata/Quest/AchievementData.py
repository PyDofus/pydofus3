from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class AchievementData(D2oData):
	bundle_name: ClassVar[str] = "achievementsdataroot"

	id: int
	nameId: i18n
	categoryId: int
	descriptionId: i18n
	iconId: int
	points: int
	level: int
	order: int
	accountLinked: bool
	objectiveIds: list[int]
	rewardIds: list[int]

