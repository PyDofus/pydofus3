from pydofus3.generated.pydantic.haw import haw
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
	instance: haw

	class has(FlagBaseModel):
		easf : Annotated[bool,0]
		easg : Annotated[bool,1]
		eash : Annotated[bool,2]
		easi : Annotated[bool,4]
		easj : Annotated[bool,8]
		eask : Annotated[bool,16]
		easl : Annotated[bool,32]
		easm : Annotated[bool,64]
		easn : Annotated[bool,128]

	class hat(OpenAPIIntEnum):
		easo = 0
		easp = 1
		easq = 2
		easr = 4
		eass = 8
		east = 16
		easu = 32
		easv = 64
		easw = 128

	class hau(FlagBaseModel):
		easx : Annotated[bool,0]
		easy : Annotated[bool,1]
		easz : Annotated[bool,2]
		eata : Annotated[bool,4]

	class hav(OpenAPIIntEnum):
		eatb = 0
		eatc = 1
		eatd = 2
		eate = 3
		eatf = 4
		eatg = 5
		eath = 6
		eati = 7
		eatj = 8
		eatk = 9
		eatl = 10
		eatm = 11
		eatn = 12
		eato = 13
		eatp = 14
		eatq = 15

