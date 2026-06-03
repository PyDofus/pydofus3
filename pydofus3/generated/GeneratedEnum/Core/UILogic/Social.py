from enum import IntEnum

class AllianceNuggetValidPopup:
	class SortType(IntEnum):
		Amount = 0
		Name = 1

class CollectedTaxCollectorUI:
	class ItemsSortingType(IntEnum):
		Name = 0
		Quantity = 1
		AveragePrice = 2

class FriendsUI:
	class FriendTabEnum(IntEnum):
		None_ = -1
		Ankama = 0
		Friend = 1
		Blocked = 2

class SocialGroupCardUI:
	class TagType(IntEnum):
		Interest = 1
		Atmosphere = 2
		PlayTime = 3

	class MembersSortingTypeEnum(IntEnum):
		Name = 0
		Rank = 1
		Level = 2

	class CardTab(IntEnum):
		None_ = -1
		Presentation = 0
		Members = 1

class SocialGroupCreatorUi:
	class SocialGroupCreatorMode(IntEnum):
		Creation = 0
		NameModification = 1
		EmblemModification = 2
		Modification = 3

	class SocialGroupCreatorTab(IntEnum):
		Undefined = -1
		Backgrounds = 0
		Icons = 1

class SocialMembersSortEnum(IntEnum):
	None_ = 0
	SortByStatus = 1
	SortByName = 2
	SortByRank = 3
	SortByLevel = 4
	SortByBreed = 5
	SortBySuccess = 6
	SortByGuildatons = 7
	SortByKohRole = 8
	SortByNuggets = 9

class SocialRecruitmentUI:
	class TagType(IntEnum):
		Interest = 1
		Atmosphere = 2
		PlayTime = 3

class SocialRightsAndRanksUi:
	class RightsAndRanksTypeEnum(IntEnum):
		Guild = 0
		Alliance = 1

	class SelectAllEnum(IntEnum):
		Select = 0
		UnSelect = 1

class UserPresence(IntEnum):
	Online = 0
	Offline = 1

class UserStatus(IntEnum):
	Available = 0
	Away = 1
	Busy = 2

