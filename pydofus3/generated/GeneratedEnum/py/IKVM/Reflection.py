from enum import IntFlag

# IKVM.Reflection.AssemblyComparisonResult
class AssemblyComparisonResult(IntFlag):
    Unknown = 0
    EquivalentFullMatch = 1
    EquivalentWeakNamed = 2
    EquivalentFXUnified = 3
    EquivalentUnified = 4
    NonEquivalentVersion = 5
    NonEquivalent = 6
    EquivalentPartialMatch = 7
    EquivalentPartialWeakNamed = 8
    EquivalentPartialUnified = 9
    EquivalentPartialFXUnified = 10
    NonEquivalentPartialVersion = 11

# IKVM.Reflection.AssemblyContentType
class AssemblyContentType(IntFlag):
    Default = 0
    WindowsRuntime = 1

# IKVM.Reflection.AssemblyNameFlags
class AssemblyNameFlags(IntFlag):
    NONE = 0
    PublicKey = 1
    Retargetable = 256
    EnableJITcompileOptimizer = 16384
    EnableJITcompileTracking = 32768

# IKVM.Reflection.BindingFlags
class BindingFlags(IntFlag):
    Default = 0
    IgnoreCase = 1
    DeclaredOnly = 2
    Instance = 4
    Static = 8
    Public = 16
    NonPublic = 32
    FlattenHierarchy = 64

# IKVM.Reflection.CallingConventions
class CallingConventions(IntFlag):
    Standard = 1
    VarArgs = 2
    Any = 3
    HasThis = 32
    ExplicitThis = 64

# IKVM.Reflection.DllCharacteristics
class DllCharacteristics(IntFlag):
    HighEntropyVA = 32
    DynamicBase = 64
    NoSEH = 1024
    NXCompat = 256
    AppContainer = 4096
    TerminalServerAware = 32768

# IKVM.Reflection.EventAttributes
class EventAttributes(IntFlag):
    NONE = 0
    SpecialName = 512
    RTSpecialName = 1024
    ReservedMask = 1024

# IKVM.Reflection.ExceptionHandlingClauseOptions
class ExceptionHandlingClauseOptions(IntFlag):
    Clause = 0
    Filter = 1
    Finally = 2
    Fault = 4

# IKVM.Reflection.FieldAttributes
class FieldAttributes(IntFlag):
    PrivateScope = 0
    Private = 1
    FamANDAssem = 2
    Assembly = 3
    Family = 4
    FamORAssem = 5
    Public = 6
    FieldAccessMask = 7
    Static = 16
    InitOnly = 32
    Literal = 64
    NotSerialized = 128
    HasFieldRVA = 256
    SpecialName = 512
    RTSpecialName = 1024
    HasFieldMarshal = 4096
    PinvokeImpl = 8192
    HasDefault = 32768
    ReservedMask = 38144

# IKVM.Reflection.GenericParameterAttributes
class GenericParameterAttributes(IntFlag):
    NONE = 0
    Covariant = 1
    Contravariant = 2
    VarianceMask = 3
    ReferenceTypeConstraint = 4
    NotNullableValueTypeConstraint = 8
    DefaultConstructorConstraint = 16
    SpecialConstraintMask = 28

# IKVM.Reflection.ImageFileMachine
class ImageFileMachine(IntFlag):
    I386 = 332
    ARM = 452
    IA64 = 512
    AMD64 = 34404

# IKVM.Reflection.ImplMapFlags
class ImplMapFlags(IntFlag):
    NoMangle = 1
    CharSetMask = 6
    CharSetNotSpec = 0
    CharSetAnsi = 2
    CharSetUnicode = 4
    CharSetAuto = 6
    SupportsLastError = 64
    CallConvMask = 1792
    CallConvWinapi = 256
    CallConvCdecl = 512
    CallConvStdcall = 768
    CallConvThiscall = 1024
    CallConvFastcall = 1280
    BestFitOn = 16
    BestFitOff = 32
    CharMapErrorOn = 4096
    CharMapErrorOff = 8192

# IKVM.Reflection.MemberTypes
class MemberTypes(IntFlag):
    Constructor = 1
    Event = 2
    Field = 4
    Method = 8
    Property = 16
    TypeInfo = 32
    Custom = 64
    NestedType = 128
    All = 191

# IKVM.Reflection.MethodAttributes
class MethodAttributes(IntFlag):
    MemberAccessMask = 7
    PrivateScope = 0
    Private = 1
    FamANDAssem = 2
    Assembly = 3
    Family = 4
    FamORAssem = 5
    Public = 6
    Static = 16
    Final = 32
    Virtual = 64
    HideBySig = 128
    VtableLayoutMask = 256
    ReuseSlot = 0
    NewSlot = 256
    CheckAccessOnOverride = 512
    Abstract = 1024
    SpecialName = 2048
    PinvokeImpl = 8192
    UnmanagedExport = 8
    RTSpecialName = 4096
    HasSecurity = 16384
    RequireSecObject = 32768
    ReservedMask = 53248

# IKVM.Reflection.MethodImplAttributes
class MethodImplAttributes(IntFlag):
    CodeTypeMask = 3
    IL = 0
    Native = 1
    OPTIL = 2
    Runtime = 3
    ManagedMask = 4
    Unmanaged = 4
    Managed = 0
    ForwardRef = 16
    PreserveSig = 128
    InternalCall = 4096
    Synchronized = 32
    NoInlining = 8
    NoOptimization = 64
    AggressiveInlining = 256
    MaxMethodImplVal = 65535

# IKVM.Reflection.ParameterAttributes
class ParameterAttributes(IntFlag):
    NONE = 0
    In = 1
    Out = 2
    Lcid = 4
    Retval = 8
    Optional = 16
    HasDefault = 4096
    HasFieldMarshal = 8192
    Reserved3 = 16384
    Reserved4 = 32768
    ReservedMask = 61440

# IKVM.Reflection.ParseAssemblyResult
class ParseAssemblyResult(IntFlag):
    OK = 0
    GenericError = 1
    DuplicateKey = 2

# IKVM.Reflection.PortableExecutableKinds
class PortableExecutableKinds(IntFlag):
    NotAPortableExecutableImage = 0
    ILOnly = 1
    Required32Bit = 2
    PE32Plus = 4
    Unmanaged32Bit = 8
    Preferred32Bit = 16

# IKVM.Reflection.ProcessorArchitecture
class ProcessorArchitecture(IntFlag):
    NONE = 0
    MSIL = 1
    X86 = 2
    IA64 = 3
    Amd64 = 4
    Arm = 5

# IKVM.Reflection.PropertyAttributes
class PropertyAttributes(IntFlag):
    NONE = 0
    SpecialName = 512
    RTSpecialName = 1024
    HasDefault = 4096

# IKVM.Reflection.ResourceAttributes
class ResourceAttributes(IntFlag):
    Public = 1
    Private = 2

# IKVM.Reflection.ResourceLocation
class ResourceLocation(IntFlag):
    Embedded = 1
    ContainedInAnotherAssembly = 2
    ContainedInManifestFile = 4

# IKVM.Reflection.Type
class Type(IntFlag):
    IsGenericTypeDefinition = 1
    HasNestedTypes = 2
    Baked = 4
    ValueType = 8
    NotValueType = 16
    PotentialEnumOrValueType = 32
    EnumOrValueType = 64
    NotGenericTypeDefinition = 128
    ContainsMissingType_Unknown = 0
    ContainsMissingType_Pending = 256
    ContainsMissingType_Yes = 512
    ContainsMissingType_No = 768
    ContainsMissingType_Mask = 768
    PotentialBuiltIn = 1024
    BuiltIn = 2048

# IKVM.Reflection.TypeAttributes
class TypeAttributes(IntFlag):
    AnsiClass = 0
    Class = 0
    AutoLayout = 0
    NotPublic = 0
    Public = 1
    NestedPublic = 2
    NestedPrivate = 3
    NestedFamily = 4
    NestedAssembly = 5
    NestedFamANDAssem = 6
    VisibilityMask = 7
    NestedFamORAssem = 7
    SequentialLayout = 8
    ExplicitLayout = 16
    LayoutMask = 24
    ClassSemanticsMask = 32
    Interface = 32
    Abstract = 128
    Sealed = 256
    SpecialName = 1024
    RTSpecialName = 2048
    Import = 4096
    Serializable = 8192
    WindowsRuntime = 16384
    UnicodeClass = 65536
    AutoClass = 131072
    CustomFormatClass = 196608
    StringFormatMask = 196608
    HasSecurity = 262144
    ReservedMask = 264192
    BeforeFieldInit = 1048576
    CustomFormatMask = 12582912

# IKVM.Reflection.UniverseOptions
class UniverseOptions(IntFlag):
    NONE = 0
    EnableFunctionPointers = 1
    DisableFusion = 2
    DisablePseudoCustomAttributeRetrieval = 4
    DontProvideAutomaticDefaultConstructor = 8
    MetadataOnly = 16
    ResolveMissingMembers = 32
    DisableWindowsRuntimeProjection = 64
    DecodeVersionInfoAttributeBlobs = 128
    DeterministicOutput = 256

# IKVM.Reflection.WindowsRuntimeProjection
class WindowsRuntimeProjection(IntFlag):
    System_Runtime = 0
    System_Runtime_InteropServices_WindowsRuntime = 1
    System_ObjectModel = 2
    System_Runtime_WindowsRuntime = 3
    System_Runtime_WindowsRuntime_UI_Xaml = 4
    Count = 5

