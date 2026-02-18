from enum import IntFlag

# System.IO.FileAccess
class FileAccess(IntFlag):
    Read = 1
    Write = 2
    ReadWrite = 3

# System.IO.FileAction
class FileAction(IntFlag):
    Added = 1
    Removed = 2
    Modified = 3
    RenamedOldName = 4
    RenamedNewName = 5

# System.IO.FileAttributes
class FileAttributes(IntFlag):
    ReadOnly = 1
    Hidden = 2
    System = 4
    Directory = 16
    Archive = 32
    Device = 64
    Normal = 128
    Temporary = 256
    SparseFile = 512
    ReparsePoint = 1024
    Compressed = 2048
    Offline = 4096
    NotContentIndexed = 8192
    Encrypted = 16384
    IntegrityStream = 32768
    NoScrubData = 131072

# System.IO.FileMode
class FileMode(IntFlag):
    CreateNew = 1
    Create = 2
    Open = 3
    OpenOrCreate = 4
    Truncate = 5
    Append = 6

# System.IO.FileOptions
class FileOptions(IntFlag):
    NONE = 0
    WriteThrough = -2147483648
    Asynchronous = 1073741824
    RandomAccess = 268435456
    DeleteOnClose = 67108864
    SequentialScan = 134217728
    Encrypted = 16384

# System.IO.FileShare
class FileShare(IntFlag):
    NONE = 0
    Read = 1
    Write = 2
    ReadWrite = 3
    Delete = 4
    Inheritable = 16

# System.IO.FileSystemWatcher
class FileSystemWatcher(IntFlag):
    FileSystemEvent = 0
    ErrorEvent = 1
    RenameEvent = 2

# System.IO.HandleInheritability
class HandleInheritability(IntFlag):
    NONE = 0
    Inheritable = 1

# System.IO.MatchCasing
class MatchCasing(IntFlag):
    PlatformDefault = 0
    CaseSensitive = 1
    CaseInsensitive = 2

# System.IO.MatchType
class MatchType(IntFlag):
    Simple = 0
    Win32 = 1

# System.IO.MonoFileType
class MonoFileType(IntFlag):
    Unknown = 0
    Disk = 1
    Char = 2
    Pipe = 3
    Remote = 32768

# System.IO.MonoIOError
class MonoIOError(IntFlag):
    ERROR_SUCCESS = 0
    ERROR_FILE_NOT_FOUND = 2
    ERROR_PATH_NOT_FOUND = 3
    ERROR_TOO_MANY_OPEN_FILES = 4
    ERROR_ACCESS_DENIED = 5
    ERROR_INVALID_HANDLE = 6
    ERROR_INVALID_DRIVE = 15
    ERROR_NOT_SAME_DEVICE = 17
    ERROR_NO_MORE_FILES = 18
    ERROR_NOT_READY = 21
    ERROR_WRITE_FAULT = 29
    ERROR_READ_FAULT = 30
    ERROR_GEN_FAILURE = 31
    ERROR_SHARING_VIOLATION = 32
    ERROR_LOCK_VIOLATION = 33
    ERROR_HANDLE_DISK_FULL = 39
    ERROR_NOT_SUPPORTED = 50
    ERROR_FILE_EXISTS = 80
    ERROR_CANNOT_MAKE = 82
    ERROR_INVALID_PARAMETER = 87
    ERROR_BROKEN_PIPE = 109
    ERROR_INVALID_NAME = 123
    ERROR_DIR_NOT_EMPTY = 145
    ERROR_ALREADY_EXISTS = 183
    ERROR_FILENAME_EXCED_RANGE = 206
    ERROR_DIRECTORY = 267
    ERROR_ENCRYPTION_FAILED = 6000

# System.IO.NotifyFilters
class NotifyFilters(IntFlag):
    Attributes = 4
    CreationTime = 64
    DirectoryName = 2
    FileName = 1
    LastAccess = 32
    LastWrite = 16
    Security = 256
    Size = 8

# System.IO.SearchOption
class SearchOption(IntFlag):
    TopDirectoryOnly = 0
    AllDirectories = 1

# System.IO.SearchPattern2
class SearchPattern2(IntFlag):
    ExactString = 0
    AnyChar = 1
    AnyString = 2
    End = 3
    TRUE = 4

# System.IO.SearchTarget
class SearchTarget(IntFlag):
    Files = 1
    Directories = 2
    Both = 3

# System.IO.SeekOrigin
class SeekOrigin(IntFlag):
    Begin = 0
    Current = 1
    End = 2

# System.IO.WatcherChangeTypes
class WatcherChangeTypes(IntFlag):
    All = 15
    Changed = 4
    Created = 1
    Deleted = 2
    Renamed = 8

