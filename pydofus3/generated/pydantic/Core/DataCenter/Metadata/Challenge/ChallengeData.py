from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class ChallengeData(D2oData):
	bundle_name: ClassVar[str] = "challengesdataroot"

	id: int
	nameId: i18n
	descriptionId: i18n
	incompatibleChallenges: list[int]
	categoryId: int
	iconId: int
	completionCriterion: str
	activationCriterion: str
	targetMonsterId: int

