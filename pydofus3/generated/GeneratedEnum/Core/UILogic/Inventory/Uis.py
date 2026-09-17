from enum import IntEnum

class ItemListSourceUi(IntEnum):
	PlayerInventory = 0

class ListContentType(IntEnum):
	None_ = 0
	Ornaments = 1
	Title = 2

class MakinaGrid:
	class MakinaType(IntEnum):
		None_ = -1
		Animakina = 0
		Kromakina = 1
		Optimakina = 2

