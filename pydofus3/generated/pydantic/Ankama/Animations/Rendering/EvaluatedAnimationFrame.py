from pydofus3.generated.pydantic.Ankama.Animations.NamedTransformPositional import NamedTransformPositional
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.AnimationGeometryVertex import AnimationGeometryVertex
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.CustomBounds import CustomBounds
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.MaterialDescriptor import MaterialDescriptor
from pydofus3.not_generated.base import MyBaseModel

class EvaluatedAnimationFrame(MyBaseModel):
	vertexBuffer: list[AnimationGeometryVertex]
	triangleBuffer: list[int]
	materialDescriptors: list[MaterialDescriptor]
	materialOffsets: list[int]
	namedTransformIndicesToBaseMaterialOffsets: dict[int, int]
	nodeBounds: dict[str, CustomBounds]
	collisionBounds: list[CustomBounds]
	namedTransformPositions: list[NamedTransformPositional]
	bounds: CustomBounds
	stencilSubMeshIndex: int
	stencilBounds: CustomBounds

