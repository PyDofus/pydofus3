from enum import IntFlag

# UnityEngine.Accessibility.AccessibilityNotification
class AccessibilityNotification(IntFlag):
    NONE = 0
    Announcement = 1
    AnnouncementFinished = 2
    ScreenReaderStatusChanged = 3
    ScreenChanged = 4
    LayoutChanged = 5
    PageScrolled = 6
    ElementFocused = 7
    ElementUnfocused = 8
    FontScaleChanged = 9
    BoldTextStatusChanged = 10
    ClosedCaptioningStatusChanged = 11

# UnityEngine.Accessibility.AccessibilityRole
class AccessibilityRole(IntFlag):
    NONE = 0
    Button = 1
    Image = 2
    StaticText = 4
    SearchField = 8
    KeyboardKey = 16
    Header = 32
    TabBar = 64
    Slider = 128
    Toggle = 256

# UnityEngine.Accessibility.AccessibilityState
class AccessibilityState(IntFlag):
    NONE = 0
    Disabled = 1
    Selected = 2

