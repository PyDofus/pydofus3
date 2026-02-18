from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.generated.pydantic.AleCore.Data.AleVector4 import AleVector4
from pydofus3.generated.pydantic.AleCore.Data.UVModes import UVModes
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.MaterialStagingEffect import MaterialStagingEffect
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingEvolutiveVar import StagingEvolutiveVar
from typing import Union, Annotated

class DistortionStagingEffect(MaterialStagingEffect):
	noiseTexTiling: StagingEvolutiveVar[AleVector2]
	noiseTexOffset: StagingEvolutiveVar[AleVector2]
	uvMode: Annotated[Union[UVModes, int], Field(union_mode='left_to_right')]
	distortionVector: StagingEvolutiveVar[AleVector4]

