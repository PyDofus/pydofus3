from enum import IntEnum

class DofusOptionsContainer:
	class TimelineTileSize(IntEnum):
		Big = 0
		Small = 1

	class TimelineGaugePlacement(IntEnum):
		Left = 0
		Right = 1

class RoleplayOptionsContainer:
	class gcb(IntEnum):
		dxmo = 0
		dxmp = 1

	class gcc(IntEnum):
		dxmq = 0
		dxmr = 1

