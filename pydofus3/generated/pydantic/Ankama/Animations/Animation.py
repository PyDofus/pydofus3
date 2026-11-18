from pydofus3.generated.pydantic.hdw import hdw
from pydofus3.not_generated.base import FlagBaseModel
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from pydofus3.not_generated.unity import Rect
from typing import Annotated

class Animation(MyBaseModel):
	name: str
	boneId: str
	bounds: Rect
	instance: hdw

	class hds(FlagBaseModel):
		eclj : Annotated[bool,0]
		eclk : Annotated[bool,1]
		ecll : Annotated[bool,2]
		eclm : Annotated[bool,4]
		ecln : Annotated[bool,8]
		eclo : Annotated[bool,16]
		eclp : Annotated[bool,32]
		eclq : Annotated[bool,64]
		eclr : Annotated[bool,128]

	class hdt(OpenAPIIntEnum):
		ecls = 0
		eclt = 1
		eclu = 2
		eclv = 4
		eclw = 8
		eclx = 16
		ecly = 32
		eclz = 64
		ecma = 128

	class hdu(FlagBaseModel):
		ecmb : Annotated[bool,0]
		ecmc : Annotated[bool,1]
		ecmd : Annotated[bool,2]
		ecme : Annotated[bool,4]

	class hdv(OpenAPIIntEnum):
		ecmf = 0
		ecmg = 1
		ecmh = 2
		ecmi = 3
		ecmj = 4
		ecmk = 5
		ecml = 6
		ecmm = 7
		ecmn = 8
		ecmo = 9
		ecmp = 10
		ecmq = 11
		ecmr = 12
		ecms = 13
		ecmt = 14
		ecmu = 15

