from pydantic import Field
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.ShaderConstants import ShaderConstants
from pydofus3.generated.pydantic.Ankama.Animations.Sources.Rendering.CustomPasses.AdjustmentsPassSettings import AdjustmentsPassSettings
from pydofus3.generated.pydantic.Ankama.Animations.Sources.Rendering.CustomPasses.ConvolutionRenderPassSettings import ConvolutionRenderPassSettings
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import Color
from pydofus3.not_generated.unity import Material
from typing import Annotated, Union

class OutlinePrepassSettings(MyBaseModel):
	renderingLayerMask: Annotated[Union[ShaderConstants.RenderingLayerIDs, int], Field(union_mode='left_to_right')]
	shaderOutlinedInWhitePassIndex: int
	outlineColor: Color
	alphaClip: float_nan
	testDiff: Annotated[Union[ShaderConstants.OutlineTestDiff, int], Field(union_mode='left_to_right')]
	width: float_nan
	shouldBlur: bool
	blurSettings: ConvolutionRenderPassSettings
	shouldAdjust: bool
	adjustmentsSettings: AdjustmentsPassSettings
	useBlendMat: bool
	blendMat: Material

