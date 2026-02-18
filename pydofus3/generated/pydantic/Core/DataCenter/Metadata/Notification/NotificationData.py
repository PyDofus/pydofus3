from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class NotificationData(D2oData):
	bundle_name: ClassVar[str] = "notificationsdataroot"

	id: int
	titleId: i18n
	messageId: i18n
	iconId: int
	typeId: int
	trigger: str
	cantBeClosed: bool

