from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class GuildMissionMilestoneData(D2oData):
	bundle_name: ClassVar[str] = "guildmissionmilestonesdataroot"

	id: int
	activityId: int
	nameId: i18n
	milestoneLevel: int
	activityPoint: int
	xp: int
	acknowledgmentPoint: int

