from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class SpeakingItemTextData(D2oData):
	bundle_name: ClassVar[str] = "speakingitemstextsdataroot"

	textId: int
	textProba: float_nan
	textStringId: i18n
	textLevel: int
	textSound: int
	textRestriction: str

