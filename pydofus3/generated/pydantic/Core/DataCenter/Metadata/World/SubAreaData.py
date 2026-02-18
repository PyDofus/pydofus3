from pydofus3.generated.pydantic.Core.DataCenter.Types.Rectangle import Rectangle
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class SubAreaData(D2oData):
	bundle_name: ClassVar[str] = "subareasdataroot"

	id: int
	nameId: i18n
	areaId: int
	mapIds: list[int]
	bounds: Rectangle
	shape: list[int]
	customWorldMapId: int
	packId: int
	level: int
	isConquestVillage: bool
	basicAccountAllowed: bool
	displayOnWorldMap: bool
	mountAutoTripAllowed: bool
	psiAllowed: bool
	monsters: list[int]
	entranceMapIds: list[int]
	exitMapIds: list[int]
	capturable: bool
	achievements: list[int]
	exploreAchievementId: int
	harvestables: list[int]
	associatedZaapMapId: int
	neighbors: list[int]
	dungeonId: int

