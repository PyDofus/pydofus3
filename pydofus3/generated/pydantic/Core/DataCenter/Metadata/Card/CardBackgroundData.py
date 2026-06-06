from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class CardBackgroundData(D2oData):
	bundle_name: ClassVar[str] = "cardbackgroundsdataroot"

	id: int
	nameId: i18n
	isDefault: bool
	picture: str

