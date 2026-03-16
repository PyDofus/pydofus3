from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class InfoMessageData(D2oData):
	bundle_name: ClassVar[str] = "infomessagesdataroot"

	typeId: int
	messageId: int
	textId: i18n

