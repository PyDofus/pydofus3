from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class InfiniteDreamTrialData(D2oData):
	bundle_name: ClassVar[str] = "infinitedreamtrialsdataroot"

	id: int
	nameId: i18n
	descriptionId: i18n
	seed: str
	achievementId: int
	achievementIntensity: int
	picture: str

