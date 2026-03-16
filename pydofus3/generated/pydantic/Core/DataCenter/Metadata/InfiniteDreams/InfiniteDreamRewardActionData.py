from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Effect.EffectInstanceData import EffectInstanceData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class InfiniteDreamRewardActionData(D2oData):
	bundle_name: ClassVar[str] = "infinitedreamrewardactionsdataroot"

	id: int
	effect: EffectInstanceData
	duration: int
	isAlly: bool

