from enum import IntFlag

# System.Reflection.AssemblyContentType
class AssemblyContentType(IntFlag):
    Default = 0
    WindowsRuntime = 1

# System.Reflection.AssemblyFlags
class AssemblyFlags(IntFlag):
    PublicKey = 1
    Retargetable = 256
    WindowsRuntime = 512
    ContentTypeMask = 3584
    DisableJitCompileOptimizer = 16384
    EnableJitCompileTracking = 32768

# System.Reflection.AssemblyHashAlgorithm
class AssemblyHashAlgorithm(IntFlag):
    NONE = 0
    MD5 = 32771
    Sha1 = 32772
    Sha256 = 32780
    Sha384 = 32781
    Sha512 = 32782

# System.Reflection.AssemblyNameFlags
class AssemblyNameFlags(IntFlag):
    NONE = 0
    PublicKey = 1
    EnableJITcompileOptimizer = 16384
    EnableJITcompileTracking = 32768
    Retargetable = 256

# System.Reflection.BindingFlags
class BindingFlags(IntFlag):
    Default = 0
    IgnoreCase = 1
    DeclaredOnly = 2
    Instance = 4
    Static = 8
    Public = 16
    NonPublic = 32
    FlattenHierarchy = 64
    InvokeMethod = 256
    CreateInstance = 512
    GetField = 1024
    SetField = 2048
    GetProperty = 4096
    SetProperty = 8192
    PutDispProperty = 16384
    PutRefDispProperty = 32768
    ExactBinding = 65536
    SuppressChangeType = 131072
    OptionalParamBinding = 262144
    IgnoreReturn = 16777216
    DoNotWrapExceptions = 33554432

# System.Reflection.CallingConventions
class CallingConventions(IntFlag):
    Standard = 1
    VarArgs = 2
    Any = 3
    HasThis = 32
    ExplicitThis = 64

# System.Reflection.CorElementType
class CorElementType(IntFlag):
    End = 0
    Void = 1
    Boolean = 2
    Char = 3
    I1 = 4
    U1 = 5
    I2 = 6
    U2 = 7
    I4 = 8
    U4 = 9
    I8 = 10
    U8 = 11
    R4 = 12
    R8 = 13
    String = 14
    Ptr = 15
    ByRef = 16
    ValueType = 17
    Class = 18
    Var = 19
    Array = 20
    GenericInst = 21
    TypedByRef = 22
    I = 24
    U = 25
    FnPtr = 27
    Object = 28
    SzArray = 29
    MVar = 30
    CModReqd = 31
    CModOpt = 32
    Internal = 33
    Max = 34
    Modifier = 64
    Sentinel = 65
    Pinned = 69
    ELEMENT_TYPE_END = 0
    ELEMENT_TYPE_VOID = 1
    ELEMENT_TYPE_BOOLEAN = 2
    ELEMENT_TYPE_CHAR = 3
    ELEMENT_TYPE_I1 = 4
    ELEMENT_TYPE_U1 = 5
    ELEMENT_TYPE_I2 = 6
    ELEMENT_TYPE_U2 = 7
    ELEMENT_TYPE_I4 = 8
    ELEMENT_TYPE_U4 = 9
    ELEMENT_TYPE_I8 = 10
    ELEMENT_TYPE_U8 = 11
    ELEMENT_TYPE_R4 = 12
    ELEMENT_TYPE_R8 = 13
    ELEMENT_TYPE_STRING = 14
    ELEMENT_TYPE_PTR = 15
    ELEMENT_TYPE_BYREF = 16
    ELEMENT_TYPE_VALUETYPE = 17
    ELEMENT_TYPE_CLASS = 18
    ELEMENT_TYPE_VAR = 19
    ELEMENT_TYPE_ARRAY = 20
    ELEMENT_TYPE_GENERICINST = 21
    ELEMENT_TYPE_TYPEDBYREF = 22
    ELEMENT_TYPE_I = 24
    ELEMENT_TYPE_U = 25
    ELEMENT_TYPE_FNPTR = 27
    ELEMENT_TYPE_OBJECT = 28
    ELEMENT_TYPE_SZARRAY = 29
    ELEMENT_TYPE_MVAR = 30
    ELEMENT_TYPE_CMOD_REQD = 31
    ELEMENT_TYPE_CMOD_OPT = 32
    ELEMENT_TYPE_INTERNAL = 33
    ELEMENT_TYPE_MAX = 34
    ELEMENT_TYPE_MODIFIER = 64
    ELEMENT_TYPE_SENTINEL = 65
    ELEMENT_TYPE_PINNED = 69

# System.Reflection.DeclarativeSecurityAction
class DeclarativeSecurityAction(IntFlag):
    NONE = 0
    Demand = 2
    Assert = 3
    Deny = 4
    PermitOnly = 5
    LinkDemand = 6
    InheritanceDemand = 7
    RequestMinimum = 8
    RequestOptional = 9
    RequestRefuse = 10

# System.Reflection.EventAttributes
class EventAttributes(IntFlag):
    NONE = 0
    SpecialName = 512
    RTSpecialName = 1024
    ReservedMask = 1024

# System.Reflection.ExceptionHandlingClauseOptions
class ExceptionHandlingClauseOptions(IntFlag):
    Clause = 0
    Filter = 1
    Finally = 2
    Fault = 4

# System.Reflection.FieldAttributes
class FieldAttributes(IntFlag):
    FieldAccessMask = 7
    PrivateScope = 0
    Private = 1
    FamANDAssem = 2
    Assembly = 3
    Family = 4
    FamORAssem = 5
    Public = 6
    Static = 16
    InitOnly = 32
    Literal = 64
    NotSerialized = 128
    SpecialName = 512
    PinvokeImpl = 8192
    RTSpecialName = 1024
    HasFieldMarshal = 4096
    HasDefault = 32768
    HasFieldRVA = 256
    ReservedMask = 38144

# System.Reflection.GenericParameterAttributes
class GenericParameterAttributes(IntFlag):
    NONE = 0
    VarianceMask = 3
    Covariant = 1
    Contravariant = 2
    SpecialConstraintMask = 28
    ReferenceTypeConstraint = 4
    NotNullableValueTypeConstraint = 8
    DefaultConstructorConstraint = 16

# System.Reflection.ImageFileMachine
class ImageFileMachine(IntFlag):
    I386 = 332
    IA64 = 512
    AMD64 = 34404
    ARM = 452

# System.Reflection.ManifestResourceAttributes
class ManifestResourceAttributes(IntFlag):
    Public = 1
    Private = 2
    VisibilityMask = 7

# System.Reflection.MemberTypes
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

# System.Reflection.MethodAttributes
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
    CheckAccessOnOverride = 512
    VtableLayoutMask = 256
    ReuseSlot = 0
    NewSlot = 256
    Abstract = 1024
    SpecialName = 2048
    PinvokeImpl = 8192
    UnmanagedExport = 8
    RTSpecialName = 4096
    HasSecurity = 16384
    RequireSecObject = 32768
    ReservedMask = 53248

# System.Reflection.MethodImplAttributes
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
    AggressiveInlining = 256
    NoOptimization = 64
    MaxMethodImplVal = 65535
    SecurityMitigations = 1024

# System.Reflection.MethodImportAttributes
class MethodImportAttributes(IntFlag):
    NONE = 0
    ExactSpelling = 1
    BestFitMappingDisable = 32
    BestFitMappingEnable = 16
    BestFitMappingMask = 48
    CharSetAnsi = 2
    CharSetUnicode = 4
    CharSetAuto = 6
    CharSetMask = 6
    ThrowOnUnmappableCharEnable = 4096
    ThrowOnUnmappableCharDisable = 8192
    ThrowOnUnmappableCharMask = 12288
    SetLastError = 64
    CallingConventionWinApi = 256
    CallingConventionCDecl = 512
    CallingConventionStdCall = 768
    CallingConventionThisCall = 1024
    CallingConventionFastCall = 1280
    CallingConventionMask = 1792

# System.Reflection.MethodSemanticsAttributes
class MethodSemanticsAttributes(IntFlag):
    Setter = 1
    Getter = 2
    Other = 4
    Adder = 8
    Remover = 16
    Raiser = 32

# System.Reflection.NullabilityInfoContext
class NullabilityInfoContext(IntFlag):
    NONE = 0
    Private = 1
    Internal = 2

# System.Reflection.NullabilityState
class NullabilityState(IntFlag):
    Unknown = 0
    NotNull = 1
    Nullable = 2

# System.Reflection.PInfo
class PInfo(IntFlag):
    Attributes = 1
    GetMethod = 2
    SetMethod = 4
    ReflectedType = 8
    DeclaringType = 16
    Name = 32

# System.Reflection.PInvokeAttributes
class PInvokeAttributes(IntFlag):
    NoMangle = 1
    CharSetMask = 6
    CharSetNotSpec = 0
    CharSetAnsi = 2
    CharSetUnicode = 4
    CharSetAuto = 6
    BestFitUseAssem = 0
    BestFitEnabled = 16
    BestFitDisabled = 32
    BestFitMask = 48
    ThrowOnUnmappableCharUseAssem = 0
    ThrowOnUnmappableCharEnabled = 4096
    ThrowOnUnmappableCharDisabled = 8192
    ThrowOnUnmappableCharMask = 12288
    SupportsLastError = 64
    CallConvMask = 1792
    CallConvWinapi = 256
    CallConvCdecl = 512
    CallConvStdcall = 768
    CallConvThiscall = 1024
    CallConvFastcall = 1280
    MaxValue = 65535

# System.Reflection.ParameterAttributes
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

# System.Reflection.PortableExecutableKinds
class PortableExecutableKinds(IntFlag):
    NotAPortableExecutableImage = 0
    ILOnly = 1
    Required32Bit = 2
    PE32Plus = 4
    Unmanaged32Bit = 8
    Preferred32Bit = 16

# System.Reflection.ProcessorArchitecture
class ProcessorArchitecture(IntFlag):
    NONE = 0
    MSIL = 1
    X86 = 2
    IA64 = 3
    Amd64 = 4
    Arm = 5

# System.Reflection.PropertyAttributes
class PropertyAttributes(IntFlag):
    NONE = 0
    SpecialName = 512
    RTSpecialName = 1024
    HasDefault = 4096
    Reserved2 = 8192
    Reserved3 = 16384
    Reserved4 = 32768
    ReservedMask = 62464

# System.Reflection.ResolveTokenError
class ResolveTokenError(IntFlag):
    OutOfRange = 0
    BadTable = 1
    Other = 2

# System.Reflection.ResourceAttributes
class ResourceAttributes(IntFlag):
    Public = 1
    Private = 2

# System.Reflection.ResourceLocation
class ResourceLocation(IntFlag):
    ContainedInAnotherAssembly = 2
    ContainedInManifestFile = 4
    Embedded = 1

# System.Reflection.TypeAttributes
class TypeAttributes(IntFlag):
    VisibilityMask = 7
    NotPublic = 0
    Public = 1
    NestedPublic = 2
    NestedPrivate = 3
    NestedFamily = 4
    NestedAssembly = 5
    NestedFamANDAssem = 6
    NestedFamORAssem = 7
    LayoutMask = 24
    AutoLayout = 0
    SequentialLayout = 8
    ExplicitLayout = 16
    ClassSemanticsMask = 32
    Class = 0
    Interface = 32
    Abstract = 128
    Sealed = 256
    SpecialName = 1024
    Import = 4096
    Serializable = 8192
    WindowsRuntime = 16384
    StringFormatMask = 196608
    AnsiClass = 0
    UnicodeClass = 65536
    AutoClass = 131072
    CustomFormatClass = 196608
    CustomFormatMask = 12582912
    BeforeFieldInit = 1048576
    RTSpecialName = 2048
    HasSecurity = 262144
    ReservedMask = 264192

