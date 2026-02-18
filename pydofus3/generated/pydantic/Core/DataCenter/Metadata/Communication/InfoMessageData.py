from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class InfoMessageData(D2oData):
	bundle_name: ClassVar[str] = "infomessagesdataroot"

	typeId: int
	messageId: int
	textId: i18n

