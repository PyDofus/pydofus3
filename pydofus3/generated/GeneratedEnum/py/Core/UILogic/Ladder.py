from enum import IntFlag

# Core.UILogic.Ladder.BaseLadderTabUI
class BaseLadderTabUI(IntFlag):
    Rank = 0
    Name = 1
    Breed = 2
    Server = 3
    Level = 4
    Rating = 5
    WinRate = 6
    Xp = 7
    AchievementPoints = 8
    Intensity = 9
    DreamPoints = 10

# Core.UILogic.Ladder.LadderUI
class LadderUI(IntFlag):
    Experience = 0
    Koli = 1
    Achievement = 2
    WorldEvents = 3
    InfiniteDream = 4

# Core.UILogic.Ladder.WorldEventsLadderTabUI
class WorldEventsLadderTabUI(IntFlag):
    Rank = 0
    Name = 1
    Level = 2
    Score = 3

