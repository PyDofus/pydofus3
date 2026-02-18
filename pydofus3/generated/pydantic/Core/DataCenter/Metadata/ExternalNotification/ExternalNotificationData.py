from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class ExternalNotificationData(D2oData):
	bundle_name: ClassVar[str] = "externalnotificationsdataroot"

	id: int
	categoryId: int
	iconId: int
	colorId: int
	descriptionId: i18n
	defaultEnable: bool
	defaultSound: bool
	defaultMultiAccount: bool
	defaultNotify: bool
	name: str
	messageId: i18n

