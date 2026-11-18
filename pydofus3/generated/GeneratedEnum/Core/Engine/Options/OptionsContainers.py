from enum import IntEnum

class DofusOptionsContainer:
	class TimelineTileSize(IntEnum):
		Big = 0
		Small = 1

	class TimelineGaugePlacement(IntEnum):
		Left = 0
		Right = 1

class RoleplayOptionsContainer:
	class gtl(IntEnum):
		ebto = 0
		ebtp = 1

	class gtm(IntEnum):
		ebtq = 0
		ebtr = 1

