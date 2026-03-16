from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class NpcActionData(D2oData):
	bundle_name: ClassVar[str] = "npcactionsdataroot"

	id: int
	realId: int
	nameId: i18n

