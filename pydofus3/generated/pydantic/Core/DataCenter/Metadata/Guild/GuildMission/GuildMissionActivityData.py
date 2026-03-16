from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class GuildMissionActivityData(D2oData):
	bundle_name: ClassVar[str] = "guildmissionactivitiesdataroot"

	id: int
	nameId: i18n
	level: int
	recommendedPlayers: int
	rerollCost: int
	milestonesIds: list[int]

