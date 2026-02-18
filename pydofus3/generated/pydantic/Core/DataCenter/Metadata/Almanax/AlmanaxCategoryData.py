from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.i18n import i18n

class AlmanaxCategoryData(D2oData):
	bundle_name: ClassVar[str] = "almanaxcategoriesdataroot"

	id: int
	nameId: i18n
	protectorNameId: i18n
	protectorDescriptionId: i18n
	protectorIllustrationId: int

