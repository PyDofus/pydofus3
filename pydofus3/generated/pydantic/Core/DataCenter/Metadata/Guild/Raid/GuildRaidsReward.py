from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Guild.Raid.GuildRaidsRewardsItemData import GuildRaidsRewardsItemData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class GuildRaidsReward(D2oData):
	bundle_name: ClassVar[str] = "guildraidsrewardsdataroot"

	id: int
	raidId: int
	descriptionId: int
	kamas: int
	experience: int
	score: int
	order: int
	rewards: list[GuildRaidsRewardsItemData]

