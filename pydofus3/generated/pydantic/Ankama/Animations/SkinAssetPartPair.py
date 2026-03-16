from pydofus3.generated.pydantic.Ankama.Animations.SkinAsset import SkinAsset
from pydofus3.generated.pydantic.Ankama.Animations.SkinAssetPart import SkinAssetPart
from pydofus3.not_generated.base import MyBaseModel

class SkinAssetPartPair(MyBaseModel):
	asset: SkinAsset
	part: SkinAssetPart

