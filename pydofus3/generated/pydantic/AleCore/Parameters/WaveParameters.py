from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Data.AleMatrix4x4 import AleMatrix4x4
from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel

class WaveParameters(MyBaseModel):
	waveFrequency: float_nan
	waveDirection: AleVector2
	waveDynamicsTexID: int
	waveDissolveDynamicsTexID: int
	waveDistoTexID: int
	waveDistoTexTiling: AleVector2
	waveDistoTexOffset: AleVector2
	waveDistoTexSpeed: AleVector2
	waveDistoPower: float_nan
	waveDistoSpeedStopMin1: float_nan
	waveDistoSpeedStopMax1: float_nan
	waveDistoSpeedStopMin2: float_nan
	waveDistoSpeedStopMax2: float_nan
	waveDistoSpeedStopMin3: float_nan
	waveDistoSpeedStopMax3: float_nan
	waveDistoSpeedStopMin4: float_nan
	waveDistoSpeedStopMax4: float_nan
	waveDissolveTexID1: int
	waveDissolveTexTiling1: AleVector2
	waveDissolveTexOffset1: AleVector2
	waveDissolveTexSpeed1: AleVector2
	waveDissolvePower1: float_nan
	waveDissolveFadeDistance: float_nan
	waveDissolveTexID2: int
	waveDissolveTexTiling2: AleVector2
	waveDissolveTexOffset2: AleVector2
	waveDissolveTexSpeed2: AleVector2
	waveDissolvePower2: float_nan
	waveDissolveShouldFade2: bool
	waveDissolveFadeStartRatio2: float_nan
	waveDissolveFadeDistanceRatio2: float_nan
	waveDissolveTexID3: int
	waveDissolveTexTiling3: AleVector2
	waveDissolveTexOffset3: AleVector2
	waveDissolveTexSpeed3: AleVector2
	waveDissolvePower3: float_nan
	waveDissolveShouldFade3: bool
	waveDissolveFadeStartRatio3: float_nan
	waveDissolveFadeDistanceRatio3: float_nan
	waveDissolveTexID4: int
	waveDissolveTexTiling4: AleVector2
	waveDissolveTexOffset4: AleVector2
	waveDissolveTexSpeed4: AleVector2
	waveDissolvePower4: float_nan
	waveDissolveShouldFade4: bool
	waveDissolveFadeStartRatio4: float_nan
	waveDissolveFadeDistanceRatio4: float_nan
	globalWaveMasksTexCamMatrix: AleMatrix4x4
	waterColor1: AleColor
	waterColor1Dissolved: AleColor
	waterColor2: AleColor
	waterColor2Dissolved: AleColor
	waterColor3: AleColor
	waterColor3Dissolved: AleColor
	waterColor4: AleColor
	waterColor4Dissolved: AleColor

