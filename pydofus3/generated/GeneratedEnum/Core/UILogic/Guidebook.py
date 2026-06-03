from enum import IntEnum

class AdventureSubTab(IntEnum):
	None_ = -1
	Collection = 0
	TemporisTab = 1
	Dofus = 2
	Suggestions = 3

class GameCollectionTabUI:
	class FilterEnum(IntEnum):
		All = 0
		Discovered = 1

	class SortType(IntEnum):
		Order = 0
		Name = 1

class GameGuideImageCategoryEnum(IntEnum):
	None_ = -1
	Item = 0
	Challenge = 1
	Emote = 2
	GuildEmblemBackground = 3
	GuildEmblemSymbol = 4
	GuildRank = 5
	Achievement = 7
	OrnamentIcon = 8
	Ornament = 9
	CharacterCosmetics = 10
	Spell = 11
	SpellState = 12
	Smiley = 13
	BreedRole = 15
	KoliLeague = 18
	KoliLeagueIllustration = 19
	TextIcon = 20
	Monster = 21
	Companion = 22
	Choices = 23
	GuideBook = 24
	ServerIllu = 25
	Suggestion = 26
	EmoteIdle = 27
	CharacterBody = 28
	Mount = 29

class GameGuideUi:
	class Category:
		class CategoryType(IntEnum):
			CtrCat = 0
			CtrSubCat = 1
			CtrSubSubCat = 2
			Unknown = 3

class GuideBookArticleEnum(IntEnum):
	Almanax = 17
	Event = 20
	TreasureHunt = 65
	Chat = 66
	DivineDimension = 120
	Kolossium = 140
	Smithmagic = 147
	InfiniteDream = 180
	KolossiumChart = 226
	KolossiumSurrender = 229
	KolossiumEventRules = 472
	InfiniteDreamTrial = 473

class GuideBookImageHorizontalAlignEnum(IntEnum):
	Left = 0
	Center = 1
	Right = 2

class GuideBookImageVerticalAlignEnum(IntEnum):
	Top = 0
	Bottom = 1

