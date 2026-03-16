from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class ServerData(D2oData):
	bundle_name: ClassVar[str] = "serversdataroot"

	id: int
	nameId: i18n
	commentId: i18n
	language: str
	populationId: int
	gameTypeId: int
	communityId: int
	monoAccount: bool
	illus: str

