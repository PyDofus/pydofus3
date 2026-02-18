from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Social.SocialTagData import SocialTagData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar


class GuildTagData(SocialTagData, D2oData):
	bundle_name: ClassVar[str] = "guildtagsdataroot"

	pass

