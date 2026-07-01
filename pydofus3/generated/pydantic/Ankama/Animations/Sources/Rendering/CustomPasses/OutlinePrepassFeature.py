from pydantic import Field
from pydofus3.generated.pydantic.Ankama.Animations.Sources.Rendering.CustomPasses.OutlinePrepassSettings import OutlinePrepassSettings
from pydofus3.generated.pydantic.hck import hck
from pydofus3.not_generated.unity import RenderPassEvent
from pydofus3.not_generated.unity import ScriptableRendererFeature
from typing import Annotated, Union

class OutlinePrepassFeature(ScriptableRendererFeature):
	renderPassEvent: RenderPassEvent
	renderFeatureType: Annotated[Union[hck.hcj, int], Field(union_mode='left_to_right')]
	outlineInTexSettings: OutlinePrepassSettings

