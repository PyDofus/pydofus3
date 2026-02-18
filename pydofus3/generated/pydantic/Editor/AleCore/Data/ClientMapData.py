from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Data.LocalizedSound import LocalizedSound
from pydofus3.generated.pydantic.AleCore.Data.Sound.PlaylistSet import PlaylistSet
from pydofus3.generated.pydantic.AleCore.Parameters.MapNoiseModifierConfiguration import MapNoiseModifierConfiguration
from pydofus3.generated.pydantic.AleCore.Parameters.MapPostProcessConfiguration import MapPostProcessConfiguration
from pydofus3.generated.pydantic.AleCore.Parameters.MapWaveConfiguration import MapWaveConfiguration
from pydofus3.generated.pydantic.AleCore.Parameters.MapWindConfiguration import MapWindConfiguration
from pydofus3.generated.pydantic.Editor.AleCore.Data.ClientAnimatedElementTransform import ClientAnimatedElementTransform
from pydofus3.generated.pydantic.Editor.AleCore.Data.ClientCellData import ClientCellData
from pydofus3.generated.pydantic.Editor.AleCore.Data.ClientElementTransform import ClientElementTransform
from pydofus3.generated.pydantic.Editor.AleCore.Data.ClientInteractiveElementTransform import ClientInteractiveElementTransform
from pydofus3.generated.pydantic.Editor.AleCore.Data.ClientParticlesParameters import ClientParticlesParameters
from pydofus3.generated.pydantic.Editor.AleCore.Data.ClientSortableElementTransform import ClientSortableElementTransform
from pydofus3.generated.pydantic.Editor.AleCore.Data.IClientInteractiveElement import IClientInteractiveElement
from pydofus3.generated.pydantic.Editor.AleCore.Data.MaterialData import MaterialData
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingSequence import StagingSequence
from pydofus3.not_generated.base import MyBaseModel


class ClientMapData(MyBaseModel):
	topNeighbourId: int
	bottomNeighbourId: int
	leftNeighbourId: int
	rightNeighbourId: int
	backgroundColor: AleColor
	playlistSet: PlaylistSet
	backgroundElements: list[ClientElementTransform]
	sortableElements: list[ClientSortableElementTransform]
	foregroundElements: list[ClientElementTransform]
	animatedElements: list[ClientAnimatedElementTransform]
	refractionElements: list[ClientElementTransform]
	interactiveElements: list[IClientInteractiveElement]
	boundingBoxes: list[ClientInteractiveElementTransform]
	particlesParameters: list[ClientParticlesParameters]
	foregroundMaterialData: MaterialData
	backgroundMaterialData: MaterialData
	sortableMaterialData: MaterialData
	cellsData: list[ClientCellData]
	topArrowCellList: list[int]
	leftArrowCellList: list[int]
	bottomArrowCellList: list[int]
	rightArrowCellList: list[int]
	mapWindConfiguration: MapWindConfiguration
	mapPostProcessConfiguration: MapPostProcessConfiguration
	mapWaveConfiguration: MapWaveConfiguration
	mapNoiseModifierConfiguration: MapNoiseModifierConfiguration
	stagingSequences: list[StagingSequence]
	localizedSounds: list[LocalizedSound]

