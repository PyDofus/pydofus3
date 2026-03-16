from enum import IntEnum
from enum import IntFlag

class AbstractChannelHandlerContext:
	class SkipFlags(IntFlag):
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
		Inbound = 2044
		Bind = 2048
		Connect = 4096
		Disconnect = 8192
		Close = 16384
		Deregister = 32768
		Read = 65536
		Write = 131072
		Flush = 262144
		Outbound = 522240

	class HandlerState(IntEnum):
		Init = 0
		Added = 1
		Removed = 2

	class FlushMode(IntEnum):
		NoFlush = 0
		VoidFlush = 1
		Flush = 2

