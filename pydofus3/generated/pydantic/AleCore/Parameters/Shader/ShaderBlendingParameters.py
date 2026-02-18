from pydofus3.generated.pydantic.AleCore.Parameters.Shader.IShaderParameters import IShaderParameters

class ShaderBlendingParameters(IShaderParameters):
	sourceFactor: int
	blendOperation: int
	destinationFactor: int

