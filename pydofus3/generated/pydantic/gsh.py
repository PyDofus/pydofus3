from pydofus3.generated.pydantic.Ankama.Animations.Animation import Animation
from pydofus3.generated.pydantic.Ankama.Animations.AnimationLabel import AnimationLabel
from pydofus3.not_generated.base import MyBaseModel

class gsh(MyBaseModel):
	dttg: str
	dtth: int
	dtti: int
	dttj: int
	dttk: Animation.gsd
	dttl: list[int]
	dttm: list[int]
	dttn: list[AnimationLabel]
	dtto: int

