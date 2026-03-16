from pydantic import Field
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.Sequencing.StagingEventTypeEnum import StagingEventTypeEnum
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.Sequencing.StagingSequencer import StagingSequencer
from pydofus3.not_generated.base import MyBaseModel
from typing import Annotated, Union
from typing import ClassVar

class SequenceEventStagingEffect(MyBaseModel):
	TYPE: ClassVar[str] = "SequenceEvent"
	sequencer: StagingSequencer
	stagingEventType: Annotated[Union[StagingEventTypeEnum, int], Field(union_mode='left_to_right')]

