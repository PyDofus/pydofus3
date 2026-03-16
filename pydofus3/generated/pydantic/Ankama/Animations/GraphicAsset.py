from pydofus3.generated.pydantic.Ankama.Animations.Rendering.AnimationGeometryVertex import AnimationGeometryVertex
from pydofus3.not_generated.base import MyBaseModel

class GraphicAsset(MyBaseModel):
	vertices: list[AnimationGeometryVertex]
	triangles: list[int]

