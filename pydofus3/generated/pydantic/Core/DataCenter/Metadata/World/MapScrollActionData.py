from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class MapScrollActionData(D2oData):
	bundle_name: ClassVar[str] = "mapscrollactionsdataroot"

	id: int
	rightExists: bool
	bottomExists: bool
	leftExists: bool
	topExists: bool
	rightMapId: int
	bottomMapId: int
	leftMapId: int
	topMapId: int

