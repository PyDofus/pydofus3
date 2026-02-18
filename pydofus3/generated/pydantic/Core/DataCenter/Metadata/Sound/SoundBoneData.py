from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Sound.SoundAnimationData import SoundAnimationData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import SerializableDictionary

class SoundBoneData(D2oData):
	bundle_name: ClassVar[str] = "soundbonesdataroot"

	animSounds: 'SoundBoneData.SoundBonesDictionary'
	class SoundBonesDictionary(SerializableDictionary[str, SoundAnimationData]):
		pass

