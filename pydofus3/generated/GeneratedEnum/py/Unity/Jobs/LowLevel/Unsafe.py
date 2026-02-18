from enum import IntFlag

# Unity.Jobs.LowLevel.Unsafe.ScheduleMode
class ScheduleMode(IntFlag):
    Run = 0
    Batched = 1
    Parallel = 1
    Single = 2

