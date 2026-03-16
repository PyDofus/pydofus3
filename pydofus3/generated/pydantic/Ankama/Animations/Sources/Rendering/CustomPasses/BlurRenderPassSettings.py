from pydofus3.generated.pydantic.Ankama.Animations.Sources.Rendering.CustomPasses.ConvolutionRenderPassSettings import ConvolutionRenderPassSettings
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import Vector2

class BlurRenderPassSettings(MyBaseModel):
	shouldBlurOnce: bool
	firstBlurSettings: ConvolutionRenderPassSettings
	shouldBlurTwice: bool
	secondBlurSettings: ConvolutionRenderPassSettings
	remapIn: Vector2

