from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class GuildRaidsGroupData(D2oData):
	bundle_name: ClassVar[str] = "guildraidsgroupsdataroot"

	id: int
	raidId: int
	nameId: int
	descriptionId: int
	minPlayers: int
	maxPlayers: int

