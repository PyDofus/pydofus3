from enum import IntFlag

class AudioSampleConsumer:
	class BusState(IntFlag):
		None_ = 0
		Locked = 1
		WaitingForStudioSystem = 2
		WaitingForChannelGroup = 4
		BusNotFound = 8
		ChannelGroupError = 16

class AudioSampleConsumerOptions(IntFlag):
	None_ = 0
	Spatialized = 1
	StallUntilBusIsLoaded = 2

