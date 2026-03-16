from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class WaypointData(D2oData):
	bundle_name: ClassVar[str] = "waypointsdataroot"

	id: int
	mapId: int
	subAreaId: int
	activated: bool

