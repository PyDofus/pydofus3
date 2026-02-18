from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Social.SocialRightData import SocialRightData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar


class AllianceRightData(SocialRightData, D2oData):
	bundle_name: ClassVar[str] = "alliancerightsdataroot"

	pass

