from pydofus3.generated.pydantic.hbk import hbk
from pydofus3.not_generated.base import FlagBaseModel
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from pydofus3.not_generated.unity import Rect
from typing import Annotated

class Animation(MyBaseModel):
	name: str
	boneId: str
	dataBytes: list[int]
	bounds: Rect
	instance: hbk

	class hbg(FlagBaseModel):
		eale : Annotated[bool,0]
		ealf : Annotated[bool,1]
		ealg : Annotated[bool,2]
		ealh : Annotated[bool,4]
		eali : Annotated[bool,8]
		ealj : Annotated[bool,16]
		ealk : Annotated[bool,32]
		eall : Annotated[bool,64]
		ealm : Annotated[bool,128]

	class hbh(OpenAPIIntEnum):
		ealn = 0
		ealo = 1
		ealp = 2
		ealq = 4
		ealr = 8
		eals = 16
		ealt = 32
		ealu = 64
		ealv = 128

	class hbi(FlagBaseModel):
		ealw : Annotated[bool,0]
		ealx : Annotated[bool,1]
		ealy : Annotated[bool,2]
		ealz : Annotated[bool,4]

	class hbj(OpenAPIIntEnum):
		eama = 0
		eamb = 1
		eamc = 2
		eamd = 3
		eame = 4
		eamf = 5
		eamg = 6
		eamh = 7
		eami = 8
		eamj = 9
		eamk = 10
		eaml = 11
		eamm = 12
		eamn = 13
		eamo = 14
		eamp = 15

