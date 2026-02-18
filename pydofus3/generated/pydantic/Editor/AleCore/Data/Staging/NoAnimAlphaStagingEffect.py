from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Utils.ObjectDisplayBehaviour import ObjectDisplayBehaviour
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.MaterialStagingEffect import MaterialStagingEffect
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingEvolutiveVar import StagingEvolutiveVar
from pydofus3.not_generated.base import float_nan
from typing import Union, Annotated

class NoAnimAlphaStagingEffect(MaterialStagingEffect):
	effectDisplay: Annotated[Union[ObjectDisplayBehaviour, int], Field(union_mode='left_to_right')]
	alpha: StagingEvolutiveVar[float_nan]
	color: StagingEvolutiveVar[AleColor]

