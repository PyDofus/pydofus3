from enum import IntFlag

# Core.DataCenter.Metadata.Enums.ActionType
class ActionType(IntFlag):
    Caracteristics = 0
    Damages = 2
    SpellBoosts = 3
    Status = 4

# Core.DataCenter.Metadata.Enums.AdministrablePopUpAction
class AdministrablePopUpAction(IntFlag):
    Link = 0
    Action = 1

# Core.DataCenter.Metadata.Enums.AreaAndSubarea
class AreaAndSubarea(IntFlag):
    AreaIncarnam = 45
    SubareaTutorial = 536
    SubareaInfiniteBreach = 904

# Core.DataCenter.Metadata.Enums.BreachReward
class BreachReward(IntFlag):
    CurrencyBudget = 0
    CurrencyFragments = 1
    TranscendenceRune = 2
    CorruptionRune = 3
    StatBoost = 4
    PositiveModifier = 5
    AddBoss = 6
    Legendary = 7
    Others = 8

# Core.DataCenter.Metadata.Enums.BreedingItem
class BreedingItem(IntFlag):
    EnergyBaseSpellID = 208
    MaturyBaseSpellID = 207
    AggroBaseSpellID = 204
    SerenityBaseSpellID = 203
    LoveBaseSpellID = 206
    StaminaBaseSpellID = 205
    RemoveObjectBaseSpellID = 197

# Core.DataCenter.Metadata.Enums.CharacterBuildType
class CharacterBuildType(IntFlag):
    Undefined = -1
    Invalid = 0
    Character = 1
    ForgettableSpell = 2

# Core.DataCenter.Metadata.Enums.Characteristics
class Characteristics(IntFlag):
    HealthPointID = 0
    ActionPointID = 1
    TypePrimary = 2
    MovementPointID = 23
    RangeID = 19
    VitalityID = 11

# Core.DataCenter.Metadata.Enums.ChatChannel
class ChatChannel(IntFlag):
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

# Core.DataCenter.Metadata.Enums.EntityType
class EntityType(IntFlag):
    Breed = 1
    Companion = 2

# Core.DataCenter.Metadata.Enums.HintCategory
class HintCategory(IntFlag):
    Temples = 1
    BidHouse = 2
    CraftHouses = 3
    Misc = 4
    Dungeons = 6
    Transportations = 9

# Core.DataCenter.Metadata.Enums.ItemGid
class ItemGid(IntFlag):
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
    BreachFragments = 20292
    BebemothReflect = 20968
    KokokoRecycler = 17207
    FairTradeRecycler = 17166
    CollectiveRecycler = 17167
    PacifyCristal = 27631
    InhibCristal = 27632
    UnknownItemGid = 666

# Core.DataCenter.Metadata.Enums.ItemSuperTypeEnum
class ItemSuperTypeEnum(IntFlag):
    NONE = -1
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

# Core.DataCenter.Metadata.Enums.ItemTypeEnum
class ItemTypeEnum(IntFlag):
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

# Core.DataCenter.Metadata.Enums.JobId
class JobId(IntFlag):
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

# Core.DataCenter.Metadata.Enums.JobSkillsActions
class JobSkillsActions(IntFlag):
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

# Core.DataCenter.Metadata.Enums.MinoukiEffects
class MinoukiEffects(IntFlag):
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

# Core.DataCenter.Metadata.Enums.MonsterType
class MonsterType(IntFlag):
    Osatopia = 248

# Core.DataCenter.Metadata.Enums.MountAbility
class MountAbility(IntFlag):
    Autopilot = 10

# Core.DataCenter.Metadata.Enums.RoleId
class RoleId(IntFlag):
    Debuffer = 1
    Tank = 2
    Protector = 3
    Healer = 4
    Damage_Dealer = 5
    Positioner = 6
    Summoner = 7
    Buffer = 8

# Core.DataCenter.Metadata.Enums.ServerCommunity
class ServerCommunity(IntFlag):
    FrenchSpeaking = 0
    EnglishSpeaking = 1
    International = 2
    Global = 12
    Beta = 100

# Core.DataCenter.Metadata.Enums.ShortCutBarTypes
class ShortCutBarTypes(IntFlag):
    Item = 2
    Preset = 3
    Spell = 4
    Smiley = 5
    Emote = 6
    Outfit = 8
    CosmeticItem = 7

# Core.DataCenter.Metadata.Enums.Skills
class Skills(IntFlag):
    LockHouse = 81
    BuyHouse = 97
    SellHouse = 98
    UnlockHouse = 100
    ChangePriceHouse = 108
    MageShoes = 164
    MageTailor = 166
    MageJewel = 168
    AccessPaddock = 175
    BuyPaddock = 176
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

# Core.DataCenter.Metadata.Enums.SocialTab
class SocialTab(IntFlag):
    LastOpenedID = -1
    FriendsID = 0
    GuildID = 1
    AllianceID = 2
    SpouseID = 3
    GuildDirectoryID = 4
    AllianceDirectoryID = 5

# Core.DataCenter.Metadata.Enums.SpellScriptType
class SpellScriptType(IntFlag):
    Fallback = -1
    Invalid = 0
    OneOrTwoGfx = 1
    Projectile = 2
    TrailEffect = 3
    Mark = 5
    RoleplaySpell = 6
    Weapon = 7
    Kamehameha = 8
    NextGen = 9

# Core.DataCenter.Metadata.Enums.Spells
class Spells(IntFlag):
    SramDouble = 12915
    SramTraps = 9846
    RogueRoguery = 13431
    StateRooted = 6
    StateCarried = 8
    StateInvulnerable = 56
    StateUnhealable = 76
    StateCantLock = 95
    StateArcher = 101
    StateCantBeLocked = 96
    StateTelefragAlly = 244
    StateTelefragEnemy = 251

# Core.DataCenter.Metadata.Enums.TextNotifications
class TextNotifications(IntFlag):
    ServerInformation = 24
    ServerKolossium = 33
    ServerGift = 34
    ServerKothSuperiority = 36

# Core.DataCenter.Metadata.Enums.World
class World(IntFlag):
    AmaknaDefault = 0
    Debug = 1
    Test = 2
    Startzone = 3

