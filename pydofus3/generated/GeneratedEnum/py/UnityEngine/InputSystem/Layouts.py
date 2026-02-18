from enum import IntFlag

# UnityEngine.InputSystem.Layouts.InputControlLayout
class InputControlLayout(IntFlag):
    isModifyingExistingControl = 1
    IsNoisy = 2
    IsSynthetic = 4
    IsFirstDefinedInThisLayout = 8
    DontReset = 16

# UnityEngine.InputSystem.Layouts.InputControlLayout
class InputControlLayout(IntFlag):
    IsGenericTypeOfDevice = 1
    HideInUI = 2
    IsOverride = 4
    CanRunInBackground = 8
    CanRunInBackgroundIsSet = 16
    IsNoisy = 32

