from pydantic import Field
from pydofus3.generated.pydantic.Ankama.Animations.Sources.Rendering.CustomPasses.CustomRenderObjectsPassSettings import CustomRenderObjectsPassSettings
from pydofus3.generated.pydantic.hcl import hcl
from pydofus3.generated.pydantic.hct import hct
from pydofus3.not_generated.unity import RenderPassEvent
from pydofus3.not_generated.unity import ScriptableRendererFeature
from typing import Annotated, Union

class CustomRenderObjectsFeature(ScriptableRendererFeature):
	renderPassEvent: RenderPassEvent
	renderFeatureType: Annotated[Union[hct.hcs, int], Field(union_mode='left_to_right')]
	renderObjectPass: hcl
	renderObjectsSettings: CustomRenderObjectsPassSettings

