from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class BreachWorldMapSectorData(D2oData):
	bundle_name: ClassVar[str] = "breachworldmapsectorsdataroot"

	id: int
	sectorNameId: i18n
	legendId: i18n
	sectorIcon: str
	minStage: int
	maxStage: int

