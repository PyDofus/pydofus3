from pydofus3.generated.pydantic.AleCore.Data.AleConstantOrCurve import AleConstantOrCurve
from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class PlayFmodEventStagingEffect(MyBaseModel):
	TYPE: ClassVar[str] = "PlayFmodEvent"
	fmodEvent: str
	xPosition: AleConstantOrCurve
	yPosition: AleConstantOrCurve

