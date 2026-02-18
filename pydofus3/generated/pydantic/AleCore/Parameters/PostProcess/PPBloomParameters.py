from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Parameters.PostProcess.IPostProcessParameters import IPostProcessParameters
from pydofus3.not_generated.base import float_nan

class PPBloomParameters(IPostProcessParameters):
	threshold: float_nan
	intensity: float_nan
	scatter: float_nan
	color: AleColor

