from pydofus3.generated.pydantic.gsd import gsd
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
	instance: gsd

	class grz(FlagBaseModel):
		dtic : Annotated[bool,0]
		dtid : Annotated[bool,1]
		dtie : Annotated[bool,2]
		dtif : Annotated[bool,4]
		dtig : Annotated[bool,8]
		dtih : Annotated[bool,16]
		dtii : Annotated[bool,32]
		dtij : Annotated[bool,64]
		dtik : Annotated[bool,128]

	class gsa(OpenAPIIntEnum):
		dtil = 0
		dtim = 1
		dtin = 2
		dtio = 4
		dtip = 8
		dtiq = 16
		dtir = 32
		dtis = 64
		dtit = 128

	class gsb(FlagBaseModel):
		dtiu : Annotated[bool,0]
		dtiv : Annotated[bool,1]
		dtiw : Annotated[bool,2]
		dtix : Annotated[bool,4]

	class gsc(OpenAPIIntEnum):
		dtiy = 0
		dtiz = 1
		dtja = 2
		dtjb = 3
		dtjc = 4
		dtjd = 5
		dtje = 6
		dtjf = 7
		dtjg = 8
		dtjh = 9
		dtji = 10
		dtjj = 11
		dtjk = 12
		dtjl = 13
		dtjm = 14
		dtjn = 15

