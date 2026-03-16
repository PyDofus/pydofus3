from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class WorldMapData(D2oData):
	bundle_name: ClassVar[str] = "worldmapsdataroot"

	id: int
	nameId: i18n
	origineX: int
	origineY: int
	mapWidth: float_nan
	mapHeight: float_nan
	minScale: float_nan
	maxScale: float_nan
	startScale: float_nan
	totalWidth: int
	totalHeight: int
	zoom: list[float_nan]
	visibleOnMap: bool

