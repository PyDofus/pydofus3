from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class AlmanaxZodiacData(D2oData):
	bundle_name: ClassVar[str] = "almanaxzodiacsdataroot"

	id: int
	nameId: i18n
	descriptionId: i18n
	dateStart: str
	dateEnd: str
	picture: str

