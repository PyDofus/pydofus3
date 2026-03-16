from enum import IntEnum

class AbstractCosmeticTab:
	class CosmeticTabs(IntEnum):
		None_ = 0
		Items = 1
		Ornaments = 2
		Titles = 3
		Auras = 4

class CosmeticItemsTab:
	class ItemTypes(IntEnum):
		LivingObjects = 113
		Costume = 199
		Hats = 246
		Cloaks = 247
		Shields = 248
		Pets = 249
		PetMounts = 250
		Weapons = 251
		Misc = 252
		Shoulders = 299
		Wings = 300
		Amulet = 316
		Shoes = 317
		Rings = 318
		Mounts = 324

