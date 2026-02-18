from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Seasons.SeasonData import SeasonData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar


class ServerSeasonData(SeasonData, D2oData):
	bundle_name: ClassVar[str] = "serverseasonsdataroot"

	pass

