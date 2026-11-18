from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class HaloShapeData(D2oData):
	bundle_name: ClassVar[str] = "haloshapedataroot"

	id: int
	shapeOrder: int
	haloId: int
	effectShape: str
	color: int
	markId: int

