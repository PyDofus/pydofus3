from enum import IntEnum

class DofusOptionsContainer:
	class TimelineTileSize(IntEnum):
		Big = 0
		Small = 1

	class TimelineGaugePlacement(IntEnum):
		Left = 0
		Right = 1

class RoleplayOptionsContainer:
	class gcr(IntEnum):
		dxmn = 0
		dxmo = 1

	class gcs(IntEnum):
		dxmp = 0
		dxmq = 1

