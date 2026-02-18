from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.generated.pydantic.AleCore.Data.AleVector4 import AleVector4
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.MaterialStagingEffect import MaterialStagingEffect
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingEvolutiveVar import StagingEvolutiveVar
from pydofus3.not_generated.base import float_nan

class TranslationStagingEffect(MaterialStagingEffect):
	directionVector: StagingEvolutiveVar[AleVector4]
	frequency: StagingEvolutiveVar[float_nan]
	resetTime: bool
	amplitude: StagingEvolutiveVar[float_nan]
	offset: StagingEvolutiveVar[float_nan]
	noiseStrenghVector: StagingEvolutiveVar[AleVector4]
	noiseSpeedVector: StagingEvolutiveVar[AleVector2]
	noiseOffset: StagingEvolutiveVar[AleVector2]

