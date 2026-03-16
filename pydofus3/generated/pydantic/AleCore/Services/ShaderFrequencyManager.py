from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Services.IShaderTimeData import IShaderTimeData
from pydofus3.generated.pydantic.AleCore.Services.ShaderFrequencyTypeEnum import ShaderFrequencyTypeEnum
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import Material
from typing import Annotated, Union

class ShaderFrequencyManager(MyBaseModel):
	globalWindPower: float_nan
	loadedMapTimeSyncOffset: float_nan
	shaderTimeDataDictionary: dict[Material, dict[Annotated[Union[ShaderFrequencyTypeEnum, int], Field(union_mode='left_to_right')], IShaderTimeData]]

