from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Social.SocialRightData import SocialRightData
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.i18n import i18n

class SocialRightGroupData(MyBaseModel):
	id: int
	nameId: i18n
	order: int
	rights: list[SocialRightData]

