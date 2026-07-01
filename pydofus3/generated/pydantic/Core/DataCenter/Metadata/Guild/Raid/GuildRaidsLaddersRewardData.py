from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Guild.Raid.GuildRaidsLaddersRewardItem import GuildRaidsLaddersRewardItem
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class GuildRaidsLaddersRewardData(D2oData):
	bundle_name: ClassVar[str] = "guildraidsladdersrewardsdataroot"

	id: int
	raidId: int
	position: list[int]
	percentage: int
	ornaments: list[int]
	titles: list[int]
	guildExperience: int
	items: list[GuildRaidsLaddersRewardItem]
	order: int

