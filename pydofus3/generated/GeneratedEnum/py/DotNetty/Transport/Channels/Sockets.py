from enum import IntFlag

# DotNetty.Transport.Channels.Sockets.AbstractSocketChannel
class AbstractSocketChannel(IntFlag):
    Open = 1
    ReadScheduled = 2
    WriteScheduled = 4
    Active = 8

