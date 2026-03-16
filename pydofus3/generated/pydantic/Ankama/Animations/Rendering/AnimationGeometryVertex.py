from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import Vector2
from pydofus3.not_generated.unity import Vector3

class AnimationGeometryVertex(MyBaseModel):
	pos: Vector3
	uv: Vector2
	multiplicativeColor: int
	additiveColor: int

