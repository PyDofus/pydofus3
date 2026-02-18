from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class AlignmentRankData(D2oData):
	bundle_name: ClassVar[str] = "alignmentranksdataroot"

	id: int
	orderId: int
	nameId: i18n
	descriptionId: i18n
	minimumAlignment: int

