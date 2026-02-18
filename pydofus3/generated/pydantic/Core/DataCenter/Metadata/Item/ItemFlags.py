from typing import Annotated
from pydofus3.not_generated.base import FlagBaseModel


class ItemFlags(FlagBaseModel):
	Usable : Annotated[bool,1]
	Targetable : Annotated[bool,2]
	Exchangeable : Annotated[bool,4]
	TwoHanded : Annotated[bool,8]
	Etheral : Annotated[bool,16]
	HideEffects : Annotated[bool,32]
	Enhanceable : Annotated[bool,64]
	NonUsableOnAnother : Annotated[bool,128]
	SecretRecipe : Annotated[bool,256]
	NeedUseConfirm : Annotated[bool,512]
	IsSaleable : Annotated[bool,1024]
	IsLegendary : Annotated[bool,2048]

