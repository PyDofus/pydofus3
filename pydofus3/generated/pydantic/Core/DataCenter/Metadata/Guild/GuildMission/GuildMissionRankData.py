from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class GuildMissionRankData(D2oData):
	bundle_name: ClassVar[str] = "guildmissionranksdataroot"

	id: int
	nameId: i18n
	grades: list[int]

