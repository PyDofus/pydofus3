from pydofus3.generated.pydantic.AleCore.Data.Sound.FmodParameterValue import FmodParameterValue
from pydofus3.generated.pydantic.AleCore.Data.Sound.Playlist import Playlist
from pydofus3.not_generated.base import MyBaseModel

class PlaylistSet(MyBaseModel):
	musicPlaylist: Playlist
	ambiantPlaylist: Playlist
	bossFightPlaylist: Playlist
	snapshot: str
	fmodParameterValues: list[FmodParameterValue]

