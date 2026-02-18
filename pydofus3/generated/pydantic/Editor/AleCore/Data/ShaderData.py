from pydofus3.generated.pydantic.AleCore.Parameters.Shader.IShaderParameters import IShaderParameters
from pydofus3.not_generated.base import MyBaseModel


class ShaderData(MyBaseModel):
	shaderParameters: list[IShaderParameters]
	gfxId: int
	unique: bool
	isStagingTarget: bool
	stagingId: str

