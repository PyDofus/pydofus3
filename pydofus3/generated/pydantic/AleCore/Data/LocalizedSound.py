from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.not_generated.base import MyBaseModel


class LocalizedSound(MyBaseModel):
	audioEvent: str
	position: AleVector2

