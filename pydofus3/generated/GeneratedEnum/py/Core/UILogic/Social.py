from enum import IntFlag

# Core.UILogic.Social.AllianceNuggetValidPopup
class AllianceNuggetValidPopup(IntFlag):
    Amount = 0
    Name = 1

# Core.UILogic.Social.CollectedTaxCollectorUI
class CollectedTaxCollectorUI(IntFlag):
    Name = 0
    Quantity = 1
    AveragePrice = 2

# Core.UILogic.Social.FriendsUI
class FriendsUI(IntFlag):
    NONE = -1
    Ankama = 0
    Friend = 1
    Blocked = 2

# Core.UILogic.Social.SocialBaseUI
class SocialBaseUI(IntFlag):
    Friend = 0
    Guild = 1
    Alliance = 2

# Core.UILogic.Social.SocialGroupCardUI
class SocialGroupCardUI(IntFlag):
    Interest = 1
    Atmosphere = 2
    PlayTime = 3

# Core.UILogic.Social.SocialGroupCardUI
class SocialGroupCardUI(IntFlag):
    Name = 0
    Rank = 1
    Level = 2

# Core.UILogic.Social.SocialGroupCardUI
class SocialGroupCardUI(IntFlag):
    NONE = -1
    Presentation = 0
    Members = 1

# Core.UILogic.Social.SocialGroupCreatorUi
class SocialGroupCreatorUi(IntFlag):
    Creation = 0
    NameModification = 1
    EmblemModification = 2
    Modification = 3

# Core.UILogic.Social.SocialGroupCreatorUi
class SocialGroupCreatorUi(IntFlag):
    Undefined = -1
    Backgrounds = 0
    Icons = 1

# Core.UILogic.Social.SocialMembersSortEnum
class SocialMembersSortEnum(IntFlag):
    NONE = 0
    SortByStatus = 1
    SortByName = 2
    SortByRank = 3
    SortByLevel = 4
    SortByBreed = 5
    SortBySuccess = 6
    SortByKohRole = 7
    SortByNuggets = 8

# Core.UILogic.Social.SocialRecruitmentUI
class SocialRecruitmentUI(IntFlag):
    Interest = 1
    Atmosphere = 2
    PlayTime = 3

# Core.UILogic.Social.SocialRightsAndRanksUi
class SocialRightsAndRanksUi(IntFlag):
    Guild = 0
    Alliance = 1

# Core.UILogic.Social.SocialRightsAndRanksUi
class SocialRightsAndRanksUi(IntFlag):
    Select = 0
    UnSelect = 1

# Core.UILogic.Social.UserPresence
class UserPresence(IntFlag):
    Online = 0
    Offline = 1

# Core.UILogic.Social.UserStatus
class UserStatus(IntFlag):
    Available = 0
    Away = 1
    Busy = 2

