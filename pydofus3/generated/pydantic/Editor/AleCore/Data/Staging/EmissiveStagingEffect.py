from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.MaterialStagingEffect import MaterialStagingEffect
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingEvolutiveVar import StagingEvolutiveVar
from pydofus3.not_generated.base import float_nan
from typing import ClassVar

class EmissiveStagingEffect(MaterialStagingEffect):
	TYPE: ClassVar[str] = "Emissive"
	factor: StagingEvolutiveVar[float_nan]

