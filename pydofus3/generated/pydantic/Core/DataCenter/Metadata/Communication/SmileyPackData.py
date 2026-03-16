from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class SmileyPackData(D2oData):
	bundle_name: ClassVar[str] = "smileypacksdataroot"

	id: int
	nameId: i18n
	order: int
	smileys: list[int]

