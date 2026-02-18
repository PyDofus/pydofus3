from pydofus3.generated.pydantic.AleCore.Data.AleVector3 import AleVector3
from pydofus3.not_generated.base import MyBaseModel


class TransformParameters(MyBaseModel):
	pos: AleVector3
	rot: AleVector3
	scale: AleVector3

