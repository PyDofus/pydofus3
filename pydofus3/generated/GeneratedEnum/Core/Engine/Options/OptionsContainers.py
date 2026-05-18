from enum import IntEnum

class DofusOptionsContainer:
	class TimelineTileSize(IntEnum):
		Big = 0
		Small = 1

	class TimelineGaugePlacement(IntEnum):
		Left = 0
		Right = 1

class RoleplayOptionsContainer:
	class fte(IntEnum):
		dqeu = 0
		dqev = 1

	class ftf(IntEnum):
		dqew = 0
		dqex = 1

