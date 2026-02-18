from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class ChatChannelData(D2oData):
	bundle_name: ClassVar[str] = "chatchannelsdataroot"

	id: int
	nameId: i18n
	descriptionId: i18n
	shortcut: str
	isPrivate: bool

