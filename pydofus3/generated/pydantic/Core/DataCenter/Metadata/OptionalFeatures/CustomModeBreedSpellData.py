from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class CustomModeBreedSpellData(D2oData):
	bundle_name: ClassVar[str] = "custommodebreedspellsdataroot"

	id: int
	pairId: int
	breedId: int
	isInitialSpell: bool
	isHidden: bool

