from pydofus3.generated.pydantic.Ankama.Animations.Animation import Animation
from pydofus3.generated.pydantic.Ankama.Animations.AnimationLabel import AnimationLabel
from pydofus3.not_generated.base import MyBaseModel

class hbx(MyBaseModel):
	eavi: str
	eavj: int
	eavk: int
	eavl: int
	eavm: Animation.hbt
	eavn: list[int]
	eavo: list[int]
	eavp: list[AnimationLabel]
	eavq: int

