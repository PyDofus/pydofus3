from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class SetFmodSnapshotStagingEffect(MyBaseModel):
	TYPE: ClassVar[str] = "SetFmodSnapshot"
	fmodSnapShot: str

