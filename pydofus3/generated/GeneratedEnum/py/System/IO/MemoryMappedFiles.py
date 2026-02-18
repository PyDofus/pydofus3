from enum import IntFlag

# System.IO.MemoryMappedFiles.MemoryMappedFileAccess
class MemoryMappedFileAccess(IntFlag):
    ReadWrite = 0
    Read = 1
    Write = 2
    CopyOnWrite = 3
    ReadExecute = 4
    ReadWriteExecute = 5

# System.IO.MemoryMappedFiles.MemoryMappedFileOptions
class MemoryMappedFileOptions(IntFlag):
    NONE = 0
    DelayAllocatePages = 67108864

