from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.generated.pydantic.AleCore.Data.AleVector4 import AleVector4
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.MaterialStagingEffect import MaterialStagingEffect
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingEvolutiveVar import StagingEvolutiveVar
from pydofus3.not_generated.base import float_nan
from typing import ClassVar

class DissolveStagingEffect(MaterialStagingEffect):
	TYPE: ClassVar[str] = "Dissolve"
	dissolveTexTiling: StagingEvolutiveVar[AleVector2]
	dissolveTexOffset: StagingEvolutiveVar[AleVector2]
	dissolveTexSpeedVector: StagingEvolutiveVar[AleVector4]
	alphaClip: StagingEvolutiveVar[float_nan]
	alphaClipFadeWidth: StagingEvolutiveVar[float_nan]
	burnWidth: StagingEvolutiveVar[float_nan]
	burnColor: StagingEvolutiveVar[AleColor]
	burnColorPower: StagingEvolutiveVar[float_nan]

