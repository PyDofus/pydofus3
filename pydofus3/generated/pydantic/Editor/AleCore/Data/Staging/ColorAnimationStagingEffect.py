from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.MaterialStagingEffect import MaterialStagingEffect
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingEvolutiveVar import StagingEvolutiveVar
from pydofus3.not_generated.base import float_nan

class ColorAnimationStagingEffect(MaterialStagingEffect):
	finalColor: StagingEvolutiveVar[AleColor]
	alpha: StagingEvolutiveVar[float_nan]
	frequency: StagingEvolutiveVar[float_nan]
	resetTime: bool
	noiseOffset: StagingEvolutiveVar[AleVector2]
	noiseStrength: StagingEvolutiveVar[float_nan]
	noiseSpeed: StagingEvolutiveVar[float_nan]
	shouldSmooth: bool

