from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class WorldPoint(MyBaseModel):
	WorldIdMax: ClassVar[int] = 8192
	MapCoordsMax: ClassVar[int] = 512

