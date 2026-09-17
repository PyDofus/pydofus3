from enum import IntEnum

class RetrieveConfirmationPopup:
	class SortType(IntEnum):
		None_ = 0
		Name = 1
		Quantity = 2

class WebGiftMysteryBoxUi:
	class MysteryBoxRarityEnum(IntEnum):
		Common = 0
		Uncommon = 1
		Rare = 2
		Epic = 3
		Legendary = 4
		NoRarity = 5

