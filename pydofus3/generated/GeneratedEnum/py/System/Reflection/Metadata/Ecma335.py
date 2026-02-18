from enum import IntFlag

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    MethodDef = 0
    Field = 1
    TypeRef = 2
    TypeDef = 3
    Param = 4
    InterfaceImpl = 5
    MemberRef = 6
    Module = 7
    DeclSecurity = 8
    Property = 9
    Event = 10
    StandAloneSig = 11
    ModuleRef = 12
    TypeSpec = 13
    Assembly = 14
    AssemblyRef = 15
    File = 16
    ExportedType = 17
    ManifestResource = 18
    GenericParam = 19
    GenericParamConstraint = 20
    MethodSpec = 21
    BitCount = 5

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    Field = 0
    Param = 1
    Property = 2
    BitCount = 2

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    MethodDef = 2
    MemberRef = 3
    BitCount = 3

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    TypeDef = 0
    MethodDef = 1
    Assembly = 2
    BitCount = 2

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    Field = 0
    Param = 1
    BitCount = 1

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    Event = 0
    Property = 1
    BitCount = 1

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    File = 0
    AssemblyRef = 1
    ExportedType = 2
    BitCount = 2

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    Field = 0
    MethodDef = 1
    BitCount = 1

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    TypeDef = 0
    TypeRef = 1
    ModuleRef = 2
    MethodDef = 3
    TypeSpec = 4
    BitCount = 3

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    MethodDef = 0
    MemberRef = 1
    BitCount = 1

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    Module = 0
    ModuleRef = 1
    AssemblyRef = 2
    TypeRef = 3
    BitCount = 2

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    TypeDef = 0
    TypeRef = 1
    TypeSpec = 2
    BitCount = 2

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    TypeDef = 0
    TypeRef = 1
    BitCount = 2

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    TypeDef = 0
    MethodDef = 1
    BitCount = 1

# System.Reflection.Metadata.Ecma335.CodedIndex
class CodedIndex(IntFlag):
    MethodDef = 0
    Field = 1
    TypeRef = 2
    TypeDef = 3
    Param = 4
    InterfaceImpl = 5
    MemberRef = 6
    Module = 7
    DeclSecurity = 8
    Property = 9
    Event = 10
    StandAloneSig = 11
    ModuleRef = 12
    TypeSpec = 13
    Assembly = 14
    AssemblyRef = 15
    File = 16
    ExportedType = 17
    ManifestResource = 18
    GenericParam = 19
    GenericParamConstraint = 20
    MethodSpec = 21
    Document = 22
    LocalScope = 23
    LocalVariable = 24
    LocalConstant = 25
    ImportScope = 26
    BitCount = 5

# System.Reflection.Metadata.Ecma335.CorElementType
class CorElementType(IntFlag):
    Invalid = 0
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
    ELEMENT_TYPE_HANDLE = 64
    ELEMENT_TYPE_SENTINEL = 65
    ELEMENT_TYPE_PINNED = 69

# System.Reflection.Metadata.Ecma335.CustomAttributeTreatment
class CustomAttributeTreatment(IntFlag):
    NONE = 0
    WinMD = 1

# System.Reflection.Metadata.Ecma335.CustomAttributeValueTreatment
class CustomAttributeValueTreatment(IntFlag):
    NONE = 0
    AttributeUsageAllowSingle = 1
    AttributeUsageAllowMultiple = 2
    AttributeUsageVersionAttribute = 3
    AttributeUsageDeprecatedAttribute = 4

# System.Reflection.Metadata.Ecma335.EditAndContinueOperation
class EditAndContinueOperation(IntFlag):
    Default = 0
    AddMethod = 1
    AddField = 2
    AddParameter = 3
    AddProperty = 4
    AddEvent = 5

# System.Reflection.Metadata.Ecma335.FieldDefTreatment
class FieldDefTreatment(IntFlag):
    NONE = 0
    EnumValue = 1

# System.Reflection.Metadata.Ecma335.FunctionPointerAttributes
class FunctionPointerAttributes(IntFlag):
    NONE = 0
    HasThis = 32
    HasExplicitThis = 96

# System.Reflection.Metadata.Ecma335.HeapIndex
class HeapIndex(IntFlag):
    UserString = 0
    String = 1
    Blob = 2
    Guid = 3

# System.Reflection.Metadata.Ecma335.HeapSizeFlag
class HeapSizeFlag(IntFlag):
    StringHeapLarge = 1
    GuidHeapLarge = 2
    BlobHeapLarge = 4
    EncDeltas = 32
    DeletedMarks = 128

# System.Reflection.Metadata.Ecma335.HeapSizes
class HeapSizes(IntFlag):
    StringHeapLarge = 1
    GuidHeapLarge = 2
    BlobHeapLarge = 4
    ExtraData = 64

# System.Reflection.Metadata.Ecma335.MemberRefTreatment
class MemberRefTreatment(IntFlag):
    NONE = 0
    Dispose = 1

# System.Reflection.Metadata.Ecma335.MetadataStreamKind
class MetadataStreamKind(IntFlag):
    Illegal = 0
    Compressed = 1
    Uncompressed = 2

# System.Reflection.Metadata.Ecma335.MethodBodyAttributes
class MethodBodyAttributes(IntFlag):
    NONE = 0
    InitLocals = 1

# System.Reflection.Metadata.Ecma335.MethodDefTreatment
class MethodDefTreatment(IntFlag):
    NONE = 0
    KindMask = 15
    Other = 1
    DelegateMethod = 2
    AttributeMethod = 3
    InterfaceMethod = 4
    Implementation = 5
    HiddenInterfaceImplementation = 6
    DisposeMethod = 7
    MarkAbstractFlag = 16
    MarkPublicFlag = 32

# System.Reflection.Metadata.Ecma335.StringKind
class StringKind(IntFlag):
    Plain = 0
    Virtual = 4
    WinRTPrefixed = 5
    DotTerminated = 1

# System.Reflection.Metadata.Ecma335.TableIndex
class TableIndex(IntFlag):
    Module = 0
    TypeRef = 1
    TypeDef = 2
    FieldPtr = 3
    Field = 4
    MethodPtr = 5
    MethodDef = 6
    ParamPtr = 7
    Param = 8
    InterfaceImpl = 9
    MemberRef = 10
    Constant = 11
    CustomAttribute = 12
    FieldMarshal = 13
    DeclSecurity = 14
    ClassLayout = 15
    FieldLayout = 16
    StandAloneSig = 17
    EventMap = 18
    EventPtr = 19
    Event = 20
    PropertyMap = 21
    PropertyPtr = 22
    Property = 23
    MethodSemantics = 24
    MethodImpl = 25
    ModuleRef = 26
    TypeSpec = 27
    ImplMap = 28
    FieldRva = 29
    EncLog = 30
    EncMap = 31
    Assembly = 32
    AssemblyProcessor = 33
    AssemblyOS = 34
    AssemblyRef = 35
    AssemblyRefProcessor = 36
    AssemblyRefOS = 37
    File = 38
    ExportedType = 39
    ManifestResource = 40
    NestedClass = 41
    GenericParam = 42
    MethodSpec = 43
    GenericParamConstraint = 44
    Document = 48
    MethodDebugInformation = 49
    LocalScope = 50
    LocalVariable = 51
    LocalConstant = 52
    ImportScope = 53
    StateMachineMethod = 54
    CustomDebugInformation = 55

# System.Reflection.Metadata.Ecma335.TableMask
class TableMask(IntFlag):
    Module = 1
    TypeRef = 2
    TypeDef = 4
    FieldPtr = 8
    Field = 16
    MethodPtr = 32
    MethodDef = 64
    ParamPtr = 128
    Param = 256
    InterfaceImpl = 512
    MemberRef = 1024
    Constant = 2048
    CustomAttribute = 4096
    FieldMarshal = 8192
    DeclSecurity = 16384
    ClassLayout = 32768
    FieldLayout = 65536
    StandAloneSig = 131072
    EventMap = 262144
    EventPtr = 524288
    Event = 1048576
    PropertyMap = 2097152
    PropertyPtr = 4194304
    Property = 8388608
    MethodSemantics = 16777216
    MethodImpl = 33554432
    ModuleRef = 67108864
    TypeSpec = 134217728
    ImplMap = 268435456
    FieldRva = 536870912
    EnCLog = 1073741824
    EnCMap = 2147483648
    Assembly = 4294967296
    AssemblyRef = 34359738368
    File = 274877906944
    ExportedType = 549755813888
    ManifestResource = 1099511627776
    NestedClass = 2199023255552
    GenericParam = 4398046511104
    MethodSpec = 8796093022208
    GenericParamConstraint = 17592186044416
    Document = 281474976710656
    MethodDebugInformation = 562949953421312
    LocalScope = 1125899906842624
    LocalVariable = 2251799813685248
    LocalConstant = 4503599627370496
    ImportScope = 9007199254740992
    StateMachineMethod = 18014398509481984
    CustomDebugInformation = 36028797018963968
    PtrTables = 4718760
    EncTables = 3221225472
    TypeSystemTables = 34952443854847
    DebugTables = 71776119061217280
    AllTables = 71811071505072127
    ValidPortablePdbExternalTables = 34949217910615

# System.Reflection.Metadata.Ecma335.TypeDefTreatment
class TypeDefTreatment(IntFlag):
    NONE = 0
    KindMask = 15
    NormalNonAttribute = 1
    NormalAttribute = 2
    UnmangleWinRTName = 3
    PrefixWinRTName = 4
    RedirectedToClrType = 5
    RedirectedToClrAttribute = 6
    MarkAbstractFlag = 16
    MarkInternalFlag = 32

# System.Reflection.Metadata.Ecma335.TypeRefSignatureTreatment
class TypeRefSignatureTreatment(IntFlag):
    NONE = 0
    ProjectedToClass = 1
    ProjectedToValueType = 2

# System.Reflection.Metadata.Ecma335.TypeRefTreatment
class TypeRefTreatment(IntFlag):
    NONE = 0
    SystemDelegate = 1
    SystemAttribute = 2
    UseProjectionInfo = 3

