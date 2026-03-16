from pydofus3.generated.pydantic.Ankama.Animations.Rendering.AnimationGeometryVertex import AnimationGeometryVertex
from pydofus3.generated.pydantic.Ankama.Animations.SkinAssetPart import SkinAssetPart
from pydofus3.not_generated.base import MyBaseModel

class SkinAsset(MyBaseModel):
	m_values: list[SkinAssetPart]
	m_keys: list[str]
	skinParts: dict[str, SkinAssetPart]
	triangles: list[int]
	vertices: list[AnimationGeometryVertex]
	referencedSymbols: list[str]
	emptyCustomisations: list[str]
	customEmptyCustomisations: set[str]

