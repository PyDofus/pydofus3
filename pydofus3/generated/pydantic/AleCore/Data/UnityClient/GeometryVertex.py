from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import Color32
from pydofus3.not_generated.unity import Vector2
from pydofus3.not_generated.unity import Vector3

class GeometryVertex(MyBaseModel):
	pos: Vector3
	color: Color32
	uv: Vector2

