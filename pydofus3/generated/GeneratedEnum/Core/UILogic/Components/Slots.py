from enum import IntEnum

class DragOwner(IntEnum):
	None_ = 0
	BannerMenu = 1
	Mimicry = 2
	MimicryStorage = 3
	EquipmentComponent = 4
	Bag = 5
	CharacterBuild = 6
	CharacterBuildSpell = 7
	Exchange = 8
	ExchangeStorage = 9
	SmithMagicStorage = 10
	SmithMagic = 11
	SmithMagicCoopBag = 12
	Craft = 13
	CraftOther = 14
	CraftStorage = 15
	Spell = 16
	TaxCollectorPersonalization = 17
	TaxCollectorActivePresetSpells = 18
	TaxCollectorPersonalizationStorage = 19
	TaxCollectorEquipment = 20
	PrismModule = 21
	PrismModuleStorage = 22
	Recycle = 23
	RecycleStorage = 24
	ActionBar1 = 100
	ActionBar2 = 101
	ActionBar3 = 102
	ActionBar4 = 103
	ActionBar5 = 104
	ActionBar6 = 105
	ActionBar7 = 106
	ActionBar8 = 107
	LevelUp = 108
	Companion = 109
	FeedUi = 110
	NpcStore = 111
	NpcStoreStorage = 112
	Cosmetic = 113
	CosmeticUi = 114
	OutfitManager = 115
	OutfitList = 116
	RuneMaker = 117
	Smiley = 118
	Emote = 119
	SmileyMood = 120
	MountStable = 121
	MountPaddock = 122
	MountEquipped = 123
	MatingUi = 124
	ExtractionUi = 125
	FillPaddockGaugeUi = 126
	PaddockUi = 127

class Slot:
	class SlotSize(IntEnum):
		xSmall = 0
		small = 1
		medium = 2
		large = 3

	class SlotType(IntEnum):
		inventory = 0
		cosmetic = 1
		navigation = 2
		button = 3
		spell = 4

	class SlotRarity(IntEnum):
		None_ = 0
		silver = 1
		gold = 2

class Tile:
	class TileContent(IntEnum):
		asset = 0
		colorWheel = 1
		icon = 2
		none = 3

	class TileFavorite(IntEnum):
		favoriteTrue = 0
		favoriteFalse = 1
		none = 2

	class TileGhost(IntEnum):
		ghostTrue = 0
		ghostFalse = 1
		none = 2

	class TileSelected(IntEnum):
		selectedTrue = 0
		none = 1

	class TileAcquired(IntEnum):
		acquiredTrue = 0
		acquiredModerate = 1
		acquiredFalse = 2
		partial = 3
		none = 4

	class TileRarity(IntEnum):
		None_ = 0
		silver = 1
		gold = 2

	class ColorStyle(IntEnum):
		none = 0
		blue = 1
		green = 2

