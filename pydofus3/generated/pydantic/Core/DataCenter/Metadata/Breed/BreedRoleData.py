from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class BreedRoleData(D2oData):
	bundle_name: ClassVar[str] = "breedrolesdataroot"

	id: int
	nameId: i18n
	descriptionId: i18n
	assetId: int
	color: int

