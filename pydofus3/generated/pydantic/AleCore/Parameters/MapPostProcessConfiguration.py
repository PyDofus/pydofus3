from pydofus3.generated.pydantic.AleCore.Parameters.PostProcess.IPostProcessParameters import IPostProcessParameters
from pydofus3.not_generated.base import MyBaseModel


class MapPostProcessConfiguration(MyBaseModel):
	postProcessParameters: list[IPostProcessParameters]

