from pydofus3.generated.pydantic.Ankama.Animations.Animation import Animation
from pydofus3.generated.pydantic.Ankama.Animations.AnimationLabel import AnimationLabel
from pydofus3.not_generated.base import MyBaseModel

class hdw(MyBaseModel):
	ecmw: str
	ecmx: int
	ecmy: int
	ecmz: int
	ecna: Animation.hds
	ecnb: list[int]
	ecnc: list[int]
	ecnd: list[AnimationLabel]
	ecne: int

