from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class AchievementObjectiveData(D2oData):
	bundle_name: ClassVar[str] = "achievementobjectivesdataroot"

	id: int
	achievementId: int
	order: int
	nameId: i18n
	criterion: str

