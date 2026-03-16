from enum import IntEnum
from enum import IntFlag

class TooltipBuilderFlags(IntFlag):
	None_ = 0
	BringToFront = 1
	AutoHide = 2
	DirectionalArrow = 4
	AllowRefresh = 8
	KeepOnZoom = 16
	Collisions = 32
	ScreenCollision = 64
	InsertLayer = 128
	IgnoreHideAll = 256
	ReplacePrevious = 512
	GroupByEntityNeighbors = 1024
	SyncWithTarget = 2048
	SyncWithZoom = 4096
	All = 4294967295

class TooltipPositioning:
	class Location(IntEnum):
		TopLeft = 0
		TopCenter = 1
		TopRight = 2
		CenterLeft = 3
		Center = 4
		CenterRight = 5
		BottomLeft = 6
		BottomCenter = 7
		BottomRight = 8

