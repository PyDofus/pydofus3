from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class GuildMissionGradeData(D2oData):
	bundle_name: ClassVar[str] = "guildmissiongradesdataroot"

	id: int
	name: str
	rankId: int
	activityPoint: int
	token: int

