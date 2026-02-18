from enum import IntFlag

# Internal.Runtime.Augments.AsyncStatus
class AsyncStatus(IntFlag):
    Started = 0
    Completed = 1
    Canceled = 2
    Error = 3

