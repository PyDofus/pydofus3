from enum import IntFlag

# Core.UILogic.SmithMagic.SmithMagicItemEffectLine
class SmithMagicItemEffectLine(IntFlag):
    neutral = 0
    bonus = 1
    malus = 2
    exo = 3
    over = 4
    missing = 5
    malusEffect = 6
    bonusEffect = 7

# Core.UILogic.SmithMagic.SmithMagicUi
class SmithMagicUi(IntFlag):
    Effect = 0
    Min = 1
    Max = 2
    Value = 3

