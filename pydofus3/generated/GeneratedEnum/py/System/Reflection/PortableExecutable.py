from enum import IntFlag

# System.Reflection.PortableExecutable.Characteristics
class Characteristics(IntFlag):
    RelocsStripped = 1
    ExecutableImage = 2
    LineNumsStripped = 4
    LocalSymsStripped = 8
    AggressiveWSTrim = 16
    LargeAddressAware = 32
    BytesReversedLo = 128
    Bit32Machine = 256
    DebugStripped = 512
    RemovableRunFromSwap = 1024
    NetRunFromSwap = 2048
    System = 4096
    Dll = 8192
    UpSystemOnly = 16384
    BytesReversedHi = 32768

# System.Reflection.PortableExecutable.CorFlags
class CorFlags(IntFlag):
    ILOnly = 1
    Requires32Bit = 2
    ILLibrary = 4
    StrongNameSigned = 8
    NativeEntryPoint = 16
    TrackDebugData = 65536
    Prefers32Bit = 131072

# System.Reflection.PortableExecutable.DebugDirectoryEntryType
class DebugDirectoryEntryType(IntFlag):
    Unknown = 0
    Coff = 1
    CodeView = 2
    Reproducible = 16
    EmbeddedPortablePdb = 17
    PdbChecksum = 19

# System.Reflection.PortableExecutable.DllCharacteristics
class DllCharacteristics(IntFlag):
    ProcessInit = 1
    ProcessTerm = 2
    ThreadInit = 4
    ThreadTerm = 8
    HighEntropyVirtualAddressSpace = 32
    DynamicBase = 64
    NxCompatible = 256
    NoIsolation = 512
    NoSeh = 1024
    NoBind = 2048
    AppContainer = 4096
    WdmDriver = 8192
    TerminalServerAware = 32768

# System.Reflection.PortableExecutable.Machine
class Machine(IntFlag):
    Unknown = 0
    I386 = 332
    WceMipsV2 = 361
    Alpha = 388
    SH3 = 418
    SH3Dsp = 419
    SH3E = 420
    SH4 = 422
    SH5 = 424
    Arm = 448
    Thumb = 450
    ArmThumb2 = 452
    AM33 = 467
    PowerPC = 496
    PowerPCFP = 497
    IA64 = 512
    MIPS16 = 614
    Alpha64 = 644
    MipsFpu = 870
    MipsFpu16 = 1126
    Tricore = 1312
    Ebc = 3772
    Amd64 = 34404
    M32R = 36929
    Arm64 = 43620

# System.Reflection.PortableExecutable.PEMagic
class PEMagic(IntFlag):
    PE32 = 267
    PE32Plus = 523

# System.Reflection.PortableExecutable.PEStreamOptions
class PEStreamOptions(IntFlag):
    Default = 0
    LeaveOpen = 1
    PrefetchMetadata = 2
    PrefetchEntireImage = 4
    IsLoadedImage = 8

# System.Reflection.PortableExecutable.SectionCharacteristics
class SectionCharacteristics(IntFlag):
    TypeReg = 0
    TypeDSect = 1
    TypeNoLoad = 2
    TypeGroup = 4
    TypeNoPad = 8
    TypeCopy = 16
    ContainsCode = 32
    ContainsInitializedData = 64
    ContainsUninitializedData = 128
    LinkerOther = 256
    LinkerInfo = 512
    TypeOver = 1024
    LinkerRemove = 2048
    LinkerComdat = 4096
    MemProtected = 16384
    NoDeferSpecExc = 16384
    GPRel = 32768
    MemFardata = 32768
    MemSysheap = 65536
    MemPurgeable = 131072
    Mem16Bit = 131072
    MemLocked = 262144
    MemPreload = 524288
    Align1Bytes = 1048576
    Align2Bytes = 2097152
    Align4Bytes = 3145728
    Align8Bytes = 4194304
    Align16Bytes = 5242880
    Align32Bytes = 6291456
    Align64Bytes = 7340032
    Align128Bytes = 8388608
    Align256Bytes = 9437184
    Align512Bytes = 10485760
    Align1024Bytes = 11534336
    Align2048Bytes = 12582912
    Align4096Bytes = 13631488
    Align8192Bytes = 14680064
    AlignMask = 15728640
    LinkerNRelocOvfl = 16777216
    MemDiscardable = 33554432
    MemNotCached = 67108864
    MemNotPaged = 134217728
    MemShared = 268435456
    MemExecute = 536870912
    MemRead = 1073741824
    MemWrite = 2147483648

# System.Reflection.PortableExecutable.Subsystem
class Subsystem(IntFlag):
    Unknown = 0
    Native = 1
    WindowsGui = 2
    WindowsCui = 3
    OS2Cui = 5
    PosixCui = 7
    NativeWindows = 8
    WindowsCEGui = 9
    EfiApplication = 10
    EfiBootServiceDriver = 11
    EfiRuntimeDriver = 12
    EfiRom = 13
    Xbox = 14
    WindowsBootApplication = 16

