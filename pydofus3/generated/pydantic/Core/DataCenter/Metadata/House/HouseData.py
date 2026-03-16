from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class HouseData(D2oData):
	bundle_name: ClassVar[str] = "housesdataroot"

	typeId: int
	defaultPrice: int
	nameId: i18n
	descriptionId: i18n
	gfxId: int
	roomCount: int

