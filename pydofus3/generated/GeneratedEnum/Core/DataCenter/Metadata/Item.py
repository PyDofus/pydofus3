from enum import IntEnum
from enum import IntFlag

class ItemData:
	class ItemCategoryEnum(IntEnum):
		None_ = -2
		All = -1
		Equipment = 0
		Consumables = 1
		Resources = 2
		Quest = 3
		Other = 4
		Cosmetics = 5
		Favorites = 6
		Box1 = 7
		Box2 = 8
		Box3 = 9
		Box4 = 10
		Box5 = 11
		Box6 = 12
		Box7 = 13
		Box8 = 14
		Titles = 15
		Ornaments = 16
		Auras = 17
		EcaflipCard = 238

class ItemFlags(IntFlag):
	Usable = 1
	Targetable = 2
	Exchangeable = 4
	TwoHanded = 8
	Etheral = 16
	HideEffects = 32
	Enhanceable = 64
	NonUsableOnAnother = 128
	SecretRecipe = 256
	NeedUseConfirm = 512
	IsSaleable = 1024
	IsLegendary = 2048

