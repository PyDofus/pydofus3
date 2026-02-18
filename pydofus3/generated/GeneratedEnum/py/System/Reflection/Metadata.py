from enum import IntFlag

# System.Reflection.Metadata.AssemblyReferenceHandle
class AssemblyReferenceHandle(IntFlag):
    System_Runtime = 0
    System_Runtime_InteropServices_WindowsRuntime = 1
    System_ObjectModel = 2
    System_Runtime_WindowsRuntime = 3
    System_Runtime_WindowsRuntime_UI_Xaml = 4
    System_Numerics_Vectors = 5
    Count = 6

# System.Reflection.Metadata.BlobHandle
class BlobHandle(IntFlag):
    Nil = 0
    ContractPublicKeyToken = 1
    ContractPublicKey = 2
    AttributeUsage_AllowSingle = 3
    AttributeUsage_AllowMultiple = 4
    Count = 5

# System.Reflection.Metadata.ConstantTypeCode
class ConstantTypeCode(IntFlag):
    Invalid = 0
    Boolean = 2
    Char = 3
    SByte = 4
    Byte = 5
    Int16 = 6
    UInt16 = 7
    Int32 = 8
    UInt32 = 9
    Int64 = 10
    UInt64 = 11
    Single = 12
    Double = 13
    String = 14
    NullReference = 18

# System.Reflection.Metadata.CustomAttributeNamedArgumentKind
class CustomAttributeNamedArgumentKind(IntFlag):
    Field = 83
    Property = 84

# System.Reflection.Metadata.ExceptionRegionKind
class ExceptionRegionKind(IntFlag):
    Catch = 0
    Filter = 1
    Finally = 2
    Fault = 4

# System.Reflection.Metadata.HandleKind
class HandleKind(IntFlag):
    ModuleDefinition = 0
    TypeReference = 1
    TypeDefinition = 2
    FieldDefinition = 4
    MethodDefinition = 6
    Parameter = 8
    InterfaceImplementation = 9
    MemberReference = 10
    Constant = 11
    CustomAttribute = 12
    DeclarativeSecurityAttribute = 14
    StandaloneSignature = 17
    EventDefinition = 20
    PropertyDefinition = 23
    MethodImplementation = 25
    ModuleReference = 26
    TypeSpecification = 27
    AssemblyDefinition = 32
    AssemblyFile = 38
    AssemblyReference = 35
    ExportedType = 39
    GenericParameter = 42
    MethodSpecification = 43
    GenericParameterConstraint = 44
    ManifestResource = 40
    Document = 48
    MethodDebugInformation = 49
    LocalScope = 50
    LocalVariable = 51
    LocalConstant = 52
    ImportScope = 53
    CustomDebugInformation = 55
    NamespaceDefinition = 124
    UserString = 112
    String = 120
    Blob = 113
    Guid = 114

# System.Reflection.Metadata.ILOpCode
class ILOpCode(IntFlag):
    Nop = 0
    Break = 1
    Ldarg_0 = 2
    Ldarg_1 = 3
    Ldarg_2 = 4
    Ldarg_3 = 5
    Ldloc_0 = 6
    Ldloc_1 = 7
    Ldloc_2 = 8
    Ldloc_3 = 9
    Stloc_0 = 10
    Stloc_1 = 11
    Stloc_2 = 12
    Stloc_3 = 13
    Ldarg_s = 14
    Ldarga_s = 15
    Starg_s = 16
    Ldloc_s = 17
    Ldloca_s = 18
    Stloc_s = 19
    Ldnull = 20
    Ldc_i4_m1 = 21
    Ldc_i4_0 = 22
    Ldc_i4_1 = 23
    Ldc_i4_2 = 24
    Ldc_i4_3 = 25
    Ldc_i4_4 = 26
    Ldc_i4_5 = 27
    Ldc_i4_6 = 28
    Ldc_i4_7 = 29
    Ldc_i4_8 = 30
    Ldc_i4_s = 31
    Ldc_i4 = 32
    Ldc_i8 = 33
    Ldc_r4 = 34
    Ldc_r8 = 35
    Dup = 37
    Pop = 38
    Jmp = 39
    Call = 40
    Calli = 41
    Ret = 42
    Br_s = 43
    Brfalse_s = 44
    Brtrue_s = 45
    Beq_s = 46
    Bge_s = 47
    Bgt_s = 48
    Ble_s = 49
    Blt_s = 50
    Bne_un_s = 51
    Bge_un_s = 52
    Bgt_un_s = 53
    Ble_un_s = 54
    Blt_un_s = 55
    Br = 56
    Brfalse = 57
    Brtrue = 58
    Beq = 59
    Bge = 60
    Bgt = 61
    Ble = 62
    Blt = 63
    Bne_un = 64
    Bge_un = 65
    Bgt_un = 66
    Ble_un = 67
    Blt_un = 68
    Switch = 69
    Ldind_i1 = 70
    Ldind_u1 = 71
    Ldind_i2 = 72
    Ldind_u2 = 73
    Ldind_i4 = 74
    Ldind_u4 = 75
    Ldind_i8 = 76
    Ldind_i = 77
    Ldind_r4 = 78
    Ldind_r8 = 79
    Ldind_ref = 80
    Stind_ref = 81
    Stind_i1 = 82
    Stind_i2 = 83
    Stind_i4 = 84
    Stind_i8 = 85
    Stind_r4 = 86
    Stind_r8 = 87
    Add = 88
    Sub = 89
    Mul = 90
    Div = 91
    Div_un = 92
    Rem = 93
    Rem_un = 94
    And = 95
    Or = 96
    Xor = 97
    Shl = 98
    Shr = 99
    Shr_un = 100
    Neg = 101
    Not = 102
    Conv_i1 = 103
    Conv_i2 = 104
    Conv_i4 = 105
    Conv_i8 = 106
    Conv_r4 = 107
    Conv_r8 = 108
    Conv_u4 = 109
    Conv_u8 = 110
    Callvirt = 111
    Cpobj = 112
    Ldobj = 113
    Ldstr = 114
    Newobj = 115
    Castclass = 116
    Isinst = 117
    Conv_r_un = 118
    Unbox = 121
    Throw = 122
    Ldfld = 123
    Ldflda = 124
    Stfld = 125
    Ldsfld = 126
    Ldsflda = 127
    Stsfld = 128
    Stobj = 129
    Conv_ovf_i1_un = 130
    Conv_ovf_i2_un = 131
    Conv_ovf_i4_un = 132
    Conv_ovf_i8_un = 133
    Conv_ovf_u1_un = 134
    Conv_ovf_u2_un = 135
    Conv_ovf_u4_un = 136
    Conv_ovf_u8_un = 137
    Conv_ovf_i_un = 138
    Conv_ovf_u_un = 139
    Box = 140
    Newarr = 141
    Ldlen = 142
    Ldelema = 143
    Ldelem_i1 = 144
    Ldelem_u1 = 145
    Ldelem_i2 = 146
    Ldelem_u2 = 147
    Ldelem_i4 = 148
    Ldelem_u4 = 149
    Ldelem_i8 = 150
    Ldelem_i = 151
    Ldelem_r4 = 152
    Ldelem_r8 = 153
    Ldelem_ref = 154
    Stelem_i = 155
    Stelem_i1 = 156
    Stelem_i2 = 157
    Stelem_i4 = 158
    Stelem_i8 = 159
    Stelem_r4 = 160
    Stelem_r8 = 161
    Stelem_ref = 162
    Ldelem = 163
    Stelem = 164
    Unbox_any = 165
    Conv_ovf_i1 = 179
    Conv_ovf_u1 = 180
    Conv_ovf_i2 = 181
    Conv_ovf_u2 = 182
    Conv_ovf_i4 = 183
    Conv_ovf_u4 = 184
    Conv_ovf_i8 = 185
    Conv_ovf_u8 = 186
    Refanyval = 194
    Ckfinite = 195
    Mkrefany = 198
    Ldtoken = 208
    Conv_u2 = 209
    Conv_u1 = 210
    Conv_i = 211
    Conv_ovf_i = 212
    Conv_ovf_u = 213
    Add_ovf = 214
    Add_ovf_un = 215
    Mul_ovf = 216
    Mul_ovf_un = 217
    Sub_ovf = 218
    Sub_ovf_un = 219
    Endfinally = 220
    Leave = 221
    Leave_s = 222
    Stind_i = 223
    Conv_u = 224
    Arglist = 65024
    Ceq = 65025
    Cgt = 65026
    Cgt_un = 65027
    Clt = 65028
    Clt_un = 65029
    Ldftn = 65030
    Ldvirtftn = 65031
    Ldarg = 65033
    Ldarga = 65034
    Starg = 65035
    Ldloc = 65036
    Ldloca = 65037
    Stloc = 65038
    Localloc = 65039
    Endfilter = 65041
    Unaligned = 65042
    Volatile = 65043
    Tail = 65044
    Initobj = 65045
    Constrained = 65046
    Cpblk = 65047
    Initblk = 65048
    Rethrow = 65050
    Sizeof = 65052
    Refanytype = 65053
    Readonly = 65054

# System.Reflection.Metadata.ImportDefinitionKind
class ImportDefinitionKind(IntFlag):
    ImportNamespace = 1
    ImportAssemblyNamespace = 2
    ImportType = 3
    ImportXmlNamespace = 4
    ImportAssemblyReferenceAlias = 5
    AliasAssemblyReference = 6
    AliasNamespace = 7
    AliasAssemblyNamespace = 8
    AliasType = 9

# System.Reflection.Metadata.LocalVariableAttributes
class LocalVariableAttributes(IntFlag):
    NONE = 0
    DebuggerHidden = 1

# System.Reflection.Metadata.MemberReferenceKind
class MemberReferenceKind(IntFlag):
    Method = 0
    Field = 1

# System.Reflection.Metadata.MetadataKind
class MetadataKind(IntFlag):
    Ecma335 = 0
    WindowsMetadata = 1
    ManagedWindowsMetadata = 2

# System.Reflection.Metadata.MetadataReaderOptions
class MetadataReaderOptions(IntFlag):
    NONE = 0
    Default = 1
    ApplyWindowsRuntimeProjections = 1

# System.Reflection.Metadata.MetadataStreamOptions
class MetadataStreamOptions(IntFlag):
    Default = 0
    LeaveOpen = 1
    PrefetchMetadata = 2

# System.Reflection.Metadata.PrimitiveSerializationTypeCode
class PrimitiveSerializationTypeCode(IntFlag):
    Boolean = 2
    Byte = 5
    SByte = 4
    Char = 3
    Int16 = 6
    UInt16 = 7
    Int32 = 8
    UInt32 = 9
    Int64 = 10
    UInt64 = 11
    Single = 12
    Double = 13
    String = 14

# System.Reflection.Metadata.PrimitiveTypeCode
class PrimitiveTypeCode(IntFlag):
    Boolean = 2
    Byte = 5
    SByte = 4
    Char = 3
    Int16 = 6
    UInt16 = 7
    Int32 = 8
    UInt32 = 9
    Int64 = 10
    UInt64 = 11
    Single = 12
    Double = 13
    IntPtr = 24
    UIntPtr = 25
    Object = 28
    String = 14
    TypedReference = 22
    Void = 1

# System.Reflection.Metadata.SerializationTypeCode
class SerializationTypeCode(IntFlag):
    Invalid = 0
    Boolean = 2
    Char = 3
    SByte = 4
    Byte = 5
    Int16 = 6
    UInt16 = 7
    Int32 = 8
    UInt32 = 9
    Int64 = 10
    UInt64 = 11
    Single = 12
    Double = 13
    String = 14
    SZArray = 29
    Type = 80
    TaggedObject = 81
    Enum = 85

# System.Reflection.Metadata.SignatureAttributes
class SignatureAttributes(IntFlag):
    NONE = 0
    Generic = 16
    Instance = 32
    ExplicitThis = 64

# System.Reflection.Metadata.SignatureCallingConvention
class SignatureCallingConvention(IntFlag):
    Default = 0
    CDecl = 1
    StdCall = 2
    ThisCall = 3
    FastCall = 4
    VarArgs = 5
    Unmanaged = 9

# System.Reflection.Metadata.SignatureKind
class SignatureKind(IntFlag):
    Method = 0
    Field = 6
    LocalVariables = 7
    Property = 8
    MethodSpecification = 10

# System.Reflection.Metadata.SignatureTypeCode
class SignatureTypeCode(IntFlag):
    Invalid = 0
    Void = 1
    Boolean = 2
    Char = 3
    SByte = 4
    Byte = 5
    Int16 = 6
    UInt16 = 7
    Int32 = 8
    UInt32 = 9
    Int64 = 10
    UInt64 = 11
    Single = 12
    Double = 13
    String = 14
    Pointer = 15
    ByReference = 16
    GenericTypeParameter = 19
    Array = 20
    GenericTypeInstance = 21
    TypedReference = 22
    IntPtr = 24
    UIntPtr = 25
    FunctionPointer = 27
    Object = 28
    SZArray = 29
    GenericMethodParameter = 30
    RequiredModifier = 31
    OptionalModifier = 32
    TypeHandle = 64
    Sentinel = 65
    Pinned = 69

# System.Reflection.Metadata.SignatureTypeKind
class SignatureTypeKind(IntFlag):
    Unknown = 0
    Class = 18
    ValueType = 17

# System.Reflection.Metadata.StandaloneSignatureKind
class StandaloneSignatureKind(IntFlag):
    Method = 0
    LocalVariables = 1

# System.Reflection.Metadata.StringHandle
class StringHandle(IntFlag):
    System_Runtime_WindowsRuntime = 0
    System_Runtime = 1
    System_ObjectModel = 2
    System_Runtime_WindowsRuntime_UI_Xaml = 3
    System_Runtime_InteropServices_WindowsRuntime = 4
    System_Numerics_Vectors = 5
    Dispose = 6
    AttributeTargets = 7
    AttributeUsageAttribute = 8
    Color = 9
    CornerRadius = 10
    DateTimeOffset = 11
    Duration = 12
    DurationType = 13
    EventHandler1 = 14
    EventRegistrationToken = 15
    Exception = 16
    GeneratorPosition = 17
    GridLength = 18
    GridUnitType = 19
    ICommand = 20
    IDictionary2 = 21
    IDisposable = 22
    IEnumerable = 23
    IEnumerable1 = 24
    IList = 25
    IList1 = 26
    INotifyCollectionChanged = 27
    INotifyPropertyChanged = 28
    IReadOnlyDictionary2 = 29
    IReadOnlyList1 = 30
    KeyTime = 31
    KeyValuePair2 = 32
    Matrix = 33
    Matrix3D = 34
    Matrix3x2 = 35
    Matrix4x4 = 36
    NotifyCollectionChangedAction = 37
    NotifyCollectionChangedEventArgs = 38
    NotifyCollectionChangedEventHandler = 39
    Nullable1 = 40
    Plane = 41
    Point = 42
    PropertyChangedEventArgs = 43
    PropertyChangedEventHandler = 44
    Quaternion = 45
    Rect = 46
    RepeatBehavior = 47
    RepeatBehaviorType = 48
    Size = 49
    System = 50
    System_Collections = 51
    System_Collections_Generic = 52
    System_Collections_Specialized = 53
    System_ComponentModel = 54
    System_Numerics = 55
    System_Windows_Input = 56
    Thickness = 57
    TimeSpan = 58
    Type = 59
    Uri = 60
    Vector2 = 61
    Vector3 = 62
    Vector4 = 63
    Windows_Foundation = 64
    Windows_UI = 65
    Windows_UI_Xaml = 66
    Windows_UI_Xaml_Controls_Primitives = 67
    Windows_UI_Xaml_Media = 68
    Windows_UI_Xaml_Media_Animation = 69
    Windows_UI_Xaml_Media_Media3D = 70
    Count = 71

