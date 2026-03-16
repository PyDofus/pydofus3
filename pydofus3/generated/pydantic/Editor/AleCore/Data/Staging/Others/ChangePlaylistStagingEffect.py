from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class ChangePlaylistStagingEffect(MyBaseModel):
	TYPE: ClassVar[str] = "ChangePlaylist"
	musicPlaylist: str
	ambiantPlaylist: str

