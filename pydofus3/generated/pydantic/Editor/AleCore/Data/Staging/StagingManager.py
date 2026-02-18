from pydofus3.generated.pydantic.AleCore.Services.ShaderFrequencyManager import ShaderFrequencyManager
from pydofus3.not_generated.base import MyBaseModel


class StagingManager(MyBaseModel):
	shaderFrequencyManager: ShaderFrequencyManager
	allowMapEffects: bool
	mapRendered: bool

