from pydofus3.generated.pydantic.Core.DataCenter.Interfaces.IWorldEventData import IWorldEventData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar


class WorldEventMonstersHunterData(IWorldEventData, D2oData):
	bundle_name: ClassVar[str] = "worldeventsmonstershunterdataroot"

	monsterList: list[int]
	criterion: str
	mapList: list[int]
	subareaList: list[int]
	areaList: list[int]
	scoreGroupShared: bool
	scorePerDamage: bool
	scorePerMonster: int

