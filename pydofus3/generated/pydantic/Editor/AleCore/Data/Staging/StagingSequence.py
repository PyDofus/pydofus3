from pydantic import Field
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingExclusivityResolveMethodEnum import StagingExclusivityResolveMethodEnum
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingShot import StagingShot
from pydofus3.not_generated.base import MyBaseModel
from typing import Annotated, Union

class StagingSequence(MyBaseModel):
	id: str
	uniqueId: int
	exclusiveGroupId: str
	exclusivityResolveMethod: Annotated[Union[StagingExclusivityResolveMethodEnum, int], Field(union_mode='left_to_right')]
	stagingShots: list[StagingShot]

