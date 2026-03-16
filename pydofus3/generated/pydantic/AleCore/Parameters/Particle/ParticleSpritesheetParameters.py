from pydofus3.generated.pydantic.AleCore.Data.AleConstantOr2Constants import AleConstantOr2Constants
from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurve import AleMinMaxCurve
from pydofus3.generated.pydantic.AleCore.Data.AleVector2Int import AleVector2Int
from pydofus3.not_generated.base import MyBaseModel

class ParticleSpritesheetParameters(MyBaseModel):
	tiles: AleVector2Int
	frameOverTime: AleMinMaxCurve
	startFrame: AleConstantOr2Constants
	cycles: int

