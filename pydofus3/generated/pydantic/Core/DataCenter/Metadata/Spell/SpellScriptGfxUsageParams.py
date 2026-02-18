from pydantic import Field
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.GfxAnimationEndPolicy import GfxAnimationEndPolicy
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.ProjectileDirectionType import ProjectileDirectionType
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.ProjectileStrata import ProjectileStrata
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.SpellScriptGfxType import SpellScriptGfxType
from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import float_nan
from typing import Union, Annotated

class SpellScriptGfxUsageParams(MyBaseModel):
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

