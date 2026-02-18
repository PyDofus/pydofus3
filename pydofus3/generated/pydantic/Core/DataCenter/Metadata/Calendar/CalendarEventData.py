from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class CalendarEventData(D2oData):
	bundle_name: ClassVar[str] = "calendareventsdataroot"

	id: int
	categoryId: int
	nameId: i18n
	descriptionId: i18n
	criterion: str
	recommendedLevel: int
	rewards: str
	map: int
	picture: str

