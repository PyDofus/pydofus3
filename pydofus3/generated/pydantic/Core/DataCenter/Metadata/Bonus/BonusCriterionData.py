from pydantic import Field
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Bonus.BonusCriterionType import BonusCriterionType
from pydofus3.not_generated.base import D2oData
from typing import Annotated, Union
from typing import ClassVar

class BonusCriterionData(D2oData):
	bundle_name: ClassVar[str] = "bonusescriterionsdataroot"

	id: int
	type: Annotated[Union[BonusCriterionType, int], Field(union_mode='left_to_right')]
	value: int

