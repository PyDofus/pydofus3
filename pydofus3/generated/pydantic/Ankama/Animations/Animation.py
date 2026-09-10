from pydofus3.generated.pydantic.hbz import hbz
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
	instance: hbz

	class hbv(FlagBaseModel):
		eavv : Annotated[bool,0]
		eavw : Annotated[bool,1]
		eavx : Annotated[bool,2]
		eavy : Annotated[bool,4]
		eavz : Annotated[bool,8]
		eawa : Annotated[bool,16]
		eawb : Annotated[bool,32]
		eawc : Annotated[bool,64]
		eawd : Annotated[bool,128]

	class hbw(OpenAPIIntEnum):
		eawe = 0
		eawf = 1
		eawg = 2
		eawh = 4
		eawi = 8
		eawj = 16
		eawk = 32
		eawl = 64
		eawm = 128

	class hbx(FlagBaseModel):
		eawn : Annotated[bool,0]
		eawo : Annotated[bool,1]
		eawp : Annotated[bool,2]
		eawq : Annotated[bool,4]

	class hby(OpenAPIIntEnum):
		eawr = 0
		eaws = 1
		eawt = 2
		eawu = 3
		eawv = 4
		eaww = 5
		eawx = 6
		eawy = 7
		eawz = 8
		eaxa = 9
		eaxb = 10
		eaxc = 11
		eaxd = 12
		eaxe = 13
		eaxf = 14
		eaxg = 15

