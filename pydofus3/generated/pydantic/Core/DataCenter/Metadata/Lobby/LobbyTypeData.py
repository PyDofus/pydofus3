from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class LobbyTypeData(D2oData):
	bundle_name: ClassVar[str] = "lobbytypesdataroot"

	id: int
	nameId: int
	tags: list[int]
	minMember: int
	maxMember: int

