from pydofus3.generated.pydantic.gsk import gsk
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
	instance: gsk

	class gsg(FlagBaseModel):
		dtwo : Annotated[bool,0]
		dtwp : Annotated[bool,1]
		dtwq : Annotated[bool,2]
		dtwr : Annotated[bool,4]
		dtws : Annotated[bool,8]
		dtwt : Annotated[bool,16]
		dtwu : Annotated[bool,32]
		dtwv : Annotated[bool,64]
		dtww : Annotated[bool,128]

	class gsh(OpenAPIIntEnum):
		dtwx = 0
		dtwy = 1
		dtwz = 2
		dtxa = 4
		dtxb = 8
		dtxc = 16
		dtxd = 32
		dtxe = 64
		dtxf = 128

	class gsi(FlagBaseModel):
		dtxg : Annotated[bool,0]
		dtxh : Annotated[bool,1]
		dtxi : Annotated[bool,2]
		dtxj : Annotated[bool,4]

	class gsj(OpenAPIIntEnum):
		dtxk = 0
		dtxl = 1
		dtxm = 2
		dtxn = 3
		dtxo = 4
		dtxp = 5
		dtxq = 6
		dtxr = 7
		dtxs = 8
		dtxt = 9
		dtxu = 10
		dtxv = 11
		dtxw = 12
		dtxx = 13
		dtxy = 14
		dtxz = 15

