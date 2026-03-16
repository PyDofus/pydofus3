from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class NotificationData(D2oData):
	bundle_name: ClassVar[str] = "notificationsdataroot"

	id: int
	titleId: i18n
	messageId: i18n
	iconId: int
	typeId: int
	trigger: str
	cantBeClosed: bool

