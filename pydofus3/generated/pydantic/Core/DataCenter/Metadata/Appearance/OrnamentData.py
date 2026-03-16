from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class OrnamentData(D2oData):
	bundle_name: ClassVar[str] = "ornamentsdataroot"

	id: int
	nameId: i18n
	visible: bool
	assetId: int
	iconId: int
	order: int

