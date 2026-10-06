from pydofus3.generated.pydantic.Ankama.Animations.Animation import Animation
from pydofus3.generated.pydantic.Ankama.Animations.AnimationLabel import AnimationLabel
from pydofus3.not_generated.base import MyBaseModel

class hbg(MyBaseModel):
	ebek: str
	ebel: int
	ebem: int
	eben: int
	ebeo: Animation.hbc
	ebep: list[int]
	ebeq: list[int]
	eber: list[AnimationLabel]
	ebes: int

