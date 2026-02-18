from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import float_nan

class ShaderWindParentParameters(MyBaseModel):
	bendCenter: AleVector2
	bendStart: AleVector2
	bendAxe: AleVector2
	bendAxeMultiplier: float_nan
	flexibility: float_nan
	shouldSwing: bool
	windSwingNoiseSpeedCoef: float_nan
	windSwingNoiseAmplitude: float_nan

