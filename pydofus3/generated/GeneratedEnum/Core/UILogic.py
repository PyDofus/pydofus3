from enum import IntEnum
from enum import IntFlag

class CursorLayerEnum(IntEnum):
	Map = 0
	Interactive = 1
	Frustum = 2
	UI = 3

class CursorStateEnum(IntFlag):
	None_ = 0
	Disabled = 1
	Wait = 2

class CursorType(IntEnum):
	NotFound = -2
	None_ = -1
	Invalid = 0
	Gear = 1
	Bubble = 2
	Lock = 4
	Sword = 8
	Scythe = 16
	Axe = 32
	Hook = 64
	Book = 128
	House = 256
	Pickaxe = 512
	Shears = 1024
	Teleport = 2048
	Disabled = 4096
	Hourglass = 8192
	Forbidden = 16384
	Beam = 32768
	Move = 65536
	ResizeEW = 131072
	ResizeNESW = 262144
	ResizeNS = 524288
	ResizeNWSE = 1048576
	Link = 2097152
	Ping = 4194304
	PingSword = 8388608
	Shield = 16777216
	Heart = 33554432
	Target = 67108864
	Skull = 134217728
	One = 268435456
	Two = 536870912
	Three = 1073741824

