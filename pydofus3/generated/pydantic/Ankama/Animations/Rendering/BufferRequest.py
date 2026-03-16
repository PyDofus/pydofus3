from pydofus3.generated.pydantic.Ankama.Animations.Animator2D import Animator2D
from pydofus3.generated.pydantic.gsd import gsd
from pydofus3.not_generated.base import MyBaseModel

class BufferRequest(MyBaseModel):
	target: Animator2D
	animation: gsd
	id: int

