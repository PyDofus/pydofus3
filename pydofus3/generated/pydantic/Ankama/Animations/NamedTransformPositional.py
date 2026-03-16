from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import Quaternion
from pydofus3.not_generated.unity import Vector3

class NamedTransformPositional(MyBaseModel):
	id: int
	position: Vector3
	rotation: Quaternion

