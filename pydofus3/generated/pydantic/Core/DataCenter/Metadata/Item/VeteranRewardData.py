from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class VeteranRewardData(D2oData):
	bundle_name: ClassVar[str] = "veteranrewardsdataroot"

	id: int
	requiredSubDays: int
	itemGID: int
	itemQuantity: int

