from pydofus3.not_generated.base import MyBaseModel


class ClientCellData(MyBaseModel):
	cellNumber: int
	speed: int
	mapChangeData: int
	moveZone: int
	linkedZone: int
	mov: bool
	los: bool
	nonWalkableDuringFight: bool
	nonWalkableDuringRP: bool
	farmCell: bool
	visible: bool
	havenbagCell: bool
	roleplayMonstersMovementBlocked: bool
	floor: int
	red: bool
	blue: bool
	arrow: int

