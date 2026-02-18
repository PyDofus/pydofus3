from enum import IntFlag

# Metadata.Enums.AlmanaxCalendarCategory
class AlmanaxCalendarCategory(IntFlag):
    Special = 2
    Floating = 3
    Javian = 4
    Flovor = 5
    Martalo = 6
    Aperirel = 7
    Maisial = 8
    Juinssidor = 9
    Joullier = 10
    Fraouctor = 11
    Septange = 12
    Octolliard = 13
    Novamaire = 14
    Descendre = 15

# Metadata.Enums.CollectableCategory
class CollectableCategory(IntFlag):
    Common = 0
    Rare = 1
    Evolution = 2
    Epic = 3
    Legendary = 4

# Metadata.Enums.Collection
class Collection(IntFlag):
    Mobedex = 1

# Metadata.Enums.SkinSlotRuleType
class SkinSlotRuleType(IntFlag):
    Default = 0
    Breed = 1
    BreedAndSex = 2
    Face = 3

# Metadata.Enums.SpellZoneShape
class SpellZoneShape(IntFlag):
    NONE = 0
    Point = 80
    Circle = 67
    OutsideCircle = 73
    Regular = 78
    OutsideComplexCircle = 90
    Ring = 79
    HalfCircle = 85
    Line = 76
    DiagonalLine = 47
    LineFromCaster = 108
    PerpendicularLine = 84
    DiagonalPerpendicularLine = 45
    Cross = 88
    CrossWithoutCenter = 81
    DiagonalCross = 43
    DiagonalCrossWithoutCenter = 35
    Star = 42
    Checkerboard = 68
    Cone = 86
    Boomerang = 66
    Square = 71
    SquareWithoutDiagonals = 87
    Rectangle = 82
    Fork = 70
    WholeMap = 97
    WholeMapWithTheDead = 65
    Custom = 59
    Empty = 32

# Metadata.Enums.WorldEventDataType
class WorldEventDataType(IntFlag):
    WorldBoss = 1
    MonstersHunter = 2
    Dungeon = 3
    FarmingSimulator = 4

