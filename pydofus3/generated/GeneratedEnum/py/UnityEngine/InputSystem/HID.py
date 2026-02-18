from enum import IntFlag

# UnityEngine.InputSystem.HID.HIDParser
class HIDParser(IntFlag):
    Input = 128
    Output = 144
    Feature = 176
    Collection = 160
    EndCollection = 192
    UsagePage = 4
    LogicalMinimum = 20
    LogicalMaximum = 36
    PhysicalMinimum = 52
    PhysicalMaximum = 68
    UnitExponent = 84
    Unit = 100
    ReportSize = 116
    ReportID = 132
    ReportCount = 148
    Push = 164
    Pop = 180
    Usage = 8
    UsageMinimum = 24
    UsageMaximum = 40
    DesignatorIndex = 56
    DesignatorMinimum = 72
    DesignatorMaximum = 88
    StringIndex = 120
    StringMinimum = 136
    StringMaximum = 152
    Delimiter = 168

