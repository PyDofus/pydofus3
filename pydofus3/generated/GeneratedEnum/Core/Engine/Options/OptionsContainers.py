from enum import IntEnum

class DofusOptionsContainer:
	class TimelineTileSize(IntEnum):
		Big = 0
		Small = 1

	class TimelineGaugePlacement(IntEnum):
		Left = 0
		Right = 1

class RoleplayOptionsContainer:
	class gcd(IntEnum):
		dxdj = 0
		dxdk = 1

	class gce(IntEnum):
		dxdl = 0
		dxdm = 1

