from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.IStagingEffect import IStagingEffect
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingEvolutiveVar import StagingEvolutiveVar
from pydofus3.not_generated.base import float_nan

class SetFmodParamStagingEffect(IStagingEffect):
	paramName: str
	startValue: float_nan
	endValue: StagingEvolutiveVar[float_nan]

