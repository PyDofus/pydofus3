from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.IStagingEffect import IStagingEffect

class ChangePlaylistStagingEffect(IStagingEffect):
	musicPlaylist: str
	ambiantPlaylist: str

