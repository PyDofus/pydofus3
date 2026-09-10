from enum import IntEnum

class DofusOptionsContainer:
	class TimelineTileSize(IntEnum):
		Big = 0
		Small = 1

	class TimelineGaugePlacement(IntEnum):
		Left = 0
		Right = 1

class RoleplayOptionsContainer:
	class gcv(IntEnum):
		dxfe = 0
		dxff = 1

	class gcw(IntEnum):
		dxfg = 0
		dxfh = 1

