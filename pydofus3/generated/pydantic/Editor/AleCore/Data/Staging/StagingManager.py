from pydofus3.generated.pydantic.AleCore.Services.ShaderFrequencyManager import ShaderFrequencyManager
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.MapAnimatedElements.IMapAnimatedElement import IMapAnimatedElement
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.Sequencing.StagingSequencer import StagingSequencer
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingSequence import StagingSequence
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import Material
from pydofus3.not_generated.unity import ParticleSystem

class StagingManager(MyBaseModel):
	stagingMaterialsTargets: dict[str, list[Material]]
	stagingParticlesTargets: dict[str, list[ParticleSystem]]
	stagingMapAnimatedElementsTargets: dict[str, list[IMapAnimatedElement]]
	stagingSequences: dict[int, StagingSequence]
	playingSequencers: dict[str, StagingSequencer]
	shaderFrequencyManager: ShaderFrequencyManager
	allowMapEffects: bool
	mapRendered: bool

