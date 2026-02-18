from enum import IntFlag

# Core.Wrappers.DataCenterWrappers.CalendarWrappers.CalendarEventStateType
class CalendarEventStateType(IntFlag):
    none = 0
    start = 1
    pending = 2
    end = 3

