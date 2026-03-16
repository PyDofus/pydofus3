from pydofus3.generated.pydantic.Ankama.Animations.DisplayListEntry import DisplayListEntry
from pydofus3.generated.pydantic.Ankama.Animations.SkinChunk import SkinChunk
from pydofus3.not_generated.base import MyBaseModel

class SkinAssetPart(MyBaseModel):
	name: str
	DisplayListEntry: list[DisplayListEntry]
	skinChunks: list[SkinChunk]

