from enum import IntFlag

# Thrift.Transport.TTransportException
class TTransportException(IntFlag):
    Unknown = 0
    NotOpen = 1
    AlreadyOpen = 2
    TimedOut = 3
    EndOfFile = 4
    Interrupted = 5

