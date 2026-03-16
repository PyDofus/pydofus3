from pydofus3.not_generated.base import FlagBaseModel
from typing import Annotated

class MonsterFlags(FlagBaseModel):
	UseSummonSlot : Annotated[bool,1]
	UseBombSlot : Annotated[bool,2]
	IsBoss : Annotated[bool,4]
	IsMiniBoss : Annotated[bool,8]
	IsQuestMonster : Annotated[bool,16]
	FastAnimsFun : Annotated[bool,32]
	CanPlay : Annotated[bool,64]
	CanTackle : Annotated[bool,128]
	CanBePushed : Annotated[bool,256]
	CanSwitchPos : Annotated[bool,512]
	CanSwitchPosOnTarget : Annotated[bool,1024]
	CanBeCarried : Annotated[bool,2048]
	CanUsePortal : Annotated[bool,4096]
	AllIdolsDisabled : Annotated[bool,8192]
	UseRaceValues : Annotated[bool,16384]
	SoulCaptureForbidden : Annotated[bool,32768]
	HideInBestiary : Annotated[bool,65536]

