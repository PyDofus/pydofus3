from enum import IntEnum
from enum import IntFlag

class DisplayOptions(IntFlag):
	None_ = 0
	Ping = 1
	Class = 2
	Entity = 4
	VitalGauges = 8
	VitalValues = 16
	States = 32
	VitalPercent = 64
	All = 4294967295

class TextTooltipBuilder:
	class TextTooltipStyleEnum(IntEnum):
		Normal = 0
		Malus = 1
		Npc = 2

class TooltipCollisionDodgeDirection(IntFlag):
	None_ = 0
	Up = 1
	Right = 2
	Down = 4
	Left = 8
	All = 15

