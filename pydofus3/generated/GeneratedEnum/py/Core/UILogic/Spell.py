from enum import IntFlag

# Core.UILogic.Spell.CommonSpellsList
class CommonSpellsList(IntFlag):
    Name = 0
    Equipped = 1

# Core.UILogic.Spell.ForgettableListBase
class ForgettableListBase(IntFlag):
    All = 0
    LearnedSpells = 1
    UnlearnedSpells = 2

# Core.UILogic.Spell.ModstersList
class ModstersList(IntFlag):
    Name = 0
    ActiveSpell = 1
    PassiveSpell = 2
    Equipped = 3

# Core.UILogic.Spell.ObtainingSpell
class ObtainingSpell(IntFlag):
    Droppable = 0
    Craftable = 1
    InQuest = 2
    Unkown = 3

# Core.UILogic.Spell.SpellList
class SpellList(IntFlag):
    Damages = 3
    Air = 4
    Fire = 5
    Water = 6
    Earth = 7
    Neutral = 8
    MultiElement = 9
    Protection = 10
    Heal = 11
    Malus = 12
    Bonus = 13
    Placement = 14
    Summons = 15
    Special = 16

