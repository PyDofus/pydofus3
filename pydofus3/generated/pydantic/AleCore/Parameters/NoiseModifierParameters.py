from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.not_generated.base import MyBaseModel


class NoiseModifierParameters(MyBaseModel):
	mapNoiseModifierTexId: int
	mapNoiseModifierTiling: AleVector2
	mapNoiseModifierOffset: AleVector2
	mapNoiseModifierSpeed: AleVector2

