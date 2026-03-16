from pydofus3.generated.pydantic.Ankama.Animations.Animation import Animation
from pydofus3.generated.pydantic.Ankama.Animations.MaskableNode import MaskableNode
from pydofus3.generated.pydantic.Ankama.Animations.SkinAsset import SkinAsset
from pydofus3.generated.pydantic.Ankama.Animations.SkinAssetPartPair import SkinAssetPartPair
from pydofus3.not_generated.base import MyBaseModel

class AnimatedObjectDefinition(MyBaseModel):
	defaultAnimationName: str
	defaultAnimationLoops: bool
	defaultFrameRate: int
	maxNodeCount: int
	exposedNodeNames: list[str]
	maskableNodes: list[MaskableNode]
	boneAsset: SkinAsset
	graphics: list[SkinAssetPartPair]
	animations: list[Animation]
	blankAnimations: list[str]

