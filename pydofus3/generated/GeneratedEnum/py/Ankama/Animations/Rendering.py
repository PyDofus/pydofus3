from enum import IntFlag

# Ankama.Animations.Rendering.AnimationMaskType
class AnimationMaskType(IntFlag):
    NONE = 0
    Bounds = 1
    Symbol = 2

# Ankama.Animations.Rendering.BufferState
class BufferState(IntFlag):
    Ready = 0
    Running = 1
    Pending = 2

# Ankama.Animations.Rendering.FlashFilters
class FlashFilters(IntFlag):
    Blur = 0
    Glow = 1
    DropShadow = 2
    ColorMatrix = 3

# Ankama.Animations.Rendering.FlashMaskState
class FlashMaskState(IntFlag):
    NONE = 0
    SetMask = 1
    ObeyMask = 2
    ClearMask = 3

# Ankama.Animations.Rendering.PrepassTextureType
class PrepassTextureType(IntFlag):
    Collection = 0
    Individual = 1

# Ankama.Animations.Rendering.ShaderConstants
class ShaderConstants(IntFlag):
    CROSS_2_SIDES = 0
    CROSS_FROM_CENTER = 1
    CROSS_AROUND = 2
    OUTLINE_MASK = 3

# Ankama.Animations.Rendering.ShaderConstants
class ShaderConstants(IntFlag):
    DEFAULT = 1
    REFRACTION = 2
    INLINE = 4
    OUTLINE = 8
    WAVE = 16

