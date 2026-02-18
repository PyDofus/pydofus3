from enum import IntFlag

# Mono.CSharp.AddressOp
class AddressOp(IntFlag):
    Store = 1
    Load = 2
    LoadStore = 3

# Mono.CSharp.Argument
class Argument(IntFlag):
    NONE = 0
    Ref = 1
    Out = 2
    Default = 3
    DynamicTypeName = 4
    ExtensionType = 5
    ExtensionTypeConditionalAccess = 133
    ConditionalAccessFlag = 128

# Mono.CSharp.AttributeEncoder
class AttributeEncoder(IntFlag):
    NONE = 0
    DynamicType = 1
    TypeParameter = 2

# Mono.CSharp.Binary
class Binary(IntFlag):
    Multiply = 32
    Division = 33
    Modulus = 34
    Addition = 2083
    Subtraction = 4132
    LeftShift = 69
    RightShift = 70
    LessThan = 8327
    GreaterThan = 8328
    LessThanOrEqual = 8329
    GreaterThanOrEqual = 8330
    Equality = 395
    Inequality = 396
    BitwiseAnd = 525
    ExclusiveOr = 526
    BitwiseOr = 527
    LogicalAnd = 1040
    LogicalOr = 1041
    ValuesOnlyMask = 31
    ArithmeticMask = 32
    ShiftMask = 64
    ComparisonMask = 128
    EqualityMask = 256
    BitwiseMask = 512
    LogicalMask = 1024
    AdditionMask = 2048
    SubtractionMask = 4096
    RelationalMask = 8192
    DecomposedMask = 524288
    NullableMask = 1048576

# Mono.CSharp.Binary
class Binary(IntFlag):
    NONE = 0
    Compound = 2
    UserOperatorsExcluded = 4

# Mono.CSharp.BindingRestriction
class BindingRestriction(IntFlag):
    NONE = 0
    DeclaredOnly = 2
    InstanceOnly = 4
    NoAccessors = 8
    OverrideOnly = 16

# Mono.CSharp.Block
class Block(IntFlag):
    Unchecked = 1
    ReachableEnd = 8
    Unsafe = 16
    HasCapturedVariable = 64
    HasCapturedThis = 128
    IsExpressionTree = 256
    CompilerGenerated = 512
    HasAsyncModifier = 1024
    Resolved = 2048
    YieldBlock = 4096
    AwaitBlock = 8192
    FinallyBlock = 16384
    CatchBlock = 32768
    Iterator = 1048576
    NoFlowAnalysis = 2097152
    InitializationEmitted = 4194304

# Mono.CSharp.BuilderContext
class BuilderContext(IntFlag):
    CheckedScope = 1
    AccurateDebugInfo = 2
    OmitDebugInfo = 4
    ConstructorScope = 8
    AsyncBody = 16

# Mono.CSharp.BuiltinTypeSpec
class BuiltinTypeSpec(IntFlag):
    NONE = 0
    FirstPrimitive = 1
    Bool = 1
    Byte = 2
    SByte = 3
    Char = 4
    Short = 5
    UShort = 6
    Int = 7
    UInt = 8
    Long = 9
    ULong = 10
    Float = 11
    Double = 12
    LastPrimitive = 12
    Decimal = 13
    IntPtr = 14
    UIntPtr = 15
    Object = 16
    Dynamic = 17
    String = 18
    Type = 19
    ValueType = 20
    Enum = 21
    Delegate = 22
    MulticastDelegate = 23
    Array = 24
    IEnumerator = 25
    IEnumerable = 26
    IDisposable = 27
    Exception = 28
    Attribute = 29
    Other = 30

# Mono.CSharp.CSharpBinderFlags
class CSharpBinderFlags(IntFlag):
    NONE = 0
    CheckedContext = 1
    InvokeSimpleName = 2
    InvokeSpecialName = 4
    BinaryOperationLogical = 8
    ConvertExplicit = 16
    ConvertArrayIndex = 32
    ResultIndexed = 64
    ValueFromCompoundAssignment = 128
    ResultDiscarded = 256

# Mono.CSharp.CSharpParser
class CSharpParser(IntFlag):
    Ref = 2
    Out = 4
    This = 8
    Params = 16
    Arglist = 32
    DefaultValue = 64
    All = 126
    PrimaryConstructor = 86

# Mono.CSharp.CommandLineParser
class CommandLineParser(IntFlag):
    Success = 0
    Error = 1
    Stop = 2
    UnknownOption = 3

# Mono.CSharp.ConvCast
class ConvCast(IntFlag):
    I1_U1 = 0
    I1_U2 = 1
    I1_U4 = 2
    I1_U8 = 3
    I1_CH = 4
    U1_I1 = 5
    U1_CH = 6
    I2_I1 = 7
    I2_U1 = 8
    I2_U2 = 9
    I2_U4 = 10
    I2_U8 = 11
    I2_CH = 12
    U2_I1 = 13
    U2_U1 = 14
    U2_I2 = 15
    U2_CH = 16
    I4_I1 = 17
    I4_U1 = 18
    I4_I2 = 19
    I4_U2 = 20
    I4_U4 = 21
    I4_U8 = 22
    I4_CH = 23
    U4_I1 = 24
    U4_U1 = 25
    U4_I2 = 26
    U4_U2 = 27
    U4_I4 = 28
    U4_CH = 29
    I8_I1 = 30
    I8_U1 = 31
    I8_I2 = 32
    I8_U2 = 33
    I8_I4 = 34
    I8_U4 = 35
    I8_U8 = 36
    I8_CH = 37
    I8_I = 38
    U8_I1 = 39
    U8_U1 = 40
    U8_I2 = 41
    U8_U2 = 42
    U8_I4 = 43
    U8_U4 = 44
    U8_I8 = 45
    U8_CH = 46
    U8_I = 47
    CH_I1 = 48
    CH_U1 = 49
    CH_I2 = 50
    R4_I1 = 51
    R4_U1 = 52
    R4_I2 = 53
    R4_U2 = 54
    R4_I4 = 55
    R4_U4 = 56
    R4_I8 = 57
    R4_U8 = 58
    R4_CH = 59
    R8_I1 = 60
    R8_U1 = 61
    R8_I2 = 62
    R8_U2 = 63
    R8_I4 = 64
    R8_U4 = 65
    R8_I8 = 66
    R8_U8 = 67
    R8_CH = 68
    R8_R4 = 69
    I_I8 = 70

# Mono.CSharp.Convert
class Convert(IntFlag):
    NONE = 0
    ImplicitOnly = 1
    ProbingOnly = 2
    NullableSourceOnly = 4

# Mono.CSharp.Evaluator
class Evaluator(IntFlag):
    Silent = 0
    ReportErrors = 1
    GetCompletions = 2

# Mono.CSharp.Evaluator
class Evaluator(IntFlag):
    EOF = 0
    StatementOrExpression = 1
    CompilationUnit = 2
    Error = 3

# Mono.CSharp.ExprClass
class ExprClass(IntFlag):
    Unresolved = 0
    Value = 1
    Variable = 2
    Namespace = 3
    Type = 4
    TypeParameter = 5
    MethodGroup = 6
    PropertyAccess = 7
    EventAccess = 8
    IndexerAccess = 9
    Nothing = 10

# Mono.CSharp.Expression
class Expression(IntFlag):
    NONE = 0
    InvocableOnly = 1
    ExactArity = 4
    ReadAccess = 8
    EmptyArguments = 16
    IgnoreArity = 32
    IgnoreAmbiguity = 64
    NameOfExcluded = 128

# Mono.CSharp.FieldBase
class FieldBase(IntFlag):
    HAS_OFFSET = 4

# Mono.CSharp.LanguageVersion
class LanguageVersion(IntFlag):
    ISO_1 = 1
    ISO_2 = 2
    V_3 = 3
    V_4 = 4
    V_5 = 5
    V_6 = 6
    Experimental = 100
    Default = 6

# Mono.CSharp.LocalVariable
class LocalVariable(IntFlag):
    Used = 1
    IsThis = 2
    AddressTaken = 4
    CompilerGenerated = 8
    Constant = 16
    ForeachVariable = 32
    FixedVariable = 64
    UsingVariable = 128
    IsLocked = 256
    ReadonlyMask = 224

# Mono.CSharp.LookupMode
class LookupMode(IntFlag):
    Normal = 0
    Probing = 1
    IgnoreAccessibility = 2

# Mono.CSharp.MemberCache
class MemberCache(IntFlag):
    HasConversionOperator = 2
    HasUserOperator = 4

# Mono.CSharp.MemberCore
class MemberCore(IntFlag):
    Obsolete_Undetected = 1
    Obsolete = 2
    ClsCompliance_Undetected = 4
    ClsCompliant = 8
    CloseTypeCreated = 16
    HasCompliantAttribute_Undetected = 32
    HasClsCompliantAttribute = 64
    ClsCompliantAttributeFalse = 128
    Excluded_Undetected = 256
    Excluded = 512
    MethodOverloadsExist = 1024
    IsUsed = 2048
    IsAssigned = 4096
    HasExplicitLayout = 8192
    PartialDefinitionExists = 16384
    HasStructLayout = 32768
    HasInstanceConstructor = 65536
    HasUserOperators = 131072
    CanBeReused = 262144
    InterfacesExpanded = 524288

# Mono.CSharp.MemberKind
class MemberKind(IntFlag):
    Constructor = 1
    Event = 2
    Field = 4
    Method = 8
    Property = 16
    Indexer = 32
    Operator = 64
    Destructor = 128
    Class = 2048
    Struct = 4096
    Delegate = 8192
    Enum = 16384
    Interface = 32768
    TypeParameter = 65536
    ArrayType = 524288
    PointerType = 1048576
    InternalCompilerType = 2097152
    MissingType = 4194304
    Void = 8388608
    Namespace = 16777216
    NestedMask = 63488
    GenericMask = 47112
    MaskType = 63743

# Mono.CSharp.MemberSpec
class MemberSpec(IntFlag):
    Obsolete_Undetected = 1
    Obsolete = 2
    CLSCompliant_Undetected = 4
    CLSCompliant = 8
    MissingDependency_Undetected = 16
    MissingDependency = 32
    HasDynamicElement = 64
    ConstraintsChecked = 128
    IsAccessor = 512
    IsGeneric = 1024
    PendingMetaInflate = 4096
    PendingMakeMethod = 8192
    PendingMemberCacheMembers = 16384
    PendingBaseTypeInflate = 32768
    InterfacesExpanded = 65536
    IsNotCSharpCompatible = 131072
    SpecialRuntimeType = 262144
    InflatedExpressionType = 524288
    InflatedNullableType = 1048576
    GenericIterateInterface = 2097152
    GenericTask = 4194304
    InterfacesImported = 8388608

# Mono.CSharp.Modifiers
class Modifiers(IntFlag):
    PROTECTED = 1
    PUBLIC = 2
    PRIVATE = 4
    INTERNAL = 8
    NEW = 16
    ABSTRACT = 32
    SEALED = 64
    STATIC = 128
    READONLY = 256
    VIRTUAL = 512
    OVERRIDE = 1024
    EXTERN = 2048
    VOLATILE = 4096
    UNSAFE = 8192
    ASYNC = 16384
    TOP = 32768
    PROPERTY_CUSTOM = 65536
    PARTIAL = 131072
    DEFAULT_ACCESS_MODIFIER = 262144
    METHOD_EXTENSION = 524288
    COMPILER_GENERATED = 1048576
    BACKING_FIELD = 2097152
    DEBUGGER_HIDDEN = 4194304
    DEBUGGER_STEP_THROUGH = 8388608
    AutoProperty = 16777216
    AccessibilityMask = 15
    AllowedExplicitImplFlags = 10240

# Mono.CSharp.Operator
class Operator(IntFlag):
    LogicalNot = 0
    OnesComplement = 1
    Increment = 2
    Decrement = 3
    TRUE = 4
    FALSE = 5
    Addition = 6
    Subtraction = 7
    UnaryPlus = 8
    UnaryNegation = 9
    Multiply = 10
    Division = 11
    Modulus = 12
    BitwiseAnd = 13
    BitwiseOr = 14
    ExclusiveOr = 15
    LeftShift = 16
    RightShift = 17
    Equality = 18
    Inequality = 19
    GreaterThan = 20
    LessThan = 21
    GreaterThanOrEqual = 22
    LessThanOrEqual = 23
    Implicit = 24
    Explicit = 25
    Is = 26
    TOP = 27

# Mono.CSharp.OverloadResolver
class OverloadResolver(IntFlag):
    NONE = 0
    DelegateInvoke = 1
    ProbingOnly = 2
    CovariantDelegate = 4
    NoBaseMembers = 8
    BaseMembersIncluded = 16
    GetEnumeratorLookup = 32

# Mono.CSharp.Parameter
class Parameter(IntFlag):
    NONE = 0
    PARAMS = 1
    REF = 2
    OUT = 4
    This = 8
    CallerMemberName = 16
    CallerLineNumber = 32
    CallerFilePath = 64
    RefOutMask = 6
    ModifierMask = 15
    CallerMask = 112

# Mono.CSharp.PendingImplementation
class PendingImplementation(IntFlag):
    Lookup = 0
    ClearOne = 1
    ClearAll = 2

# Mono.CSharp.Platform
class Platform(IntFlag):
    AnyCPU = 0
    AnyCPU32Preferred = 1
    Arm = 2
    X86 = 3
    X64 = 4
    IA64 = 5

# Mono.CSharp.ResolveContext
class ResolveContext(IntFlag):
    CheckedScope = 1
    ConstantCheckState = 2
    AllCheckStateFlags = 3
    UnsafeScope = 4
    CatchScope = 8
    FinallyScope = 16
    FieldInitializerScope = 32
    CompoundAssignmentScope = 64
    FixedInitializerScope = 128
    BaseInitializer = 256
    EnumScope = 512
    ConstantScope = 1024
    ConstructorScope = 2048
    UsingInitializerScope = 4096
    LockScope = 8192
    TryScope = 16384
    TryWithCatchScope = 32768
    ConditionalAccessReceiver = 65536
    ProbingMode = 4194304
    InferReturnType = 8388608
    OmitDebuggingInfo = 16777216
    ExpressionTreeConversion = 33554432
    InvokeSpecialName = 67108864

# Mono.CSharp.ResolveFlags
class ResolveFlags(IntFlag):
    VariableOrValue = 1
    Type = 2
    MethodGroup = 4
    TypeParameter = 8
    MaskExprClass = 15

# Mono.CSharp.RuntimeVersion
class RuntimeVersion(IntFlag):
    v1 = 0
    v2 = 1
    v4 = 2

# Mono.CSharp.SpecialConstraint
class SpecialConstraint(IntFlag):
    NONE = 0
    Constructor = 4
    Class = 8
    Struct = 16

# Mono.CSharp.StateMachine
class StateMachine(IntFlag):
    Running = -3
    Uninitialized = -2
    After = -1
    Start = 0

# Mono.CSharp.Target
class Target(IntFlag):
    Library = 0
    Exe = 1
    Module = 2
    WinExe = 3

# Mono.CSharp.TimeReporter
class TimeReporter(IntFlag):
    ParseTotal = 0
    AssemblyBuilderSetup = 1
    CreateTypeTotal = 2
    ReferencesLoading = 3
    ReferencesImporting = 4
    PredefinedTypesInit = 5
    ModuleDefinitionTotal = 6
    EmitTotal = 7
    CloseTypes = 8
    Resouces = 9
    OutputSave = 10
    DebugSave = 11

# Mono.CSharp.Tokenizer
class Tokenizer(IntFlag):
    Invalid = 0
    Region = 1
    Endregion = 2
    If = 2051
    Endif = 4
    Elif = 2053
    Else = 6
    Define = 2055
    Undef = 2056
    Error = 9
    Warning = 10
    Pragma = 1035
    Line = 1036
    CustomArgumentsParsing = 1024
    RequiresArgument = 2048

# Mono.CSharp.TypeDefinition
class TypeDefinition(IntFlag):
    Equals = 1
    GetHashCode = 2
    HasStaticFieldInitializer = 4

# Mono.CSharp.TypeInferenceContext
class TypeInferenceContext(IntFlag):
    Exact = 0
    Lower = 1
    Upper = 2

# Mono.CSharp.Unary
class Unary(IntFlag):
    UnaryPlus = 0
    UnaryNegation = 1
    LogicalNot = 2
    OnesComplement = 3
    AddressOf = 4
    TOP = 5

# Mono.CSharp.UnaryMutator
class UnaryMutator(IntFlag):
    IsIncrement = 0
    IsDecrement = 1
    IsPre = 0
    IsPost = 2
    PreIncrement = 0
    PreDecrement = 1
    PostIncrement = 2
    PostDecrement = 3

# Mono.CSharp.Variance
class Variance(IntFlag):
    NONE = 0
    Covariant = 1
    Contravariant = -1

# Mono.CSharp.XmlCommentState
class XmlCommentState(IntFlag):
    Allowed = 0
    NotAllowed = 1
    Error = 2

