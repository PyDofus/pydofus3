from pydantic import Field
from pydofus3.generated.pydantic.Ankama.Animations.Sources.Rendering.CustomPasses.CustomScreenPassSettings import CustomScreenPassSettings
from pydofus3.generated.pydantic.hbu import hbu
from pydofus3.not_generated.unity import RenderPassEvent
from pydofus3.not_generated.unity import ScriptableRendererFeature
from typing import Annotated, Union

class CustomScreenPassFeature(ScriptableRendererFeature):
	renderPassEvent: RenderPassEvent
	renderFeatureType: Annotated[Union[hbu.hbt, int], Field(union_mode='left_to_right')]
	customScreenPassSettings: CustomScreenPassSettings

