from enum import IntEnum

class HorizontalAnchorType(IntEnum):
	Top = 0
	Center = 1
	Bottom = 2

class OrnamentInfo:
	class ColorSource(IntEnum):
		none = 0
		guild = 1
		guildIcon = 2
		alliance = 3
		allianceIcon = 4

class TooltipAdditionalType(IntEnum):
	AlignmentCharacterInfo = 0
	OrnamentsCharacterInfo = 1

class TooltipArrow:
	class ArrowDirection(IntEnum):
		Right = 0
		Down = 1
		Left = 2
		Up = 3

class TooltipManipulatorBehavior(IntEnum):
	Leave = 0
	Out = 1

