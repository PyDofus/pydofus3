from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Data.Sound.PlaylistSet import PlaylistSet
from pydofus3.generated.pydantic.AleCore.Data.UnityClient.ClientCellData import ClientCellData
from pydofus3.generated.pydantic.AleCore.Data.UnityClient.ClientIsometricMergedMapElements import ClientIsometricMergedMapElements
from pydofus3.generated.pydantic.AleCore.Data.UnityClient.ClientMapAnimatedElement import ClientMapAnimatedElement
from pydofus3.generated.pydantic.AleCore.Data.UnityClient.ClientMergedMapElements import ClientMergedMapElements
from pydofus3.generated.pydantic.AleCore.Data.UnityClient.ClientParticlesParameters import ClientParticlesParameters
from pydofus3.generated.pydantic.AleCore.Data.UnityClient.LocalizedSound import LocalizedSound
from pydofus3.generated.pydantic.AleCore.Data.UnityClient.MapEffectsConfigurations import MapEffectsConfigurations
from pydofus3.generated.pydantic.AleCore.Data.UnityClient.MaterialData import MaterialData
from pydofus3.generated.pydantic.AleCore.Data.UnityClient.ShaderData import ShaderData
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingSequence import StagingSequence
from pydofus3.not_generated.base import MyBaseModel

class ClientMapData(MyBaseModel):
	id: int
	topNeighbourId: int
	bottomNeighbourId: int
	leftNeighbourId: int
	rightNeighbourId: int
	backgroundColor: AleColor
	playlistSet: PlaylistSet
	backgroundMapElements: list[ClientMergedMapElements]
	middlegroundMapElements: list[ClientIsometricMergedMapElements]
	foregroundMapElements: list[ClientMergedMapElements]
	mapAnimatedElements: list[ClientMapAnimatedElement]
	backgroundMaterialData: MaterialData
	middlegroundMaterialData: MaterialData
	foregroundMaterialData: MaterialData
	particlesShaderData: list[ShaderData]
	shaderVariants: list[int]
	particlesParameters: list[ClientParticlesParameters]
	cellsData: list[ClientCellData]
	topArrowCellList: list[int]
	leftArrowCellList: list[int]
	bottomArrowCellList: list[int]
	rightArrowCellList: list[int]
	mapEffectsConfigurations: MapEffectsConfigurations
	stagingSequences: list[StagingSequence]
	localizedSounds: list[LocalizedSound]

