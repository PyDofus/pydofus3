from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import WrappedList
from pydofus3.not_generated.base import float_nan

class CompanionCharacteristicData(D2oData):
	bundle_name: ClassVar[str] = "companioncharacteristicsdataroot"

	id: int
	caracId: int
	companionId: int
	order: int
	statPerLevelRange: list[WrappedList[float_nan]]

