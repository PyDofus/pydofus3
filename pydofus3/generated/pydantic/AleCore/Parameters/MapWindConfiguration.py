from pydofus3.generated.pydantic.AleCore.Parameters.WindParameters import WindParameters
from pydofus3.not_generated.base import MyBaseModel


class MapWindConfiguration(MyBaseModel):
	windParameters: WindParameters

