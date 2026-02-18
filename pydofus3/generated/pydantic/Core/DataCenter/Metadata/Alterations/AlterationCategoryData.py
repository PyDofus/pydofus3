from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.i18n import i18n

class AlterationCategoryData(D2oData):
	bundle_name: ClassVar[str] = "alterationcategoriesdataroot"

	id: int
	nameId: i18n
	parentId: int

