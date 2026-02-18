from enum import IntFlag

# DotNetty.Handlers.Timeout.IdleState
class IdleState(IntFlag):
    ReaderIdle = 0
    WriterIdle = 1
    AllIdle = 2

