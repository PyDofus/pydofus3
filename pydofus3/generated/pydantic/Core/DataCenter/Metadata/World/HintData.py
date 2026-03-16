from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class HintData(D2oData):
	bundle_name: ClassVar[str] = "hintsdataroot"

	id: int
	categoryId: int
	gfx: int
	nameId: i18n
	mapId: int
	realMapId: int
	x: int
	y: int
	outdoor: bool
	subareaId: int
	worldMapId: int
	level: int

