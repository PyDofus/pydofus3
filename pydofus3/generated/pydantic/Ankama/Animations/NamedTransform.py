from pydofus3.generated.pydantic.Ankama.Animations.Animator2D import Animator2D
from pydofus3.not_generated.base import MyBaseModel

class NamedTransform(MyBaseModel):
	materialCount: int
	animator: Animator2D

