from pydofus3.generated.pydantic.AleCore.Data.AleAnimationCurve import AleAnimationCurve
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingEffectsPack import StagingEffectsPack
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel

class StagingShot(MyBaseModel):
	id: str
	previousShot: str
	delay: float_nan
	duration: float_nan
	intensityMultiplierSensitivity: float_nan
	skipIfInstant: bool
	intensityCurve: AleAnimationCurve
	stagingEffectsPacks: list[StagingEffectsPack]

