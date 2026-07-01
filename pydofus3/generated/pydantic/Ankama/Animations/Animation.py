from pydofus3.generated.pydantic.hbm import hbm
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
	instance: hbm

	class hbi(FlagBaseModel):
		eatv : Annotated[bool,0]
		eatw : Annotated[bool,1]
		eatx : Annotated[bool,2]
		eaty : Annotated[bool,4]
		eatz : Annotated[bool,8]
		eaua : Annotated[bool,16]
		eaub : Annotated[bool,32]
		eauc : Annotated[bool,64]
		eaud : Annotated[bool,128]

	class hbj(OpenAPIIntEnum):
		eaue = 0
		eauf = 1
		eaug = 2
		eauh = 4
		eaui = 8
		eauj = 16
		eauk = 32
		eaul = 64
		eaum = 128

	class hbk(FlagBaseModel):
		eaun : Annotated[bool,0]
		eauo : Annotated[bool,1]
		eaup : Annotated[bool,2]
		eauq : Annotated[bool,4]

	class hbl(OpenAPIIntEnum):
		eaur = 0
		eaus = 1
		eaut = 2
		eauu = 3
		eauv = 4
		eauw = 5
		eaux = 6
		eauy = 7
		eauz = 8
		eava = 9
		eavb = 10
		eavc = 11
		eavd = 12
		eave = 13
		eavf = 14
		eavg = 15

