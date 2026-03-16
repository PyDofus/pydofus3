from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.generated.pydantic.AleCore.Data.AleVector4 import AleVector4
from pydofus3.generated.pydantic.AleCore.Parameters.Shader.ShaderWindParentParameters import ShaderWindParentParameters
from pydofus3.generated.pydantic.AleCore.Utils.WindSensitiveTypeTest import WindSensitiveTypeTest
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from typing import Annotated, Union
from typing import ClassVar

class ShaderWindParameters(MyBaseModel):
	TYPE: ClassVar[str] = "Wind"
	isWindSensitive: Annotated[Union[WindSensitiveTypeTest, int], Field(union_mode='left_to_right')]
	bendCenter: AleVector2
	worldSpaceBendCenter: AleVector4
	bendStart: AleVector2
	worldSpaceBendStart: AleVector4
	bendAxe: AleVector2
	bendAxeMultiplier: float_nan
	flexibility: float_nan
	shouldSwing: bool
	windSwingNoiseSpeedCoef: float_nan
	windSwingNoiseAmplitude: float_nan
	parentParameters: list[ShaderWindParentParameters]

