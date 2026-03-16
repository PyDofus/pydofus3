from enum import IntEnum

class AdministrablePopupButtonTypeEnum(IntEnum):
	MainButton = 0
	SecondaryButton = 1

class FeedUI:
	class FeedUIType(IntEnum):
		Pet = 0

	class FeedQuantityMode(IntEnum):
		SingleItem = 0
		SingleItemSingleQuantity = 1
		MultipleItems = 2

class WidgetManager:
	class UiWithHeaderMinimizable(IntEnum):
		BannerMenu = 0
		Buffs = 1
		TreasureHunt = 2
		Timeline = 3
		MiniMap = 4
		QuestList = 5
		ActionBar = 6
		Party = 7
		Challenges = 8
		Chat = 9
		Breach = 10
		CharacterInformations = 11
		Summons = 12
		Smiley = 13
		EndTurn = 14

