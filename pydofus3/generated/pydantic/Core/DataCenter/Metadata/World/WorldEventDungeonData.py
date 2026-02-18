from pydofus3.generated.pydantic.Core.DataCenter.Interfaces.IWorldEventData import IWorldEventData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar


class WorldEventDungeonData(IWorldEventData, D2oData):
	bundle_name: ClassVar[str] = "worldeventsdungeonsdataroot"

	dungeonId: int
	dungeonMapIdTeleport: int
	scoreGroupShared: bool
	scorePerDamage: bool
	scorePerDungeon: int

