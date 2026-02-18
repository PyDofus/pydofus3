from pydofus3.generated.pydantic.Core.DataCenter.Interfaces.IWorldEventData import IWorldEventData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar


class WorldEventWorldBossesData(IWorldEventData, D2oData):
	bundle_name: ClassVar[str] = "worldeventsworldbossesdataroot"

	monsterList: list[int]
	criterion: str
	mapList: list[int]
	subareaList: list[int]
	areaList: list[int]
	scoreGroupShared: bool
	scorePerDamage: bool
	scoreTotal: int
	scoreRatio: int
	scoreDayCount: int

