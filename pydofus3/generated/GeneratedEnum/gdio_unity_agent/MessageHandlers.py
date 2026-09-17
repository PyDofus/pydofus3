from enum import IntEnum

class HookingObject(IntEnum):
	KEYBOARD = 1
	MOUSE = 2
	GAMEPAD = 4
	TOUCHINPUT = 8
	XRLEGACY = 16
	ALL = 31

