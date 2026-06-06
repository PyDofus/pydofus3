from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class LobbyTagData(D2oData):
	bundle_name: ClassVar[str] = "lobbytagsdataroot"

	id: int
	nameId: i18n
	concurrentTags: list[int]

