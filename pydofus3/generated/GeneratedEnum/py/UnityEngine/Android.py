from enum import IntFlag

# UnityEngine.Android.AndroidColorModeHdr
class AndroidColorModeHdr(IntFlag):
    Undefined = 0
    No = 4
    Yes = 8

# UnityEngine.Android.AndroidColorModeWideColorGamut
class AndroidColorModeWideColorGamut(IntFlag):
    Undefined = 0
    No = 1
    Yes = 2

# UnityEngine.Android.AndroidHardwareKeyboardHidden
class AndroidHardwareKeyboardHidden(IntFlag):
    Undefined = 0
    No = 1
    Yes = 2

# UnityEngine.Android.AndroidKeyboard
class AndroidKeyboard(IntFlag):
    Undefined = 0
    NoKeys = 1
    Qwerty = 2
    _12Key = 3

# UnityEngine.Android.AndroidKeyboardHidden
class AndroidKeyboardHidden(IntFlag):
    Undefined = 0
    No = 1
    Yes = 2

# UnityEngine.Android.AndroidNavigation
class AndroidNavigation(IntFlag):
    Undefined = 0
    NoNav = 1
    Dpad = 2
    TrackBall = 3
    Wheel = 4

# UnityEngine.Android.AndroidNavigationHidden
class AndroidNavigationHidden(IntFlag):
    Undefined = 0
    No = 1
    Yes = 2

# UnityEngine.Android.AndroidOrientation
class AndroidOrientation(IntFlag):
    Undefined = 0
    Portrait = 1
    Landscape = 2

# UnityEngine.Android.AndroidScreenLayoutDirection
class AndroidScreenLayoutDirection(IntFlag):
    LTR = 64
    RTL = 128

# UnityEngine.Android.AndroidScreenLayoutLong
class AndroidScreenLayoutLong(IntFlag):
    Undefined = 0
    No = 16
    Yes = 32

# UnityEngine.Android.AndroidScreenLayoutRound
class AndroidScreenLayoutRound(IntFlag):
    Undefined = 0
    No = 256
    Yes = 512

# UnityEngine.Android.AndroidScreenLayoutSize
class AndroidScreenLayoutSize(IntFlag):
    Undefined = 0
    Small = 1
    Normal = 2
    Large = 3
    XLarge = 4

# UnityEngine.Android.AndroidTouchScreen
class AndroidTouchScreen(IntFlag):
    Undefined = 0
    NoTouch = 1
    Finger = 3

# UnityEngine.Android.AndroidUIModeNight
class AndroidUIModeNight(IntFlag):
    Undefined = 0
    No = 16
    Yes = 32

# UnityEngine.Android.AndroidUIModeType
class AndroidUIModeType(IntFlag):
    Undefined = 0
    Normal = 1
    Desk = 2
    Car = 3
    Television = 4
    Appliance = 5
    Watch = 6
    VrHeadset = 7

