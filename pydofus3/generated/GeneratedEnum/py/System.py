from enum import IntFlag

# System.AppContext
class AppContext(IntFlag):
    HasFalseValue = 1
    HasTrueValue = 2
    HasLookedForOverride = 4
    UnknownValue = 8

# System.AttributeTargets
class AttributeTargets(IntFlag):
    Assembly = 1
    Module = 2
    Class = 4
    Struct = 8
    Enum = 16
    Constructor = 32
    Method = 64
    Property = 128
    Field = 256
    Event = 512
    Interface = 1024
    Parameter = 2048
    Delegate = 4096
    ReturnValue = 8192
    GenericParameter = 16384
    All = 32767

# System.Base64FormattingOptions
class Base64FormattingOptions(IntFlag):
    NONE = 0
    InsertLineBreaks = 1

# System.ByteEnum
class ByteEnum(IntFlag):

# System.ConsoleColor
class ConsoleColor(IntFlag):
    Black = 0
    DarkBlue = 1
    DarkGreen = 2
    DarkCyan = 3
    DarkRed = 4
    DarkMagenta = 5
    DarkYellow = 6
    Gray = 7
    DarkGray = 8
    Blue = 9
    Green = 10
    Cyan = 11
    Red = 12
    Magenta = 13
    Yellow = 14
    White = 15

# System.ConsoleKey
class ConsoleKey(IntFlag):
    Backspace = 8
    Tab = 9
    Clear = 12
    Enter = 13
    Pause = 19
    Escape = 27
    Spacebar = 32
    PageUp = 33
    PageDown = 34
    End = 35
    Home = 36
    LeftArrow = 37
    UpArrow = 38
    RightArrow = 39
    DownArrow = 40
    Select = 41
    Print = 42
    Execute = 43
    PrintScreen = 44
    Insert = 45
    Delete = 46
    Help = 47
    D0 = 48
    D1 = 49
    D2 = 50
    D3 = 51
    D4 = 52
    D5 = 53
    D6 = 54
    D7 = 55
    D8 = 56
    D9 = 57
    A = 65
    B = 66
    C = 67
    D = 68
    E = 69
    F = 70
    G = 71
    H = 72
    I = 73
    J = 74
    K = 75
    L = 76
    M = 77
    N = 78
    O = 79
    P = 80
    Q = 81
    R = 82
    S = 83
    T = 84
    U = 85
    V = 86
    W = 87
    X = 88
    Y = 89
    Z = 90
    LeftWindows = 91
    RightWindows = 92
    Applications = 93
    Sleep = 95
    NumPad0 = 96
    NumPad1 = 97
    NumPad2 = 98
    NumPad3 = 99
    NumPad4 = 100
    NumPad5 = 101
    NumPad6 = 102
    NumPad7 = 103
    NumPad8 = 104
    NumPad9 = 105
    Multiply = 106
    Add = 107
    Separator = 108
    Subtract = 109
    Decimal = 110
    Divide = 111
    F1 = 112
    F2 = 113
    F3 = 114
    F4 = 115
    F5 = 116
    F6 = 117
    F7 = 118
    F8 = 119
    F9 = 120
    F10 = 121
    F11 = 122
    F12 = 123
    F13 = 124
    F14 = 125
    F15 = 126
    F16 = 127
    F17 = 128
    F18 = 129
    F19 = 130
    F20 = 131
    F21 = 132
    F22 = 133
    F23 = 134
    F24 = 135
    BrowserBack = 166
    BrowserForward = 167
    BrowserRefresh = 168
    BrowserStop = 169
    BrowserSearch = 170
    BrowserFavorites = 171
    BrowserHome = 172
    VolumeMute = 173
    VolumeDown = 174
    VolumeUp = 175
    MediaNext = 176
    MediaPrevious = 177
    MediaStop = 178
    MediaPlay = 179
    LaunchMail = 180
    LaunchMediaSelect = 181
    LaunchApp1 = 182
    LaunchApp2 = 183
    Oem1 = 186
    OemPlus = 187
    OemComma = 188
    OemMinus = 189
    OemPeriod = 190
    Oem2 = 191
    Oem3 = 192
    Oem4 = 219
    Oem5 = 220
    Oem6 = 221
    Oem7 = 222
    Oem8 = 223
    Oem102 = 226
    Process = 229
    Packet = 231
    Attention = 246
    CrSel = 247
    ExSel = 248
    EraseEndOfFile = 249
    Play = 250
    Zoom = 251
    NoName = 252
    Pa1 = 253
    OemClear = 254

# System.ConsoleModifiers
class ConsoleModifiers(IntFlag):
    Alt = 1
    Shift = 2
    Control = 4

# System.ConsoleSpecialKey
class ConsoleSpecialKey(IntFlag):
    ControlC = 0
    ControlBreak = 1

# System.DTSubStringType
class DTSubStringType(IntFlag):
    Unknown = 0
    Invalid = 1
    Number = 2
    End = 3
    Other = 4

# System.DateTimeKind
class DateTimeKind(IntFlag):
    Unspecified = 0
    Utc = 1
    Local = 2

# System.DateTimeParse
class DateTimeParse(IntFlag):
    End = 0
    NumEnd = 1
    NumAmpm = 2
    NumSpace = 3
    NumDatesep = 4
    NumTimesep = 5
    MonthEnd = 6
    MonthSpace = 7
    MonthDatesep = 8
    NumDatesuff = 9
    NumTimesuff = 10
    DayOfWeek = 11
    YearSpace = 12
    YearDateSep = 13
    YearEnd = 14
    TimeZone = 15
    Era = 16
    NumUTCTimeMark = 17
    Unk = 18
    NumLocalTimeMark = 19
    Max = 20

# System.DateTimeParse
class DateTimeParse(IntFlag):
    NotSet = -1
    AM = 0
    PM = 1

# System.DateTimeParse
class DateTimeParse(IntFlag):
    BEGIN = 0
    N = 1
    NN = 2
    D_Nd = 3
    D_NN = 4
    D_NNd = 5
    D_M = 6
    D_MN = 7
    D_NM = 8
    D_MNd = 9
    D_NDS = 10
    D_Y = 11
    D_YN = 12
    D_YNd = 13
    D_YM = 14
    D_YMd = 15
    D_S = 16
    T_S = 17
    T_Nt = 18
    T_NNt = 19
    ERROR = 20
    DX_NN = 21
    DX_NNN = 22
    DX_MN = 23
    DX_NM = 24
    DX_MNN = 25
    DX_DS = 26
    DX_DSN = 27
    DX_NDS = 28
    DX_NNDS = 29
    DX_YNN = 30
    DX_YMN = 31
    DX_YN = 32
    DX_YM = 33
    TX_N = 34
    TX_NN = 35
    TX_NNN = 36
    TX_TS = 37
    DX_NNY = 38

# System.DayOfWeek
class DayOfWeek(IntFlag):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6

# System.Decimal
class Decimal(IntFlag):
    ToEven = 0
    AwayFromZero = 1
    Truncate = 2
    Floor = 3
    Ceiling = 4

# System.DefaultBinder
class DefaultBinder(IntFlag):
    Boolean = 8
    Char = 16
    SByte = 32
    Byte = 64
    Int16 = 128
    UInt16 = 256
    Int32 = 512
    UInt32 = 1024
    Int64 = 2048
    UInt64 = 4096
    Single = 8192
    Double = 16384
    Decimal = 32768
    DateTime = 65536
    String = 262144

# System.Enum
class Enum(IntFlag):
    NONE = 0
    Argument = 1
    ArgumentNull = 2
    ArgumentWithParameter = 3
    UnhandledException = 4

# System.Environment
class Environment(IntFlag):
    MyDocuments = 5
    Desktop = 0
    MyComputer = 17
    Programs = 2
    Personal = 5
    Favorites = 6
    Startup = 7
    Recent = 8
    SendTo = 9
    StartMenu = 11
    MyMusic = 13
    DesktopDirectory = 16
    Templates = 21
    ApplicationData = 26
    LocalApplicationData = 28
    InternetCache = 32
    Cookies = 33
    History = 34
    CommonApplicationData = 35
    System = 37
    ProgramFiles = 38
    MyPictures = 39
    CommonProgramFiles = 43
    MyVideos = 14
    NetworkShortcuts = 19
    Fonts = 20
    CommonStartMenu = 22
    CommonPrograms = 23
    CommonStartup = 24
    CommonDesktopDirectory = 25
    PrinterShortcuts = 27
    Windows = 36
    UserProfile = 40
    SystemX86 = 41
    ProgramFilesX86 = 42
    CommonProgramFilesX86 = 44
    CommonTemplates = 45
    CommonDocuments = 46
    CommonAdminTools = 47
    AdminTools = 48
    CommonMusic = 53
    CommonPictures = 54
    CommonVideos = 55
    Resources = 56
    LocalizedResources = 57
    CommonOemLinks = 58
    CDBurning = 59

# System.Environment
class Environment(IntFlag):
    NONE = 0
    DoNotVerify = 16384
    Create = 32768

# System.Exception
class Exception(IntFlag):
    ThreadAbort = 1
    ThreadInterrupted = 2
    OutOfMemory = 3

# System.ExceptionArgument
class ExceptionArgument(IntFlag):
    obj = 0
    dictionary = 1
    dictionaryCreationThreshold = 2
    array = 3
    info = 4
    key = 5
    collection = 6
    list = 7
    match = 8
    converter = 9
    queue = 10
    stack = 11
    capacity = 12
    index = 13
    startIndex = 14
    value = 15
    count = 16
    arrayIndex = 17
    name = 18
    mode = 19
    item = 20
    options = 21
    view = 22
    sourceBytesToCopy = 23
    start = 24
    pointer = 25
    ownedMemory = 26
    text = 27
    length = 28
    comparer = 29
    comparable = 30
    exceptions = 31
    exception = 32
    action = 33
    comparison = 34
    startSegment = 35
    endSegment = 36
    endIndex = 37
    task = 38
    source = 39
    state = 40
    culture = 41
    destination = 42
    byteOffset = 43
    minimumBufferSize = 44
    offset = 45
    values = 46
    comparisonType = 47
    s = 48
    input = 49
    format = 50

# System.ExceptionArgument
class ExceptionArgument(IntFlag):
    length = 0
    start = 1
    minimumBufferSize = 2
    elementIndex = 3
    comparable = 4
    comparer = 5
    destination = 6
    offset = 7
    startSegment = 8
    endSegment = 9
    startIndex = 10
    endIndex = 11
    array = 12
    culture = 13
    manager = 14

# System.ExceptionArgument
class ExceptionArgument(IntFlag):
    task = 0
    source = 1
    state = 2

# System.ExceptionResource
class ExceptionResource(IntFlag):
    Argument_ImplementIComparable = 0
    Argument_InvalidType = 1
    Argument_InvalidArgumentForComparison = 2
    Argument_InvalidRegistryKeyPermissionCheck = 3
    ArgumentOutOfRange_NeedNonNegNum = 4
    Arg_ArrayPlusOffTooSmall = 5
    Arg_NonZeroLowerBound = 6
    Arg_RankMultiDimNotSupported = 7
    Arg_RegKeyDelHive = 8
    Arg_RegKeyStrLenBug = 9
    Arg_RegSetStrArrNull = 10
    Arg_RegSetMismatchedKind = 11
    Arg_RegSubKeyAbsent = 12
    Arg_RegSubKeyValueAbsent = 13
    Argument_AddingDuplicate = 14
    Serialization_InvalidOnDeser = 15
    Serialization_MissingKeys = 16
    Serialization_NullKey = 17
    Argument_InvalidArrayType = 18
    NotSupported_KeyCollectionSet = 19
    NotSupported_ValueCollectionSet = 20
    ArgumentOutOfRange_SmallCapacity = 21
    ArgumentOutOfRange_Index = 22
    Argument_InvalidOffLen = 23
    Argument_ItemNotExist = 24
    ArgumentOutOfRange_Count = 25
    ArgumentOutOfRange_InvalidThreshold = 26
    ArgumentOutOfRange_ListInsert = 27
    NotSupported_ReadOnlyCollection = 28
    InvalidOperation_CannotRemoveFromStackOrQueue = 29
    InvalidOperation_EmptyQueue = 30
    InvalidOperation_EnumOpCantHappen = 31
    InvalidOperation_EnumFailedVersion = 32
    InvalidOperation_EmptyStack = 33
    ArgumentOutOfRange_BiggerThanCollection = 34
    InvalidOperation_EnumNotStarted = 35
    InvalidOperation_EnumEnded = 36
    NotSupported_SortedListNestedWrite = 37
    InvalidOperation_NoValue = 38
    InvalidOperation_RegRemoveSubKey = 39
    Security_RegistryPermission = 40
    UnauthorizedAccess_RegistryNoWrite = 41
    ObjectDisposed_RegKeyClosed = 42
    NotSupported_InComparableType = 43
    Argument_InvalidRegistryOptionsCheck = 44
    Argument_InvalidRegistryViewCheck = 45
    TaskT_TransitionToFinal_AlreadyCompleted = 46
    TaskCompletionSourceT_TrySetException_NullException = 47
    TaskCompletionSourceT_TrySetException_NoExceptions = 48
    NotSupported_StringComparison = 49
    InvalidOperation_NullArray = 50

# System.GCCollectionMode
class GCCollectionMode(IntFlag):
    Default = 0
    Forced = 1
    Optimized = 2

# System.Guid
class Guid(IntFlag):
    NONE = 0
    AllowParenthesis = 1
    AllowBraces = 2
    AllowDashes = 4
    AllowHexPrefix = 8
    RequireParenthesis = 16
    RequireBraces = 32
    RequireDashes = 64
    RequireHexPrefix = 128
    HexFormat = 160
    NumberFormat = 0
    DigitFormat = 64
    BraceFormat = 96
    ParenthesisFormat = 80
    Any = 15

# System.Guid
class Guid(IntFlag):
    NONE = 0
    All = 1
    AllButOverflow = 2

# System.Guid
class Guid(IntFlag):
    NONE = 0
    ArgumentNull = 1
    Format = 2
    FormatWithParameter = 3
    NativeException = 4
    FormatWithInnerException = 5

# System.Handles
class Handles(IntFlag):
    STD_INPUT = -10
    STD_OUTPUT = -11
    STD_ERROR = -12

# System.HexConverter
class HexConverter(IntFlag):
    Upper = 0
    Lower = 8224

# System.HexConverter
class HexConverter(IntFlag):
    Upper = 0
    Lower = 8224

# System.IOOperation
class IOOperation(IntFlag):
    Read = 1
    Write = 2

# System.Int16Enum
class Int16Enum(IntFlag):

# System.Int32Enum
class Int32Enum(IntFlag):

# System.Int64Enum
class Int64Enum(IntFlag):

# System.LazyState
class LazyState(IntFlag):
    NoneViaConstructor = 0
    NoneViaFactory = 1
    NoneException = 2
    PublicationOnlyViaConstructor = 3
    PublicationOnlyViaFactory = 4
    PublicationOnlyWait = 5
    PublicationOnlyException = 6
    ExecutionAndPublicationViaConstructor = 7
    ExecutionAndPublicationViaFactory = 8
    ExecutionAndPublicationException = 9

# System.MidpointRounding
class MidpointRounding(IntFlag):
    ToEven = 0
    AwayFromZero = 1

# System.ParseFailureKind
class ParseFailureKind(IntFlag):
    NONE = 0
    ArgumentNull = 1
    Format = 2
    FormatWithParameter = 3
    FormatWithOriginalDateTime = 4
    FormatWithFormatSpecifier = 5
    FormatWithOriginalDateTimeAndParameter = 6
    FormatBadDateTimeCalendar = 7

# System.ParseFlags
class ParseFlags(IntFlag):
    HaveYear = 1
    HaveMonth = 2
    HaveDay = 4
    HaveHour = 8
    HaveMinute = 16
    HaveSecond = 32
    HaveTime = 64
    HaveDate = 128
    TimeZoneUsed = 256
    TimeZoneUtc = 512
    ParsedMonthName = 1024
    CaptureOffset = 2048
    YearDefault = 4096
    Rfc1123Pattern = 8192
    UtcSortPattern = 16384

# System.ParsingError
class ParsingError(IntFlag):
    NONE = 0
    BadFormat = 1
    BadScheme = 2
    BadAuthority = 3
    EmptyUriString = 4
    LastRelativeUriOkErrIndex = 4
    SchemeLimit = 5
    SizeLimit = 6
    MustRootedPath = 7
    BadHostName = 8
    NonEmptyHost = 9
    BadPort = 10
    BadAuthorityTerminator = 11
    CannotCreateRelative = 12

# System.PlatformID
class PlatformID(IntFlag):
    Win32S = 0
    Win32Windows = 1
    Win32NT = 2
    WinCE = 3
    Unix = 4
    Xbox = 5
    MacOSX = 6

# System.RuntimeType
class RuntimeType(IntFlag):
    All = 0
    CaseSensitive = 1
    CaseInsensitive = 2
    HandleToInfo = 3

# System.SByteEnum
class SByteEnum(IntFlag):

# System.StringComparison
class StringComparison(IntFlag):
    CurrentCulture = 0
    CurrentCultureIgnoreCase = 1
    InvariantCulture = 2
    InvariantCultureIgnoreCase = 3
    Ordinal = 4
    OrdinalIgnoreCase = 5

# System.StringSplitOptions
class StringSplitOptions(IntFlag):
    NONE = 0
    RemoveEmptyEntries = 1

# System.TermInfoNumbers
class TermInfoNumbers(IntFlag):
    Columns = 0
    InitTabs = 1
    Lines = 2
    LinesOfMemory = 3
    MagicCookieGlitch = 4
    PaddingBaudRate = 5
    VirtualTerminal = 6
    WidthStatusLine = 7
    NumLabels = 8
    LabelHeight = 9
    LabelWidth = 10
    MaxAttributes = 11
    MaximumWindows = 12
    MaxColors = 13
    MaxPairs = 14
    NoColorVideo = 15
    BufferCapacity = 16
    DotVertSpacing = 17
    DotHorzSpacing = 18
    MaxMicroAddress = 19
    MaxMicroJump = 20
    MicroColSize = 21
    MicroLineSize = 22
    NumberOfPins = 23
    OutputResChar = 24
    OutputResLine = 25
    OutputResHorzInch = 26
    OutputResVertInch = 27
    PrintRate = 28
    WideCharSize = 29
    Buttons = 30
    BitImageEntwining = 31
    BitImageType = 32
    Last = 33

# System.TermInfoStrings
class TermInfoStrings(IntFlag):
    BackTab = 0
    Bell = 1
    CarriageReturn = 2
    ChangeScrollRegion = 3
    ClearAllTabs = 4
    ClearScreen = 5
    ClrEol = 6
    ClrEos = 7
    ColumnAddress = 8
    CommandCharacter = 9
    CursorAddress = 10
    CursorDown = 11
    CursorHome = 12
    CursorInvisible = 13
    CursorLeft = 14
    CursorMemAddress = 15
    CursorNormal = 16
    CursorRight = 17
    CursorToLl = 18
    CursorUp = 19
    CursorVisible = 20
    DeleteCharacter = 21
    DeleteLine = 22
    DisStatusLine = 23
    DownHalfLine = 24
    EnterAltCharsetMode = 25
    EnterBlinkMode = 26
    EnterBoldMode = 27
    EnterCaMode = 28
    EnterDeleteMode = 29
    EnterDimMode = 30
    EnterInsertMode = 31
    EnterSecureMode = 32
    EnterProtectedMode = 33
    EnterReverseMode = 34
    EnterStandoutMode = 35
    EnterUnderlineMode = 36
    EraseChars = 37
    ExitAltCharsetMode = 38
    ExitAttributeMode = 39
    ExitCaMode = 40
    ExitDeleteMode = 41
    ExitInsertMode = 42
    ExitStandoutMode = 43
    ExitUnderlineMode = 44
    FlashScreen = 45
    FormFeed = 46
    FromStatusLine = 47
    Init1string = 48
    Init2string = 49
    Init3string = 50
    InitFile = 51
    InsertCharacter = 52
    InsertLine = 53
    InsertPadding = 54
    KeyBackspace = 55
    KeyCatab = 56
    KeyClear = 57
    KeyCtab = 58
    KeyDc = 59
    KeyDl = 60
    KeyDown = 61
    KeyEic = 62
    KeyEol = 63
    KeyEos = 64
    KeyF0 = 65
    KeyF1 = 66
    KeyF10 = 67
    KeyF2 = 68
    KeyF3 = 69
    KeyF4 = 70
    KeyF5 = 71
    KeyF6 = 72
    KeyF7 = 73
    KeyF8 = 74
    KeyF9 = 75
    KeyHome = 76
    KeyIc = 77
    KeyIl = 78
    KeyLeft = 79
    KeyLl = 80
    KeyNpage = 81
    KeyPpage = 82
    KeyRight = 83
    KeySf = 84
    KeySr = 85
    KeyStab = 86
    KeyUp = 87
    KeypadLocal = 88
    KeypadXmit = 89
    LabF0 = 90
    LabF1 = 91
    LabF10 = 92
    LabF2 = 93
    LabF3 = 94
    LabF4 = 95
    LabF5 = 96
    LabF6 = 97
    LabF7 = 98
    LabF8 = 99
    LabF9 = 100
    MetaOff = 101
    MetaOn = 102
    Newline = 103
    PadChar = 104
    ParmDch = 105
    ParmDeleteLine = 106
    ParmDownCursor = 107
    ParmIch = 108
    ParmIndex = 109
    ParmInsertLine = 110
    ParmLeftCursor = 111
    ParmRightCursor = 112
    ParmRindex = 113
    ParmUpCursor = 114
    PkeyKey = 115
    PkeyLocal = 116
    PkeyXmit = 117
    PrintScreen = 118
    PrtrOff = 119
    PrtrOn = 120
    RepeatChar = 121
    Reset1string = 122
    Reset2string = 123
    Reset3string = 124
    ResetFile = 125
    RestoreCursor = 126
    RowAddress = 127
    SaveCursor = 128
    ScrollForward = 129
    ScrollReverse = 130
    SetAttributes = 131
    SetTab = 132
    SetWindow = 133
    Tab = 134
    ToStatusLine = 135
    UnderlineChar = 136
    UpHalfLine = 137
    InitProg = 138
    KeyA1 = 139
    KeyA3 = 140
    KeyB2 = 141
    KeyC1 = 142
    KeyC3 = 143
    PrtrNon = 144
    CharPadding = 145
    AcsChars = 146
    PlabNorm = 147
    KeyBtab = 148
    EnterXonMode = 149
    ExitXonMode = 150
    EnterAmMode = 151
    ExitAmMode = 152
    XonCharacter = 153
    XoffCharacter = 154
    EnaAcs = 155
    LabelOn = 156
    LabelOff = 157
    KeyBeg = 158
    KeyCancel = 159
    KeyClose = 160
    KeyCommand = 161
    KeyCopy = 162
    KeyCreate = 163
    KeyEnd = 164
    KeyEnter = 165
    KeyExit = 166
    KeyFind = 167
    KeyHelp = 168
    KeyMark = 169
    KeyMessage = 170
    KeyMove = 171
    KeyNext = 172
    KeyOpen = 173
    KeyOptions = 174
    KeyPrevious = 175
    KeyPrint = 176
    KeyRedo = 177
    KeyReference = 178
    KeyRefresh = 179
    KeyReplace = 180
    KeyRestart = 181
    KeyResume = 182
    KeySave = 183
    KeySuspend = 184
    KeyUndo = 185
    KeySbeg = 186
    KeyScancel = 187
    KeyScommand = 188
    KeyScopy = 189
    KeyScreate = 190
    KeySdc = 191
    KeySdl = 192
    KeySelect = 193
    KeySend = 194
    KeySeol = 195
    KeySexit = 196
    KeySfind = 197
    KeyShelp = 198
    KeyShome = 199
    KeySic = 200
    KeySleft = 201
    KeySmessage = 202
    KeySmove = 203
    KeySnext = 204
    KeySoptions = 205
    KeySprevious = 206
    KeySprint = 207
    KeySredo = 208
    KeySreplace = 209
    KeySright = 210
    KeySrsume = 211
    KeySsave = 212
    KeySsuspend = 213
    KeySundo = 214
    ReqForInput = 215
    KeyF11 = 216
    KeyF12 = 217
    KeyF13 = 218
    KeyF14 = 219
    KeyF15 = 220
    KeyF16 = 221
    KeyF17 = 222
    KeyF18 = 223
    KeyF19 = 224
    KeyF20 = 225
    KeyF21 = 226
    KeyF22 = 227
    KeyF23 = 228
    KeyF24 = 229
    KeyF25 = 230
    KeyF26 = 231
    KeyF27 = 232
    KeyF28 = 233
    KeyF29 = 234
    KeyF30 = 235
    KeyF31 = 236
    KeyF32 = 237
    KeyF33 = 238
    KeyF34 = 239
    KeyF35 = 240
    KeyF36 = 241
    KeyF37 = 242
    KeyF38 = 243
    KeyF39 = 244
    KeyF40 = 245
    KeyF41 = 246
    KeyF42 = 247
    KeyF43 = 248
    KeyF44 = 249
    KeyF45 = 250
    KeyF46 = 251
    KeyF47 = 252
    KeyF48 = 253
    KeyF49 = 254
    KeyF50 = 255
    KeyF51 = 256
    KeyF52 = 257
    KeyF53 = 258
    KeyF54 = 259
    KeyF55 = 260
    KeyF56 = 261
    KeyF57 = 262
    KeyF58 = 263
    KeyF59 = 264
    KeyF60 = 265
    KeyF61 = 266
    KeyF62 = 267
    KeyF63 = 268
    ClrBol = 269
    ClearMargins = 270
    SetLeftMargin = 271
    SetRightMargin = 272
    LabelFormat = 273
    SetClock = 274
    DisplayClock = 275
    RemoveClock = 276
    CreateWindow = 277
    GotoWindow = 278
    Hangup = 279
    DialPhone = 280
    QuickDial = 281
    Tone = 282
    Pulse = 283
    FlashHook = 284
    FixedPause = 285
    WaitTone = 286
    User0 = 287
    User1 = 288
    User2 = 289
    User3 = 290
    User4 = 291
    User5 = 292
    User6 = 293
    User7 = 294
    User8 = 295
    User9 = 296
    OrigPair = 297
    OrigColors = 298
    InitializeColor = 299
    InitializePair = 300
    SetColorPair = 301
    SetForeground = 302
    SetBackground = 303
    ChangeCharPitch = 304
    ChangeLinePitch = 305
    ChangeResHorz = 306
    ChangeResVert = 307
    DefineChar = 308
    EnterDoublewideMode = 309
    EnterDraftQuality = 310
    EnterItalicsMode = 311
    EnterLeftwardMode = 312
    EnterMicroMode = 313
    EnterNearLetterQuality = 314
    EnterNormalQuality = 315
    EnterShadowMode = 316
    EnterSubscriptMode = 317
    EnterSuperscriptMode = 318
    EnterUpwardMode = 319
    ExitDoublewideMode = 320
    ExitItalicsMode = 321
    ExitLeftwardMode = 322
    ExitMicroMode = 323
    ExitShadowMode = 324
    ExitSubscriptMode = 325
    ExitSuperscriptMode = 326
    ExitUpwardMode = 327
    MicroColumnAddress = 328
    MicroDown = 329
    MicroLeft = 330
    MicroRight = 331
    MicroRowAddress = 332
    MicroUp = 333
    OrderOfPins = 334
    ParmDownMicro = 335
    ParmLeftMicro = 336
    ParmRightMicro = 337
    ParmUpMicro = 338
    SelectCharSet = 339
    SetBottomMargin = 340
    SetBottomMarginParm = 341
    SetLeftMarginParm = 342
    SetRightMarginParm = 343
    SetTopMargin = 344
    SetTopMarginParm = 345
    StartBitImage = 346
    StartCharSetDef = 347
    StopBitImage = 348
    StopCharSetDef = 349
    SubscriptCharacters = 350
    SuperscriptCharacters = 351
    TheseCauseCr = 352
    ZeroMotion = 353
    CharSetNames = 354
    KeyMouse = 355
    MouseInfo = 356
    ReqMousePos = 357
    GetMouse = 358
    SetAForeground = 359
    SetABackground = 360
    PkeyPlab = 361
    DeviceType = 362
    CodeSetInit = 363
    Set0DesSeq = 364
    Set1DesSeq = 365
    Set2DesSeq = 366
    Set3DesSeq = 367
    SetLrMargin = 368
    SetTbMargin = 369
    BitImageRepeat = 370
    BitImageNewline = 371
    BitImageCarriageReturn = 372
    ColorNames = 373
    DefineBitImageRegion = 374
    EndBitImageRegion = 375
    SetColorBand = 376
    SetPageLength = 377
    DisplayPcChar = 378
    EnterPcCharsetMode = 379
    ExitPcCharsetMode = 380
    EnterScancodeMode = 381
    ExitScancodeMode = 382
    PcTermOptions = 383
    ScancodeEscape = 384
    AltScancodeEsc = 385
    EnterHorizontalHlMode = 386
    EnterLeftHlMode = 387
    EnterLowHlMode = 388
    EnterRightHlMode = 389
    EnterTopHlMode = 390
    EnterVerticalHlMode = 391
    SetAAttributes = 392
    SetPglenInch = 393
    Last = 394

# System.TimeZoneInfo
class TimeZoneInfo(IntFlag):
    Success = 0
    TimeZoneNotFoundException = 1
    InvalidTimeZoneException = 2
    SecurityException = 3

# System.TimeZoneInfoOptions
class TimeZoneInfoOptions(IntFlag):
    NONE = 1
    NoThrowOnInvalidTime = 2

# System.TokenType
class TokenType(IntFlag):
    NumberToken = 1
    YearNumberToken = 2
    Am = 3
    Pm = 4
    MonthToken = 5
    EndOfString = 6
    DayOfWeekToken = 7
    TimeZoneToken = 8
    EraToken = 9
    DateWordToken = 10
    UnknownToken = 11
    HebrewNumber = 12
    JapaneseEraToken = 13
    TEraToken = 14
    IgnorableSymbol = 15
    SEP_Unk = 256
    SEP_End = 512
    SEP_Space = 768
    SEP_Am = 1024
    SEP_Pm = 1280
    SEP_Date = 1536
    SEP_Time = 1792
    SEP_YearSuff = 2048
    SEP_MonthSuff = 2304
    SEP_DaySuff = 2560
    SEP_HourSuff = 2816
    SEP_MinuteSuff = 3072
    SEP_SecondSuff = 3328
    SEP_LocalTimeMark = 3584
    SEP_DateOrOffset = 3840
    RegularTokenMask = 255
    SeparatorTokenMask = 65280

# System.TypeCode
class TypeCode(IntFlag):
    Empty = 0
    Object = 1
    DBNull = 2
    Boolean = 3
    Char = 4
    SByte = 5
    Byte = 6
    Int16 = 7
    UInt16 = 8
    Int32 = 9
    UInt32 = 10
    Int64 = 11
    UInt64 = 12
    Single = 13
    Double = 14
    Decimal = 15
    DateTime = 16
    String = 18

# System.TypeNameFormatFlags
class TypeNameFormatFlags(IntFlag):
    FormatBasic = 0
    FormatNamespace = 1
    FormatFullInst = 2
    FormatAssembly = 4
    FormatSignature = 8
    FormatNoVersion = 16
    FormatAngleBrackets = 64
    FormatStubInfo = 128
    FormatGenericParam = 256
    FormatSerialization = 259

# System.TypeNameKind
class TypeNameKind(IntFlag):
    Name = 0
    ToString = 1
    SerializationName = 2
    FullName = 3

# System.TypeSpec
class TypeSpec(IntFlag):
    Default = 0
    WANT_ASSEMBLY = 1
    NO_MODIFIERS = 2

# System.UInt16Enum
class UInt16Enum(IntFlag):

# System.UInt32Enum
class UInt32Enum(IntFlag):

# System.UInt64Enum
class UInt64Enum(IntFlag):

# System.UnescapeMode
class UnescapeMode(IntFlag):
    CopyOnly = 0
    Escape = 1
    Unescape = 2
    EscapeUnescape = 3
    V1ToStringFlag = 4
    UnescapeAll = 8
    UnescapeAllOrThrow = 24

# System.Uri
class Uri(IntFlag):
    Zero = 0
    SchemeNotCanonical = 1
    UserNotCanonical = 2
    HostNotCanonical = 4
    PortNotCanonical = 8
    PathNotCanonical = 16
    QueryNotCanonical = 32
    FragmentNotCanonical = 64
    CannotDisplayCanonical = 127
    E_UserNotCanonical = 128
    E_HostNotCanonical = 256
    E_PortNotCanonical = 512
    E_PathNotCanonical = 1024
    E_QueryNotCanonical = 2048
    E_FragmentNotCanonical = 4096
    E_CannotDisplayCanonical = 8064
    ShouldBeCompressed = 8192
    FirstSlashAbsent = 16384
    BackslashInPath = 32768
    IndexMask = 65535
    HostTypeMask = 458752
    HostNotParsed = 0
    IPv6HostType = 65536
    IPv4HostType = 131072
    DnsHostType = 196608
    UncHostType = 262144
    BasicHostType = 327680
    UnusedHostType = 393216
    UnknownHostType = 458752
    UserEscaped = 524288
    AuthorityFound = 1048576
    HasUserInfo = 2097152
    LoopbackHost = 4194304
    NotDefaultPort = 8388608
    UserDrivenParsing = 16777216
    CanonicalDnsHost = 33554432
    ErrorOrParsingRecursion = 67108864
    DosPath = 134217728
    UncPath = 268435456
    ImplicitFile = 536870912
    MinimalUriInfoSet = 1073741824
    AllUriInfoSet = 2147483648
    IdnHost = 4294967296
    HasUnicode = 8589934592
    HostUnicodeNormalized = 17179869184
    RestUnicodeNormalized = 34359738368
    UnicodeHost = 68719476736
    IntranetUri = 137438953472
    UseOrigUncdStrOffset = 274877906944
    UserIriCanonical = 549755813888
    PathIriCanonical = 1099511627776
    QueryIriCanonical = 2199023255552
    FragmentIriCanonical = 4398046511104
    IriCanonical = 8246337208320
    CompressedSlashes = 17592186044416

# System.Uri
class Uri(IntFlag):
    NONE = 0
    EscapedCanonical = 1
    DisplayCanonical = 2
    DotSlashAttn = 4
    DotSlashEscaped = 128
    BackslashInPath = 16
    ReservedFound = 32
    NotIriCanonical = 64
    FoundNonAscii = 8

# System.UriComponents
class UriComponents(IntFlag):
    Scheme = 1
    UserInfo = 2
    Host = 4
    Port = 8
    Path = 16
    Query = 32
    Fragment = 64
    StrongPort = 128
    NormalizedHost = 256
    KeepDelimiter = 1073741824
    SerializationInfoString = -2147483648
    AbsoluteUri = 127
    HostAndPort = 132
    StrongAuthority = 134
    SchemeAndServer = 13
    HttpRequestUrl = 61
    PathAndQuery = 48

# System.UriFormat
class UriFormat(IntFlag):
    UriEscaped = 1
    Unescaped = 2
    SafeUnescaped = 3

# System.UriHostNameType
class UriHostNameType(IntFlag):
    Unknown = 0
    Basic = 1
    Dns = 2
    IPv4 = 3
    IPv6 = 4

# System.UriIdnScope
class UriIdnScope(IntFlag):
    NONE = 0
    AllExceptIntranet = 1
    All = 2

# System.UriKind
class UriKind(IntFlag):
    RelativeOrAbsolute = 0
    Absolute = 1
    Relative = 2

# System.UriParser
class UriParser(IntFlag):
    V2 = 2
    V3 = 3

# System.UriSyntaxFlags
class UriSyntaxFlags(IntFlag):
    NONE = 0
    MustHaveAuthority = 1
    OptionalAuthority = 2
    MayHaveUserInfo = 4
    MayHavePort = 8
    MayHavePath = 16
    MayHaveQuery = 32
    MayHaveFragment = 64
    AllowEmptyHost = 128
    AllowUncHost = 256
    AllowDnsHost = 512
    AllowIPv4Host = 1024
    AllowIPv6Host = 2048
    AllowAnInternetHost = 3584
    AllowAnyOtherHost = 4096
    FileLikeUri = 8192
    MailToLikeUri = 16384
    V1_UnknownUri = 65536
    SimpleUserSyntax = 131072
    BuiltInSyntax = 262144
    ParserSchemeOnly = 524288
    AllowDOSPath = 1048576
    PathIsRooted = 2097152
    ConvertPathSlashes = 4194304
    CompressPath = 8388608
    CanonicalizeAsFilePath = 16777216
    UnEscapeDotsAndSlashes = 33554432
    AllowIdn = 67108864
    AllowIriParsing = 268435456

