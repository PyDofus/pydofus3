from enum import IntFlag

# UnityEngine.InputSystem.Users.InputUser
class InputUser(IntFlag):
    BindToAllDevices = 1
    UserAccountSelectionInProgress = 2

# UnityEngine.InputSystem.Users.InputUserChange
class InputUserChange(IntFlag):
    Added = 0
    Removed = 1
    DevicePaired = 2
    DeviceUnpaired = 3
    DeviceLost = 4
    DeviceRegained = 5
    AccountChanged = 6
    AccountNameChanged = 7
    AccountSelectionInProgress = 8
    AccountSelectionCanceled = 9
    AccountSelectionComplete = 10
    ControlSchemeChanged = 11
    ControlsChanged = 12

# UnityEngine.InputSystem.Users.InputUserPairingOptions
class InputUserPairingOptions(IntFlag):
    NONE = 0
    ForcePlatformUserAccountSelection = 1
    ForceNoPlatformUserAccountSelection = 2
    UnpairCurrentDevicesFromUser = 8

