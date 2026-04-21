from pydofus3.generated.pydantic.Ankama.Animations.Rendering.Animator2DRenderer import Animator2DRenderer
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.EvaluatedAnimationFrame import EvaluatedAnimationFrame
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.MaterialDescriptor import MaterialDescriptor
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.RenderState import RenderState
from pydofus3.generated.pydantic.gsp import gsp
from pydofus3.not_generated.base import MyBaseModel
from typing import Optional

class Animator2DCustomisableRenderer(Animator2DRenderer):
	class ShaderID(MyBaseModel):
		pass

	class MaterialOffsetForSymbol(MyBaseModel):
		pass

	class DrawContext(MyBaseModel):
		renderState: RenderState
		evaluatedAnimationFrame: EvaluatedAnimationFrame
		lastRenderedIndex: int
		maskDepth: int
		currentMaterialIdentifier: Optional[MaterialDescriptor]
		namedTransforms: gsp
		isMaskNode: bool
		renderer: Animator2DCustomisableRenderer

