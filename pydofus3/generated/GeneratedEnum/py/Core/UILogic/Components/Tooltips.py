from enum import IntFlag

# Core.UILogic.Components.Tooltips.HorizontalAnchorType
class HorizontalAnchorType(IntFlag):
    Top = 0
    Center = 1
    Bottom = 2

# Core.UILogic.Components.Tooltips.TooltipAdditionalType
class TooltipAdditionalType(IntFlag):
    AlignmentCharacterInfo = 0
    OrnamentsCharacterInfo = 1

# Core.UILogic.Components.Tooltips.TooltipArrow
class TooltipArrow(IntFlag):
    Right = 0
    Down = 1
    Left = 2
    Up = 3

# Core.UILogic.Components.Tooltips.TooltipManipulatorBehavior
class TooltipManipulatorBehavior(IntFlag):
    Leave = 0
    Out = 1

# Core.UILogic.Components.Tooltips.TooltipType
class TooltipType(IntFlag):
    Text = 0
    TextInfo = 1
    TextWithTitle = 2
    TextWithTexture = 4
    TextInfoWithHorizontalSeparator = 5
    Spell = 6
    SpellBanner = 7
    WeaponBanner = 8
    Item = 9
    ItemName = 10
    Smiley = 11
    ChatBubble = 12
    ThinkBubble = 13
    Player = 14
    Mutant = 15
    MonsterGroup = 17
    BreachMonsterGroup = 18
    Merchant = 19
    GroundObject = 20
    TaxCollector = 21
    Effects = 23
    EffectsList = 24
    TexturesList = 25
    DelayedAction = 26
    Prism = 27
    Portal = 28
    Mount = 29
    Paddock = 30
    PaddockItem = 31
    PaddockMount = 32
    Challenge = 33
    PlayerFighter = 34
    MonsterFighter = 35
    CompanionFighter = 36
    RoleplayFight = 37
    House = 38
    SlotTexture = 39
    SellCriterion = 40
    InteractiveElement = 41
    DirectionalSign = 42
    BreachReward = 43
    MysteryBox = 44
    SimpleInterfaceTuto = 45
    CartographyAreaMap = 46
    StatFloors = 47
    BreachRoom = 48
    Alteration = 49
    EntityIconList = 50
    Cartography = 51
    Stats = 52
    SpellPair = 53
    EntityDebug = 54
    FighterInfo = 55
    FighterInfoHorizontal = 56
    FightBuff = 57
    FightMapPreviewLegend = 58
    BuffsUiHelp = 59
    MainStatDetails = 60
    Shortcut = 61
    MonsterCharacteristics = 62
    PetFood = 63
    ChatMonsterGroup = 64
    BreachGate = 65
    InfiniteDreamPartners = 66
    PingShortcut = 67
    TemporaryPingShortcut = 68
    GuildActivityRewards = 69

