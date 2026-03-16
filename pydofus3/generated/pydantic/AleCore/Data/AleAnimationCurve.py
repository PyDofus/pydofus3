from pydofus3.generated.pydantic.AleCore.Data.AleKeyframe import AleKeyframe
from pydofus3.not_generated.base import MyBaseModel

class AleAnimationCurve(MyBaseModel):
	keys: list[AleKeyframe]

