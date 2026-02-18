from enum import IntFlag

# Editor.AleCore.Data.ElementType
class ElementType(IntFlag):
    Normal = 0
    InteractiveBoundingBox = 1
    InteractiveTexture = 2
    Animated = 3
    ServerAnimated = 6

