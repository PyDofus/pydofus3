from pydantic import Field
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.IStagingEffect import IStagingEffect
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.Sequencing.StagingEventTypeEnum import StagingEventTypeEnum
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.Sequencing.StagingSequencer import StagingSequencer
from typing import Union, Annotated

class SequenceEventStagingEffect(IStagingEffect):
	sequencer: StagingSequencer
	stagingEventType: Annotated[Union[StagingEventTypeEnum, int], Field(union_mode='left_to_right')]

