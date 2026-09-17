from pydofus3.generated.pydantic.Ankama.Animations.Animation import Animation
from pydofus3.generated.pydantic.Ankama.Animations.AnimationLabel import AnimationLabel
from pydofus3.not_generated.base import MyBaseModel

class hbk(MyBaseModel):
	eamr: str
	eams: int
	eamt: int
	eamu: int
	eamv: Animation.hbg
	eamw: list[int]
	eamx: list[int]
	eamy: list[AnimationLabel]
	eamz: int

