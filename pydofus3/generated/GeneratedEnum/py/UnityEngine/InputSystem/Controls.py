from enum import IntFlag

# UnityEngine.InputSystem.Controls.AxisControl
class AxisControl(IntFlag):
    NONE = 0
    BeforeNormalize = 1
    AfterNormalize = 2
    ToConstantBeforeNormalize = 3

# UnityEngine.InputSystem.Controls.DiscreteButtonControl
class DiscreteButtonControl(IntFlag):
    WriteDisabled = 0
    WriteNullAndMaxValue = 1

# UnityEngine.InputSystem.Controls.DpadControl
class DpadControl(IntFlag):
    Up = 0
    Down = 1
    Left = 2
    Right = 3

