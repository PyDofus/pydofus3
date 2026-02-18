from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import float_nan

class WindParameters(MyBaseModel):
	windPower: float_nan
	windModelTexID: int
	mainWindNoiseTexID: int
	mainWindNoiseTiling: AleVector2
	mainWindNoiseTilingMultiplier: float_nan
	mainWindNoiseDirection: AleVector2
	mainWindNoiseDirectionMultiplier: float_nan
	mainWindAmplitudeMultiplierCursor: float_nan
	mainWindAmplitudeCurvePower: float_nan
	mainWindFrequencyCurvePower: float_nan
	swingNoiseTexID: int
	swingNoiseTiling: AleVector2
	swingNoiseTilingMultiplier: float_nan
	swingNoiseDirection: AleVector2
	swingNoiseDirectionMultiplier: float_nan
	swingAmplitudeMultiplierCursor: float_nan
	swingAmplitudeCurvePower: float_nan
	swingFrequencyCurvePower: float_nan
	mainWindAmplitudeMultiplier: float_nan
	mainWindFrequencyMultiplier: float_nan
	swingFrequencyMultiplier: float_nan
	swingAmplitudeMultiplier: float_nan
	minimumSwingAmplitude: float_nan
	windSwingNoiseSpeed: AleVector2

