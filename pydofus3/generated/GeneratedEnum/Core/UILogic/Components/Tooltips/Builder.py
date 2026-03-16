from enum import IntEnum
from enum import IntFlag

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

