from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingEvolutiveVar import StagingEvolutiveVar
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class SetFmodParamStagingEffect(MyBaseModel):
	TYPE: ClassVar[str] = "SetFmodParam"
	paramName: str
	startValue: float_nan
	endValue: StagingEvolutiveVar[float_nan]

