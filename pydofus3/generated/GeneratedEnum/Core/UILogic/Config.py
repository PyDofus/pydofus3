from enum import IntEnum

class OptionCategoryId(IntEnum):
	Default = -2
	None_ = -1
	Game = 0
	GameGeneral = 1
	GameFight = 2
	GameSocial = 3
	Ui = 4
	UiGeneral = 5
	UiMap = 6
	UiChat = 7
	Display = 8
	DisplayResolutions = 9
	DisplayAura = 10
	DisplayWorld = 11
	Sound = 12
	SoundGeneral = 13
	Accessibility = 14
	AccessibilityColor = 15
	AccessibilityText = 16
	AccessibilityIcons = 17
	Theme = 18
	ThemeColor = 19
	Notification = 20
	Support = 21
	SupportGeneral = 21
	SupportCache = 22
	DisplayGraphics = 23
	AccessibilityUiSize = 23
	ExternalNotificationMessage = 24
	ExternalNotificationFight = 25
	ExternalNotificationInvitation = 26
	ExternalNotificationKolizeum = 27
	ExternalNotificationOthers = 28
	InternalNotification = 29
	NotificationGeneral = 30
	InternalNotificationSuccessQuest = 31
	Common = 40
	Menu = 41
	Tooltip = 42
	Chat = 43
	Option = 44
	Fight = 45
	QuickSlot = 46
	Misc = 47
	SoundChat = 48
	SoundFight = 49

class OptionElementType(IntEnum):
	None_ = 0
	Slider = 1
	BigToggleTheme = 2
	BigToggleTexturesPack = 3
	Bool = 4
	Button = 5
	ChatColorSelection = 6
	ColorChoice = 7
	Divider = 8
	ExternalNotification = 9
	Label = 10
	MultipleChoice = 11
	Notification = 12
	Shortcut = 13
	TextButton = 14
	Sound = 15

class OptionTab(IntEnum):
	GeneralOptionTab = 0
	ShortCutOptionTab = 1

class OptionType(IntEnum):
	Boolean = 0
	MultipleChoice = 1
	ExternalNotification = 2
	Slider = 3
	ThemeSelection = 4
	TexturePackSelection = 5
	Button = 6
	TextButton = 7
	Divider = 8
	Notification = 9
	ChatColorSelection = 10
	Shortcut = 11
	ColorChoice = 12
	Label = 13
	Sound = 14

