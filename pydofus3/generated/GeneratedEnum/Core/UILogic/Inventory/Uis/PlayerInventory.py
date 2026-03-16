from enum import IntEnum

class AppearanceType(IntEnum):
	None_ = 0
	Body = 1
	Color = 2
	Face = 3
	Idle = 4

class AppearanceUI:
	class AppearanceTab(IntEnum):
		Face = 0
		Body = 1
		Idle = 2
		Colors = 3

class CosmeticUi:
	class SortType(IntEnum):
		Default = 0
		Name = 1
		ItemSet = 2

class PresetListUi:
	class SortCriteria(IntEnum):
		Name = 0
		ModificationDate = 1

