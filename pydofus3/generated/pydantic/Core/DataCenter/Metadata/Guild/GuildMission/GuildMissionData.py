from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class GuildMissionData(D2oData):
	bundle_name: ClassVar[str] = "guildmissionsdataroot"

	id: int
	categoryId: int
	superCategoryId: int
	nameId: i18n
	recommendedLevel: int
	gradeId: int
	activityPoint: int
	token: int
	objectives: list[int]
	rankId: int

