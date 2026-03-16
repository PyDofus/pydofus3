from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class StopLocalizedFmodEventsStagingEffect(MyBaseModel):
	TYPE: ClassVar[str] = "StopLocalizedSound"
	fmodEvent: str

