from pydofus3.generated.pydantic.hbv import hbv
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
	instance: hbv

	class hbr(FlagBaseModel):
		ebde : Annotated[bool,0]
		ebdf : Annotated[bool,1]
		ebdg : Annotated[bool,2]
		ebdh : Annotated[bool,4]
		ebdi : Annotated[bool,8]
		ebdj : Annotated[bool,16]
		ebdk : Annotated[bool,32]
		ebdl : Annotated[bool,64]
		ebdm : Annotated[bool,128]

	class hbs(OpenAPIIntEnum):
		ebdn = 0
		ebdo = 1
		ebdp = 2
		ebdq = 4
		ebdr = 8
		ebds = 16
		ebdt = 32
		ebdu = 64
		ebdv = 128

	class hbt(FlagBaseModel):
		ebdw : Annotated[bool,0]
		ebdx : Annotated[bool,1]
		ebdy : Annotated[bool,2]
		ebdz : Annotated[bool,4]

	class hbu(OpenAPIIntEnum):
		ebea = 0
		ebeb = 1
		ebec = 2
		ebed = 3
		ebee = 4
		ebef = 5
		ebeg = 6
		ebeh = 7
		ebei = 8
		ebej = 9
		ebek = 10
		ebel = 11
		ebem = 12
		eben = 13
		ebeo = 14
		ebep = 15

