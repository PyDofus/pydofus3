from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class WorldEventData(D2oData):
	bundle_name: ClassVar[str] = "worldeventsdataroot"

	id: int
	nameId: i18n
	descriptionId: i18n
	categoryId: int
	level: int
	areas: list[int]
	subareas: list[int]
	globalDrops: list[int]
	fightScenarios: list[int]
	deletedObjects: list[int]
	monsterHunterGroupsPerMap: int
	dungeonHunterGroupsPerMap: int
	preMsgId: int
	startMsgId: int
	endMsgId: int
	preMsgDelay: int
	worldEventRewardId: int
	duration: int
	worldEventDataType: int
	worldEventEventId: int

