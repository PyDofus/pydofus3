from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.i18n import i18n

class AchievementCategoryData(D2oData):
	bundle_name: ClassVar[str] = "achievementcategoriesdataroot"

	id: int
	nameId: i18n
	parentId: int
	icon: str
	order: int
	color: str
	achievementIds: list[int]
	visibilityCriterion: str

