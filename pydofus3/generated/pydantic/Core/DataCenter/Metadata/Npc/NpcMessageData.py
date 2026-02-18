from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class NpcMessageData(D2oData):
	bundle_name: ClassVar[str] = "npcmessagesdataroot"

	id: int
	messageId: i18n
	messageParams: list[str]
	messageSkinId: int
	messageBubblePosition: int
	messageNpcMoodId: int

