from pydantic import Field
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Bonus.BonusCriterionType import BonusCriterionType
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from typing import Union, Annotated

class BonusCriterionData(D2oData):
	bundle_name: ClassVar[str] = "bonusescriterionsdataroot"

	id: int
	type: Annotated[Union[BonusCriterionType, int], Field(union_mode='left_to_right')]
	value: int

