from pydofus3.generated.pydantic.gsh import gsh
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
	instance: gsh

	class gsd(FlagBaseModel):
		dtrt : Annotated[bool,0]
		dtru : Annotated[bool,1]
		dtrv : Annotated[bool,2]
		dtrw : Annotated[bool,4]
		dtrx : Annotated[bool,8]
		dtry : Annotated[bool,16]
		dtrz : Annotated[bool,32]
		dtsa : Annotated[bool,64]
		dtsb : Annotated[bool,128]

	class gse(OpenAPIIntEnum):
		dtsc = 0
		dtsd = 1
		dtse = 2
		dtsf = 4
		dtsg = 8
		dtsh = 16
		dtsi = 32
		dtsj = 64
		dtsk = 128

	class gsf(FlagBaseModel):
		dtsl : Annotated[bool,0]
		dtsm : Annotated[bool,1]
		dtsn : Annotated[bool,2]
		dtso : Annotated[bool,4]

	class gsg(OpenAPIIntEnum):
		dtsp = 0
		dtsq = 1
		dtsr = 2
		dtss = 3
		dtst = 4
		dtsu = 5
		dtsv = 6
		dtsw = 7
		dtsx = 8
		dtsy = 9
		dtsz = 10
		dtta = 11
		dttb = 12
		dttc = 13
		dttd = 14
		dtte = 15

