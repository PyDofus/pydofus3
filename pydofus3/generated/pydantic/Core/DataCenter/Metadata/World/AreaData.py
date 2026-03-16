from pydofus3.generated.pydantic.Core.DataCenter.Types.Rectangle import Rectangle
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class AreaData(D2oData):
	bundle_name: ClassVar[str] = "areasdataroot"

	id: int
	nameId: i18n
	superAreaId: int
	containHouses: bool
	containPaddocks: bool
	bounds: Rectangle
	worldmapId: int
	subareaIds: list[int]
	hasWorldMap: bool
	hasSuggestion: bool

