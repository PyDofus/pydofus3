from enum import IntFlag

# DotNetty.Transport.Channels.Local.LocalChannel
class LocalChannel(IntFlag):
    Open = 0
    Bound = 1
    Connected = 2
    Closed = 3

