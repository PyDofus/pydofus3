from pydofus3.generated.pydantic.Ankama.Animations.Animation import Animation
from pydofus3.generated.pydantic.Ankama.Animations.AnimationLabel import AnimationLabel
from pydofus3.not_generated.base import MyBaseModel

class gsd(MyBaseModel):
	dtjp: str
	dtjq: int
	dtjr: int
	dtjs: int
	dtjt: Animation.grz
	dtju: list[int]
	dtjv: list[int]
	dtjw: list[AnimationLabel]
	dtjx: int

