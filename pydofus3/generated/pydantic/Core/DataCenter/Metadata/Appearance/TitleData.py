from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class TitleData(D2oData):
	bundle_name: ClassVar[str] = "titlesdataroot"

	id: int
	nameMaleId: i18n
	nameFemaleId: i18n
	visible: bool
	categoryId: int

