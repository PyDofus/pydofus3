from pydantic import Field
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.ShaderConstants import ShaderConstants
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import RenderPassEvent
from pydofus3.not_generated.unity import ScriptableRendererFeature
from typing import Annotated, Union

class RefractionRendererFeature(ScriptableRendererFeature):
	_refractionPassSettings: RefractionPassSettings

	class RefractionPassSettings(MyBaseModel):
		renderPassEvent: RenderPassEvent
		renderingLayerMask: Annotated[Union[ShaderConstants.RenderingLayerIDs, int], Field(union_mode='left_to_right')]
		shaderPassIndex: int

	class gtg(MyBaseModel):
		class gte(MyBaseModel):
			pass

		class gtf(MyBaseModel):
			pass

