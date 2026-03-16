from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingManager import StagingManager
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingSequence import StagingSequence
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingShotNode import StagingShotNode
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class StagingSequencer(MyBaseModel):
	IntensityDiffTreshold: ClassVar[float_nan] = 0.001
	sequence: StagingSequence
	stagingManager: StagingManager
	fastForward: bool
	playingShotNodes: list[StagingShotNode]
	duration: float_nan
	shotNodes: list[StagingShotNode]
	shotNodesIds: dict[str, StagingShotNode]
	intensityMultiplier: float_nan

	class SequenceEndCallback(MyBaseModel):
		pass

	class SequenceEventCallback(MyBaseModel):
		pass

