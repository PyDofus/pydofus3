from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class CharacteristicData(D2oData):
	bundle_name: ClassVar[str] = "characteristicsdataroot"

	id: int
	keyword: str
	nameId: i18n
	asset: str
	categoryId: int
	visible: bool
	order: int
	scaleFormulaId: int
	upgradable: bool

