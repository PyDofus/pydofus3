from pydofus3.generated.pydantic.hau import hau
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
	instance: hau

	class haq(FlagBaseModel):
		ebbj : Annotated[bool,0]
		ebbk : Annotated[bool,1]
		ebbl : Annotated[bool,2]
		ebbm : Annotated[bool,4]
		ebbn : Annotated[bool,8]
		ebbo : Annotated[bool,16]
		ebbp : Annotated[bool,32]
		ebbq : Annotated[bool,64]
		ebbr : Annotated[bool,128]

	class har(OpenAPIIntEnum):
		ebbs = 0
		ebbt = 1
		ebbu = 2
		ebbv = 4
		ebbw = 8
		ebbx = 16
		ebby = 32
		ebbz = 64
		ebca = 128

	class has(FlagBaseModel):
		ebcb : Annotated[bool,0]
		ebcc : Annotated[bool,1]
		ebcd : Annotated[bool,2]
		ebce : Annotated[bool,4]

	class hat(OpenAPIIntEnum):
		ebcf = 0
		ebcg = 1
		ebch = 2
		ebci = 3
		ebcj = 4
		ebck = 5
		ebcl = 6
		ebcm = 7
		ebcn = 8
		ebco = 9
		ebcp = 10
		ebcq = 11
		ebcr = 12
		ebcs = 13
		ebct = 14
		ebcu = 15

