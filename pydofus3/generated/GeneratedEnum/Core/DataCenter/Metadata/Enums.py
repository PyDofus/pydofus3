from enum import IntEnum

class ActionType(IntEnum):
	Caracteristics = 0
	Damages = 2
	SpellBoosts = 3
	Status = 4

class AdministrablePopUpAction(IntEnum):
	Link = 0
	Action = 1

class AreaAndSubarea(IntEnum):
	AreaIncarnam = 45
	SubareaTutorial = 536
	SubareaInfiniteBreach = 904

class BreachReward(IntEnum):
	CurrencyBudget = 0
	CurrencyFragments = 1
	TranscendenceRune = 2
	CorruptionRune = 3
	StatBoost = 4
	PositiveModifier = 5
	AddBoss = 6
	Legendary = 7
	Others = 8

class BreedingItem(IntEnum):
	RemoveObjectBaseSpellID = 197
	SerenityBaseSpellID = 203
	AggroBaseSpellID = 204
	StaminaBaseSpellID = 205
	LoveBaseSpellID = 206
	MaturyBaseSpellID = 207
	EnergyBaseSpellID = 208

class CharacterBuildType(IntEnum):
	Undefined = -1
	Invalid = 0
	Character = 1
	ForgettableSpell = 2

class Characteristics(IntEnum):
	HealthPointID = 0
	ActionPointID = 1
	TypePrimary = 2
	VitalityID = 11
	RangeID = 19
	MovementPointID = 23

class ChatChannel(IntEnum):
	General = 0
	Team = 1
	Guild = 2
	Alliance = 3
	Group = 4
	Trade = 5
	Recruitment = 6
	Noob = 7
	Admin = 8
	Private = 9
	Information = 10
	Fight = 11
	Promotional = 12
	Arena = 13
	Community = 14

class EntityType(IntEnum):
	Breed = 1
	Companion = 2

class HintCategory(IntEnum):
	Temples = 1
	BidHouse = 2
	CraftHouses = 3
	Misc = 4
	Dungeons = 6
	Transportations = 9

class ItemGid(IntEnum):
	UnknownItemGid = 666
	Soulstone = 7010
	SignatureRune = 7508
	DragoturkeyBreedingBook = 7805
	HuntingRune = 10057
	SoulstoneBoss = 10417
	SoulstoneMiniboss = 10418
	PresetShortcut = 11589
	Dolmanax = 13344
	CalendarPage = 13345
	TeleportationModule = 14552
	Nugget = 14635
	SandsRose = 15263
	FairTradeRecycler = 17166
	CollectiveRecycler = 17167
	KokokoRecycler = 17207
	BreachFragments = 20292
	BebemothReflect = 20968
	InhibCristal = 27631
	PacifyCristal = 27632

class ItemSuperTypeEnum(IntEnum):
	None_ = -1
	Collar = 1
	Weapon = 2
	Ring = 3
	Belt = 4
	Shoes = 5
	Consumable = 6
	Shield = 7
	CatchingItems = 8
	Resources = 9
	Helmet = 10
	Cape = 11
	Pet = 12
	DofusTrophy = 13
	QuestItems = 14
	Mutations = 15
	Foods = 16
	Blessings = 17
	Curses = 18
	RoleplayBuffs = 19
	Followers = 20
	Mounts = 21
	LivingItems = 22
	Companion = 23
	MountEquipment = 24
	Costume = 25
	Certificate = 27
	PetGhost = 28
	TaxCollectorEquipment = 69
	FightConsumable = 70

class ItemTypeEnum(IntEnum):
	Collar = 1
	Bow = 2
	Rod = 3
	Staff = 4
	Dagger = 5
	Sword = 6
	Hammer = 7
	Shovel = 8
	Ring = 9
	Belt = 10
	Shoes = 11
	Hat = 16
	Cloak = 17
	Pet = 18
	Axe = 19
	Pickaxe = 21
	Scythe = 22
	Dofus = 23
	SmithmagicPotion = 26
	Mutations = 27
	RoleplayBuffs = 31
	Meat = 63
	PetEgg = 72
	SmithmagicRune = 78
	Drink = 79
	Backpack = 81
	Shield = 82
	EmptySoulstone = 83
	Soulstone = 85
	BreedingItem = 93
	DragoturkeyCertificate = 97
	CatchingNet = 99
	Crossbow = 102
	Wing = 104
	Prism = 112
	LivingObject = 113
	MagicWeapon = 114
	PetPotion = 116
	Hidden = 118
	Petsmount = 121
	PetsmountPotion = 122
	Trophy = 151
	Mimisymbic = 166
	Companion = 169
	CeremonialItems = 177
	IdolsRessource = 178
	SmithmagicOrb = 189
	HarnessMount = 190
	MuldoCertificate = 196
	Receipt = 197
	CosmeticCostume = 199
	MountPotion = 206
	FlyhornCertificate = 207
	PetFood = 209
	SmithmagicTranscendanceRune = 211
	SmithmagicCorruptionRune = 212
	Prysmaradite = 217
	Havenbag = 218
	TemporisSpellScroll = 223
	TemporisHiddenSpell = 224
	TemporisRichetonBag = 226
	SmithmagicAstralRune = 233
	TemporisCard = 238
	Minouki = 240
	CosmeticHat = 246
	CosmeticCloak = 247
	CosmeticShield = 248
	CosmeticPet = 249
	CosmeticPetmount = 250
	CosmeticWeapon = 251
	CosmeticMisc = 252
	HarnessMuldo = 255
	HarnessFlyhorn = 256
	SmithMagicCarving = 258
	Klonebawks = 259
	Modster = 261
	IdolsEquipment = 267
	Lance = 271
	TaxCollectorHorseShoe = 273
	TaxCollectorCuirass = 274
	TaxCollectorBanner = 275
	TaxCollectorDagger = 276
	TaxCollectorTunic = 277
	TaxCollectorChest = 279
	TaxCollectorBag = 280
	ShoulderPad = 299
	CosmeticWings = 300
	TamedMount = 301
	CosmeticFace = 306
	Makina = 323
	PaddockRessources = 326
	SoulStoneBoss = 327
	SoulStoneMiniBoss = 328
	CosmeticBody = 329
	CosmeticIdle = 330
	DragoTurkey = 331
	Muldo = 332
	FlyHorn = 333

class JobId(IntEnum):
	Base = 1
	Lumberjack = 2
	Smith = 11
	Carver = 13
	Shoemaker = 15
	Jeweler = 16
	Miner = 24
	Alchemist = 26
	Tailor = 27
	Farmer = 28
	Fisherman = 36
	Hunter = 41
	Smithmagus = 44
	Carvmagus = 48
	Artificer = 60
	Shoemagus = 62
	Jewelmagus = 63
	Costumagus = 64
	Handyman = 65
	Craftmagus = 74
	Breeder = 79

class JobSkillsActions(IntEnum):
	Other = 0
	Resource = 1
	Craft = 2
	Waypoint = 3
	LifeRegenerationNovice = 4
	Door = 5
	Storage = 6
	LifeRegeneration = 7
	FightAgainstMonster = 8
	ModifyInventory = 9
	SubwayPoint = 10
	Obstacle = 11
	JobIndex = 12
	Farm = 13
	Switch = 14
	ClassStatue = 15
	ExecuteActions = 16
	TopTaxCollector = 17

class MinoukiEffects(IntEnum):
	CardSuperEffectID = 3
	MinoukiSuperEffectID = 4
	CardBonusCustomEffectID = 5
	CardHeartCustomEffectID = 6
	CardDiamondCustomEffectID = 7
	CardSpadeCustomEffectID = 8
	CardClubCustomEffectID = 9
	LocationBonusCustomEffectID = 10
	LocationHeartCustomEffectID = 11
	LocationDiamondCustomEffectID = 12
	LocationSpadeCustomEffectID = 13
	LocationClubCustomEffectID = 14

class MonsterType(IntEnum):
	Osatopia = 248

class MountAbility(IntEnum):
	Autopilot = 10

class RoleId(IntEnum):
	Debuffer = 1
	Tank = 2
	Protector = 3
	Healer = 4
	Damage_Dealer = 5
	Positioner = 6
	Summoner = 7
	Buffer = 8

class ServerCommunity(IntEnum):
	FrenchSpeaking = 0
	EnglishSpeaking = 1
	International = 2
	Global = 12
	Beta = 100

class ShortCutBarTypes(IntEnum):
	Item = 2
	Preset = 3
	Spell = 4
	Smiley = 5
	Emote = 6
	CosmeticItem = 7
	Outfit = 8

class Skills(IntEnum):
	LockHouse = 81
	BuyHouse = 97
	SellHouse = 98
	UnlockHouse = 100
	ChangePriceHouse = 108
	MageShoes = 164
	MageTailor = 166
	MageJewel = 168
	SellPaddock = 177
	ModifyPaddockPrice = 178
	ShatterItem = 181
	WrapGift = 209
	PointOutExit = 339
	SignFreeText = 360
	SignHint = 361
	SignSubarea = 362
	Chinq = 397
	Minouki = 398

class SocialTab(IntEnum):
	LastOpenedID = -1
	FriendsID = 0
	GuildID = 1
	AllianceID = 2
	SpouseID = 3
	GuildDirectoryID = 4
	AllianceDirectoryID = 5

class Spells(IntEnum):
	StateRooted = 6
	StateCarried = 8
	StateInvulnerable = 56
	StateUnhealable = 76
	StateCantLock = 95
	StateCantBeLocked = 96
	StateArcher = 101
	StateTelefragAlly = 244
	StateTelefragEnemy = 251
	SramTraps = 9846
	SramDouble = 12915
	RogueRoguery = 13431

class SpellScriptType(IntEnum):
	Invalid = 0
	OneOrTwoGfx = 1
	Projectile = 2
	TrailEffect = 3
	Mark = 5
	RoleplaySpell = 6
	Weapon = 7
	Kamehameha = 8
	NextGen = 9
	Fallback = 255

class TextNotifications(IntEnum):
	ServerInformation = 24
	ServerKolossium = 33
	ServerGift = 34
	ServerKothSuperiority = 36

class World(IntEnum):
	AmaknaDefault = 0
	Debug = 1
	Test = 2
	Startzone = 3

