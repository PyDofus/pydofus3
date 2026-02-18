from enum import IntFlag

# DotNetty.Transport.Channels.AbstractChannelHandlerContext
class AbstractChannelHandlerContext(IntFlag):
    HandlerAdded = 1
    HandlerRemoved = 2
    ExceptionCaught = 4
    ChannelRegistered = 8
    ChannelUnregistered = 16
    ChannelActive = 32
    ChannelInactive = 64
    ChannelRead = 128
    ChannelReadComplete = 256
    ChannelWritabilityChanged = 512
    UserEventTriggered = 1024
    Bind = 2048
    Connect = 4096
    Disconnect = 8192
    Close = 16384
    Deregister = 32768
    Read = 65536
    Write = 131072
    Flush = 262144
    Inbound = 2044
    Outbound = 522240

# DotNetty.Transport.Channels.AbstractChannelHandlerContext
class AbstractChannelHandlerContext(IntFlag):
    Init = 0
    Added = 1
    Removed = 2

# DotNetty.Transport.Channels.AbstractChannelHandlerContext
class AbstractChannelHandlerContext(IntFlag):
    NoFlush = 0
    VoidFlush = 1
    Flush = 2

