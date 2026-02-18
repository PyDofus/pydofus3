from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Effect.EffectInstanceData import EffectInstanceData
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Effect.Instance.EffectInstanceInteger import EffectInstanceInteger

class EffectInstanceMount(EffectInstanceData):
	id: int
	expirationDate: int
	model: int
	name: str
	owner: str
	level: int
	sex: bool
	isRideable: bool
	isFeconded: bool
	isFecondationReady: bool
	reproductionCount: int
	reproductionCountMax: int
	effects: list[EffectInstanceInteger]
	capacities: list[int]

