from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Effect.EffectInstanceData import EffectInstanceData
from pydofus3.not_generated.base import MyBaseModel

class WrappedEffectInstanceList(MyBaseModel):
	values: list[EffectInstanceData]

