from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class LobbyTagData(D2oData):
	bundle_name: ClassVar[str] = "lobbytagsdataroot"

	id: int
	nameId: int
	concurrentTags: list[int]

