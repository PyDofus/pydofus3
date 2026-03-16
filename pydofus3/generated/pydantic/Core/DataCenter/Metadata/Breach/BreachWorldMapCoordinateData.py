from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class BreachWorldMapCoordinateData(D2oData):
	bundle_name: ClassVar[str] = "breachworldmapcoordinatesdataroot"

	mapStage: int
	mapCoordinateX: int
	mapCoordinateY: int
	unexploredMapIcon: int
	exploredMapIcon: int

