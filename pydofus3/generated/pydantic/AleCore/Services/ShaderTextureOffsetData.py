from pydofus3.generated.pydantic.AleCore.Services.IShaderTimeData import IShaderTimeData
from pydofus3.not_generated.unity import Vector2

class ShaderTextureOffsetData(IShaderTimeData):
	customTime: Vector2
	timeSpeed: Vector2
	timeOffset: Vector2
	linkToWind: bool

