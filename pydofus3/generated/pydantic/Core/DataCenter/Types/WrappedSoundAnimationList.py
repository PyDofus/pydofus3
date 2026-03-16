from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Sound.SoundAnimationData import SoundAnimationData
from pydofus3.not_generated.base import MyBaseModel

class WrappedSoundAnimationList(MyBaseModel):
	values: list[SoundAnimationData]

