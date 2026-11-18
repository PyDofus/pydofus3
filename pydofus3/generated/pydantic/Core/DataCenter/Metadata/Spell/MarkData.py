from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import float_nan
from typing import ClassVar

class MarkData(D2oData):
	bundle_name: ClassVar[str] = "marksdataroot"

	id: int
	color: str
	gfxID: int
	directionId: int
	strataId: int
	offsetX: int
	offsetY: int
	scaleX: float_nan
	scaleY: float_nan
	rotation: int
	frameOffset: int
	vfxId: int
	vfxDuration: int
	vfxColors: str
	startVfxId: int
	endVfxId: int
	materialName: str
	tooltipTextureName: str

