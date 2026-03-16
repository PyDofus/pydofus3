from enum import IntEnum

class ContextMenuItem:
	class State(IntEnum):
		None_ = 0
		Checkbox = 1
		RadioButton = 2
		AssetToggle = 3
		ColorSquare = 4

class ContextMenuPageSwitchItem:
	class Direction(IntEnum):
		Previous = 0
		Next = 1

