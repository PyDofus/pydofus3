from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class MapsCoordinateData(D2oData):
	bundle_name: ClassVar[str] = "mapscoordinatesdataroot"

	compressedCoords: int
	mapIds: list[int]

