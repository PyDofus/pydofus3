from pydofus3.generated.pydantic.Ankama.Animations.Animator2D import Animator2D
from pydofus3.generated.pydantic.hau import hau
from pydofus3.not_generated.base import MyBaseModel

class BufferRequest(MyBaseModel):
	target: Animator2D
	animation: hau
	id: int

