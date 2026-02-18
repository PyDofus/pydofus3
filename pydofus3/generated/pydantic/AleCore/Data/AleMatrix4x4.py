from pydofus3.generated.pydantic.AleCore.Data.AleVector4 import AleVector4
from pydofus3.not_generated.base import MyBaseModel


class AleMatrix4x4(MyBaseModel):
	column0: AleVector4
	column1: AleVector4
	column2: AleVector4
	column3: AleVector4

