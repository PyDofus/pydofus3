from pydantic import Field
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Progression.DofusProgressionStepType import DofusProgressionStepType
from pydofus3.not_generated.base import MyBaseModel
from typing import Annotated, Union

class DofusProgressionStepData(MyBaseModel):
	order: int
	value: int
	type: Annotated[Union[DofusProgressionStepType, int], Field(union_mode='left_to_right')]
	hideObjectives: bool

