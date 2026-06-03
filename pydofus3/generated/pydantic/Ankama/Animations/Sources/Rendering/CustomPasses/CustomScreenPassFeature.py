from pydantic import Field
from pydofus3.generated.pydantic.Ankama.Animations.Sources.Rendering.CustomPasses.CustomScreenPassSettings import CustomScreenPassSettings
from pydofus3.generated.pydantic.hbs import hbs
from pydofus3.not_generated.unity import RenderPassEvent
from pydofus3.not_generated.unity import ScriptableRendererFeature
from typing import Annotated, Union

class CustomScreenPassFeature(ScriptableRendererFeature):
	renderPassEvent: RenderPassEvent
	renderFeatureType: Annotated[Union[hbs.hbr, int], Field(union_mode='left_to_right')]
	customScreenPassSettings: CustomScreenPassSettings

