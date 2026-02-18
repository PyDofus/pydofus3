from enum import IntFlag

# Core.Enums.BreedEnum
class BreedEnum(IntFlag):
    Undefined = 0
    Feca = 1
    Osamodas = 2
    Enutrof = 3
    Sram = 4
    Xelor = 5
    Ecaflip = 6
    Eniripsa = 7
    Iop = 8
    Cra = 9
    Sadida = 10
    Sacrieur = 11
    Pandawa = 12
    Roublard = 13
    Zobal = 14
    Steamer = 15
    Eliotrope = 16
    Huppermage = 17
    Ouginak = 18
    Forgelance = 20
    Summoned = -1
    Monster = -2
    MonsterGroup = -3
    NPC = -4
    TaxCollector = -5
    Mutant = -6
    MutantInDungeon = -7
    MountOutside = -8
    Prism = -9

# Core.Enums.BuildTypeEnum
class BuildTypeEnum(IntFlag):
    RELEASE = 0
    BETA = 1
    ALPHA = 2
    TESTING = 3
    INTERNAL = 4
    DEBUG = 5
    DRAFT = 6

# Core.Enums.CharacterCosmeticPositionEnum
class CharacterCosmeticPositionEnum(IntFlag):
    POSITION_TITLES = -12
    POSITION_AURAS = -11
    POSITION_ORNAMENTS = -10
    POSITION_AMULET = 0
    POSITION_RING_LEFT = 1
    POSITION_RING_RIGHT = 2
    POSITION_BELT = 3
    POSITION_BOOTS = 4
    POSITION_PETMOUNT = 5
    POSITION_DRAGOTURKEY = 6
    POSITION_RHINEETLE = 7
    POSITION_SEEMYOOL = 8
    POSITION_CAPE = 9
    POSITION_HAT = 10
    POSITION_PET = 11
    POSITION_SHIELD = 12
    POSITION_BOW = 13
    POSITION_WAND = 14
    POSITION_STAFF = 15
    POSITION_DAGGER = 16
    POSITION_SCYTHE = 17
    POSITION_AXE = 18
    POSITION_LANCE = 19
    POSITION_HAMMER = 20
    POSITION_SHOVEL = 21
    POSITION_SWORD = 22
    POSITION_DISGUISE = 23
    POSITION_WINGS = 24
    POSITION_SHOULDERS = 25
    POSITION_NOT_EQUIPED = 63

# Core.Enums.CharacterInventoryPositionEnum
class CharacterInventoryPositionEnum(IntFlag):
    ACCESSORY_POSITION_HAT = 6
    ACCESSORY_POSITION_CAPE = 7
    ACCESSORY_POSITION_BELT = 3
    ACCESSORY_POSITION_BOOTS = 5
    ACCESSORY_POSITION_AMULET = 0
    ACCESSORY_POSITION_SHIELD = 15
    ACCESSORY_POSITION_WEAPON = 1
    ACCESSORY_POSITION_PETS = 8
    ACCESSORY_POSITION_RIDE_HARNESS = 29
    INVENTORY_POSITION_RING_LEFT = 2
    INVENTORY_POSITION_RING_RIGHT = 4
    INVENTORY_POSITION_DOFUS_1 = 9
    INVENTORY_POSITION_DOFUS_2 = 10
    INVENTORY_POSITION_DOFUS_3 = 11
    INVENTORY_POSITION_DOFUS_4 = 12
    INVENTORY_POSITION_DOFUS_5 = 13
    INVENTORY_POSITION_DOFUS_6 = 14
    INVENTORY_POSITION_MOUNT = 16
    INVENTORY_POSITION_MUTATION = 20
    INVENTORY_POSITION_BOOST_FOOD = 21
    INVENTORY_POSITION_FIRST_BONUS = 22
    INVENTORY_POSITION_SECOND_BONUS = 23
    INVENTORY_POSITION_FIRST_MALUS = 24
    INVENTORY_POSITION_SECOND_MALUS = 25
    INVENTORY_POSITION_ROLEPLAY_BUFFER = 26
    INVENTORY_POSITION_FOLLOWER = 27
    INVENTORY_POSITION_ENTITY = 28
    INVENTORY_POSITION_COSTUME = 30
    INVENTORY_POSITION_CONSUMABLE = 31
    INVENTORY_POSITION_NOT_EQUIPED = 63

# Core.Enums.JobUis
class JobUis(IntFlag):
    Craft = 0
    CrafterList = 1
    CraftCoop = 2
    SmithMagic = 3
    SmithMagicCoop = 4
    CheckCraft = 5
    RuneMaker = 6

