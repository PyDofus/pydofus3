from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class CardBackgroundData(D2oData):
	bundle_name: ClassVar[str] = "cardbackgroundsdataroot"

	id: int
	nameId: int
	isDefault: bool
	picture: str

