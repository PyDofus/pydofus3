from pydantic import Field
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.ShaderConstants import ShaderConstants
from pydofus3.generated.pydantic.hbu import hbu
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import RenderPassEvent
from pydofus3.not_generated.unity import ScriptableRendererFeature
from typing import Annotated, Union

class RefractionRendererFeature(ScriptableRendererFeature):
	_refractionPassSettings: RefractionPassSettings

	class RefractionPassSettings(MyBaseModel):
		renderPassEvent: RenderPassEvent
		renderFeatureType: Annotated[Union[hbu.hbt, int], Field(union_mode='left_to_right')]
		renderingLayerMask: Annotated[Union[ShaderConstants.RenderingLayerIDs, int], Field(union_mode='left_to_right')]
		shaderPassIndex: int

	class hbs(MyBaseModel):
		class hbq(MyBaseModel):
			pass

		class hbr(MyBaseModel):
			pass

