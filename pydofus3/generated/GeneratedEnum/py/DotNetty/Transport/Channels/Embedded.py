from enum import IntFlag

# DotNetty.Transport.Channels.Embedded.EmbeddedChannel
class EmbeddedChannel(IntFlag):
    Open = 0
    Active = 1
    Closed = 2

# DotNetty.Transport.Channels.Embedded.SingleThreadedEmbeddedChannel
class SingleThreadedEmbeddedChannel(IntFlag):
    Open = 0
    Active = 1
    Closed = 2

