from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Utils.OutlineTestDiff import OutlineTestDiff
from pydofus3.generated.pydantic.AleCore.Utils.OutlineType import OutlineType
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from typing import Annotated, Union

class ShaderOutlineParameters(MyBaseModel):
	type: Annotated[Union[OutlineType, int], Field(union_mode='left_to_right')]
	testDiff: Annotated[Union[OutlineTestDiff, int], Field(union_mode='left_to_right')]
	alphaClip: float_nan
	color: AleColor

