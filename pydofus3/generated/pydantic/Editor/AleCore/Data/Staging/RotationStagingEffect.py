from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.generated.pydantic.AleCore.Data.AleVector4 import AleVector4
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.MaterialStagingEffect import MaterialStagingEffect
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingEvolutiveVar import StagingEvolutiveVar
from pydofus3.not_generated.base import float_nan

class RotationStagingEffect(MaterialStagingEffect):
	rotationCenterVector: StagingEvolutiveVar[AleVector4]
	frequency: StagingEvolutiveVar[float_nan]
	resetTime: bool
	amplitude: StagingEvolutiveVar[float_nan]
	offset: StagingEvolutiveVar[float_nan]
	noiseStrength: StagingEvolutiveVar[float_nan]
	noiseSpeed: StagingEvolutiveVar[float_nan]
	noiseOffset: StagingEvolutiveVar[AleVector2]

