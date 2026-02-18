from typing import Annotated
from pydofus3.not_generated.base import FlagBaseModel


class SpellLevelFlags(FlagBaseModel):
	CastInLine : Annotated[bool,1]
	CastInDiagonal : Annotated[bool,2]
	CastTestLos : Annotated[bool,4]
	NeedFreeCell : Annotated[bool,8]
	NeedTakenCell : Annotated[bool,16]
	NeedFreeTrapCell : Annotated[bool,32]
	RangeCanBeBoosted : Annotated[bool,64]
	HideEffects : Annotated[bool,128]
	Hidden : Annotated[bool,256]
	PlayAnimation : Annotated[bool,512]
	NeedVisibleEntity : Annotated[bool,1024]
	NeedCellWithoutPortal : Annotated[bool,2048]
	PortalProjectionForbidden : Annotated[bool,4096]

