from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingManager import StagingManager
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingSequence import StagingSequence
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingShotNode import StagingShotNode
from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import float_nan

class StagingSequencer(MyBaseModel):
	sequence: StagingSequence
	stagingManager: StagingManager
	fastForward: bool
	playingShotNodes: list[StagingShotNode]
	duration: float_nan
	shotNodes: list[StagingShotNode]
	intensityMultiplier: float_nan
	class SequenceEndCallback(MyBaseModel):
		pass
	class SequenceEventCallback(MyBaseModel):
		pass

