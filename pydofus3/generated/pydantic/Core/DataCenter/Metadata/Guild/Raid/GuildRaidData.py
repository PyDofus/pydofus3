from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Guild.Raid.GuildRaidsVariablesData import GuildRaidsVariablesData
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import ClassVar

class GuildRaidData(D2oData):
	bundle_name: ClassVar[str] = "guildraidsdataroot"

	id: int
	nameId: int
	descriptionId: int
	duration: int
	playerHealth: int
	minPlayers: int
	maxPlayers: int
	groups: list[int]
	goals: list[int]
	variables: list[GuildRaidsVariablesData]
	maxScore: int
	price: int
	canFinish: bool
	canRestart: bool
	type: int

	class GoalType(OpenAPIIntEnum):
		Validation = 0
		CounterUp = 1
		CounterDown = 2

