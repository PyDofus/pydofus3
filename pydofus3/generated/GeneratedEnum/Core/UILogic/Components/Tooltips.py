from enum import IntEnum

class HorizontalAnchorType(IntEnum):
	Top = 0
	Center = 1
	Bottom = 2

class TooltipAdditionalType(IntEnum):
	AlignmentCharacterInfo = 0
	OrnamentsCharacterInfo = 1

class TooltipArrow:
	class ArrowDirection(IntEnum):
		Right = 0
		Down = 1
		Left = 2
		Up = 3

class TooltipManipulatorBehavior(IntEnum):
	Leave = 0
	Out = 1

class TooltipType(IntEnum):
	Text = 0
	TextWithTitle = 2
	TextWithTexture = 4
	Spell = 6
	SpellBanner = 7
	WeaponBanner = 8
	Item = 9
	ItemName = 10
	Smiley = 11
	ChatBubble = 12
	ThinkBubble = 13
	Player = 14
	MonsterGroup = 17
	GroundObject = 20
	TaxCollector = 21
	TexturesList = 25
	DelayedAction = 26
	Prism = 27
	Portal = 28
	Mount = 29
	Challenge = 33
	PlayerFighter = 34
	MonsterFighter = 35
	CompanionFighter = 36
	RoleplayFight = 37
	House = 38
	SellCriterion = 40
	InteractiveElement = 41
	DirectionalSign = 42
	BreachReward = 43
	MysteryBox = 44
	SimpleInterfaceTuto = 45
	StatFloors = 47
	Alteration = 49
	EntityIconList = 50
	Cartography = 51
	Stats = 52
	SpellPair = 53
	EntityDebug = 54
	FighterInfo = 55
	FightBuff = 57
	FightMapPreviewLegend = 58
	BuffsUiHelp = 59
	MainStatDetails = 60
	Shortcut = 61
	MonsterCharacteristics = 62
	PetFood = 63
	ChatMonsterGroup = 64
	BreachGate = 65
	PingShortcut = 67
	TemporaryPingShortcut = 68
	GuildActivityRewards = 69
	PaddockGauge = 70
	MarketPrice = 71
	GuildActivityToken = 72

