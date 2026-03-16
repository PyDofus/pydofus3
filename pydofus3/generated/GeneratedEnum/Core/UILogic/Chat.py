from enum import IntFlag

class ChatView:
	class ChatWidgetOptions(IntFlag):
		FontSmall = 1
		FontMedium = 2
		FontLarge = 4
		OpacityLow = 8
		OpacityMedium = 16
		OpacityHigh = 32
		Default = 34
		Extended = 64
		FontXLarge = 128
		BigChannels = 256

