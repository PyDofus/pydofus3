from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class MapReferenceData(D2oData):
	bundle_name: ClassVar[str] = "mapreferencesdataroot"

	id: int
	mapId: int
	cellId: int

