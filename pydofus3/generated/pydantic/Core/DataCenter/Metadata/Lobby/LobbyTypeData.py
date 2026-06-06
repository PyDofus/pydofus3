from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class LobbyTypeData(D2oData):
	bundle_name: ClassVar[str] = "lobbytypesdataroot"

	id: int
	nameId: i18n
	tags: list[int]
	minMember: int
	maxMember: int

