from pydofus3.generated.pydantic.AleCore.Data.AleVector4 import AleVector4
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.MaterialStagingEffect import MaterialStagingEffect
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingEvolutiveVar import StagingEvolutiveVar
from pydofus3.not_generated.base import float_nan
from typing import ClassVar

class ScaleStagingEffect(MaterialStagingEffect):
	TYPE: ClassVar[str] = "Scale"
	axesVector: StagingEvolutiveVar[AleVector4]
	pivotVector: StagingEvolutiveVar[AleVector4]
	frequency: StagingEvolutiveVar[float_nan]
	resetTime: bool
	amplitude: StagingEvolutiveVar[float_nan]
	offset: StagingEvolutiveVar[float_nan]
	noiseStrengthVector: StagingEvolutiveVar[AleVector4]
	noiseOffsetVector: StagingEvolutiveVar[AleVector4]

