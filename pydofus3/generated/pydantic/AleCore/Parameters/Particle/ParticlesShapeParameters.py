from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleConstantOrCurve import AleConstantOrCurve
from pydofus3.generated.pydantic.AleCore.Data.AleParticleSystemEmitFromBox import AleParticleSystemEmitFromBox
from pydofus3.generated.pydantic.AleCore.Data.AleParticleSystemEmitFromCone import AleParticleSystemEmitFromCone
from pydofus3.generated.pydantic.AleCore.Data.AleParticleSystemShapeMultiModeValue import AleParticleSystemShapeMultiModeValue
from pydofus3.generated.pydantic.AleCore.Data.AleParticleSystemShapeType import AleParticleSystemShapeType
from pydofus3.generated.pydantic.AleCore.Data.AleVector3 import AleVector3
from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import float_nan
from typing import Union, Annotated

class ParticlesShapeParameters(MyBaseModel):
	particleSystemShape: AleParticleSystemShapeType
	angle: float_nan
	radius: float_nan
	donutRadius: float_nan
	radiusThickness: float_nan
	arc: float_nan
	arcMode: AleParticleSystemShapeMultiModeValue
	arcSpread: float_nan
	arcSpeed: AleConstantOrCurve
	length: float_nan
	emitFromCone: Annotated[Union[AleParticleSystemEmitFromCone, int], Field(union_mode='left_to_right')]
	emitFromBox: Annotated[Union[AleParticleSystemEmitFromBox, int], Field(union_mode='left_to_right')]
	boxThickness: AleVector3
	shapePosition: AleVector3
	shapeRotation: AleVector3
	shapeScale: AleVector3
	alignToDirection: bool
	randomDirectionAmount: float_nan
	sphericalDirectionAmount: float_nan
	randomPositionAmount: float_nan

