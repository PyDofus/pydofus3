from enum import IntFlag

# UnityEngine.InputSystem.Composites.AxisComposite
class AxisComposite(IntFlag):
    Neither = 0
    Positive = 1
    Negative = 2

# UnityEngine.InputSystem.Composites.ButtonWithOneModifier
class ButtonWithOneModifier(IntFlag):
    Default = 0
    Ordered = 1
    Unordered = 2

# UnityEngine.InputSystem.Composites.ButtonWithTwoModifiers
class ButtonWithTwoModifiers(IntFlag):
    Default = 0
    Ordered = 1
    Unordered = 2

# UnityEngine.InputSystem.Composites.OneModifierComposite
class OneModifierComposite(IntFlag):
    Default = 0
    Ordered = 1
    Unordered = 2

# UnityEngine.InputSystem.Composites.TwoModifiersComposite
class TwoModifiersComposite(IntFlag):
    Default = 0
    Ordered = 1
    Unordered = 2

# UnityEngine.InputSystem.Composites.Vector2Composite
class Vector2Composite(IntFlag):
    Analog = 2
    DigitalNormalized = 0
    Digital = 1

# UnityEngine.InputSystem.Composites.Vector3Composite
class Vector3Composite(IntFlag):
    Analog = 0
    DigitalNormalized = 1
    Digital = 2

