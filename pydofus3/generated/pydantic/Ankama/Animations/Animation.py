from pydofus3.generated.pydantic.hbg import hbg
from pydofus3.not_generated.base import FlagBaseModel
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from pydofus3.not_generated.unity import Rect
from typing import Annotated

class Animation(MyBaseModel):
	name: str
	boneId: str
	bounds: Rect
	instance: hbg

	class hbc(FlagBaseModel):
		ebcx : Annotated[bool,0]
		ebcy : Annotated[bool,1]
		ebcz : Annotated[bool,2]
		ebda : Annotated[bool,4]
		ebdb : Annotated[bool,8]
		ebdc : Annotated[bool,16]
		ebdd : Annotated[bool,32]
		ebde : Annotated[bool,64]
		ebdf : Annotated[bool,128]

	class hbd(OpenAPIIntEnum):
		ebdg = 0
		ebdh = 1
		ebdi = 2
		ebdj = 4
		ebdk = 8
		ebdl = 16
		ebdm = 32
		ebdn = 64
		ebdo = 128

	class hbe(FlagBaseModel):
		ebdp : Annotated[bool,0]
		ebdq : Annotated[bool,1]
		ebdr : Annotated[bool,2]
		ebds : Annotated[bool,4]

	class hbf(OpenAPIIntEnum):
		ebdt = 0
		ebdu = 1
		ebdv = 2
		ebdw = 3
		ebdx = 4
		ebdy = 5
		ebdz = 6
		ebea = 7
		ebeb = 8
		ebec = 9
		ebed = 10
		ebee = 11
		ebef = 12
		ebeg = 13
		ebeh = 14
		ebei = 15

