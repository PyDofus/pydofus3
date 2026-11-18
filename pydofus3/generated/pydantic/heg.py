from pydofus3.generated.pydantic.hef import hef
from pydofus3.not_generated.base import MyBaseModel

class heg(MyBaseModel):
	ecps: int
	ecpt: hef
	ecpu: bool
	ecpv: bool

