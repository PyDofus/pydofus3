from enum import IntFlag

# Core.UILogic.Components.Tooltips.Components.ConditionsTooltipElement
class ConditionsTooltipElement(IntFlag):
    BonusEffect = 0
    NeutralEffect = 1
    MalusEffect = 2

# Core.UILogic.Components.Tooltips.Components.EffectAndDamageTooltipBlock
class EffectAndDamageTooltipBlock(IntFlag):
    Effects = 0
    Damages = 1
    Status = 2

# Core.UILogic.Components.Tooltips.Components.EffectAndDamageTooltipBlock
class EffectAndDamageTooltipBlock(IntFlag):
    BonusEffect = 0
    MalusEffect = 1
    NeutralEffect = 2
    OverEffect = 3
    ExoticEffect = 4
    TheoreticalEffect = 5

