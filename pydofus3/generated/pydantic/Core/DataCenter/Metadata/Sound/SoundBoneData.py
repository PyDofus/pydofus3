from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Sound.SoundAnimationData import SoundAnimationData
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import SerializableDictionary
from typing import ClassVar

class SoundBoneData(D2oData):
	bundle_name: ClassVar[str] = "soundbonesdataroot"

	animSounds: SoundBonesDictionary

	class SoundBonesDictionary(SerializableDictionary[str, SoundAnimationData]):
		pass

