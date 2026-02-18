from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class HouseData(D2oData):
	bundle_name: ClassVar[str] = "housesdataroot"

	typeId: int
	defaultPrice: int
	nameId: i18n
	descriptionId: i18n
	gfxId: int
	roomCount: int

