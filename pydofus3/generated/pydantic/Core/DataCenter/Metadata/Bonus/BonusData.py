from pydantic import Field
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Bonus.BonusType import BonusType
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from typing import Union, Annotated

class BonusData(D2oData):
	bundle_name: ClassVar[str] = "bonusesdataroot"

	id: int
	type: Annotated[Union[BonusType, int], Field(union_mode='left_to_right')]
	amount: int
	criterionsIds: list[int]

