from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class GuildMissionMilestoneRewardData(D2oData):
	bundle_name: ClassVar[str] = "guildmissionmilestonerewardsdataroot"

	id: int
	milestoneId: int
	objectId: int
	quantity: int
	criterion: str

