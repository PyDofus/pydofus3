from pydofus3.generated.pydantic.AleCore.Parameters.Shader.IShaderParameters import IShaderParameters
from pydofus3.not_generated.base import MyBaseModel

class ParticlesShaderParameters(MyBaseModel):
	textureId: int
	shaderParameters: list[IShaderParameters]
	isStagingTarget: bool
	stagingId: str

