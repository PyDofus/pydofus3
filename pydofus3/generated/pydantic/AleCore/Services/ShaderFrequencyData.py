from pydofus3.generated.pydantic.AleCore.Services.IShaderTimeData import IShaderTimeData
from pydofus3.not_generated.base import float_nan

class ShaderFrequencyData(IShaderTimeData):
	advancement: float_nan
	frequency: float_nan
	timeOffset: float_nan
	linkToWind: bool

