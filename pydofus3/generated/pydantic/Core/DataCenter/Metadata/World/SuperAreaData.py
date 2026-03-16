from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class SuperAreaData(D2oData):
	bundle_name: ClassVar[str] = "superareasdataroot"

	id: int
	nameId: i18n
	worldmapId: int
	hasWorldMap: bool

