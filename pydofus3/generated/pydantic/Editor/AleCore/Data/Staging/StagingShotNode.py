from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.IStagingEffect import IStagingEffect
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingShot import StagingShot
from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import float_nan

class StagingShotNode(MyBaseModel):
	shot: StagingShot
	childs: list['StagingShotNode']
	parent: 'StagingShotNode'
	effectInstances: list[IStagingEffect]
	intensityCurve: UnityEngine.AnimationCurve
	initialized: bool
	lastIntensity: float_nan

