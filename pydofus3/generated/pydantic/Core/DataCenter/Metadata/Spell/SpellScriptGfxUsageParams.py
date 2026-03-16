from pydantic import Field
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.GfxAnimationEndPolicy import GfxAnimationEndPolicy
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.ProjectileDirectionType import ProjectileDirectionType
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.ProjectileStrata import ProjectileStrata
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.SpellScriptGfxType import SpellScriptGfxType
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from typing import Annotated, Union
from typing import ClassVar

class SpellScriptGfxUsageParams(MyBaseModel):
	DefaultType: ClassVar[Annotated[Union[SpellScriptGfxType, int], Field(union_mode='left_to_right')]] = Annotated[Union[SpellScriptGfxType, int], Field(union_mode='left_to_right')].Unknown
	DefaultGfxId: ClassVar[int] = 0
	DefaultOffsetX: ClassVar[int] = 0
	DefaultOffsetY: ClassVar[int] = 0
	DefaultScaleX: ClassVar[float_nan] = 1
	DefaultScaleY: ClassVar[float_nan] = 1
	DefaultRotation: ClassVar[int] = 0
	DefaultDirectionType: ClassVar[Annotated[Union[ProjectileDirectionType, int], Field(union_mode='left_to_right')]] = Annotated[Union[ProjectileDirectionType, int], Field(union_mode='left_to_right')].Normal
	DefaultIsOriented: ClassVar[bool] = False
	DefaultSpeed: ClassVar[int] = 100
	DefaultCurvature: ClassVar[float_nan] = 5
	DefaultIsCurveFollowed: ClassVar[bool] = True
	DefaultMinScale: ClassVar[int] = 0
	DefaultMaxScale: ClassVar[int] = 0
	DefaultCasterAnimation: ClassVar[str] = "AnimAttaque4"
	DefaultIsCasterOriented: ClassVar[bool] = True
	DefaultStrata: ClassVar[Annotated[Union[ProjectileStrata, int], Field(union_mode='left_to_right')]] = Annotated[Union[ProjectileStrata, int], Field(union_mode='left_to_right')].Front
	DefaultFrameOffset: ClassVar[int] = 0
	DefaultGfxAnimationEndPolicy: ClassVar[Annotated[Union[GfxAnimationEndPolicy, int], Field(union_mode='left_to_right')]] = Annotated[Union[GfxAnimationEndPolicy, int], Field(union_mode='left_to_right')].SameAsSequence
	DefaultStagingId: ClassVar[int] = 0
	DefaultStagingIntensity: ClassVar[float_nan] = 1
	DefaultStagingProgress: ClassVar[float_nan] = 0
	DefaultStagingIsBlocking: ClassVar[bool] = False
	type: Annotated[Union[SpellScriptGfxType, int], Field(union_mode='left_to_right')]
	gfxId: int
	offsetX: int
	offsetY: int
	scaleX: float_nan
	scaleY: float_nan
	rotation: int
	directionType: Annotated[Union[ProjectileDirectionType, int], Field(union_mode='left_to_right')]
	isOriented: bool
	speed: int
	curvature: float_nan
	isCurveFollowed: bool
	isEntireSpellZone: bool
	isContainedInSpellZone: bool
	minScale: int
	maxScale: int
	isFromCaster: bool
	isToTarget: bool
	casterAnimation: str
	isCasterOriented: bool
	strata: Annotated[Union[ProjectileStrata, int], Field(union_mode='left_to_right')]
	frameOffset: int
	gfxAnimationEndPolicy: Annotated[Union[GfxAnimationEndPolicy, int], Field(union_mode='left_to_right')]
	stagingId: int
	stagingIntensity: float_nan
	stagingProgress: float_nan
	stagingIsBlocking: bool

