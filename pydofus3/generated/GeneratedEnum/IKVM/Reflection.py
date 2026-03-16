from enum import IntEnum
from enum import IntFlag

class AssemblyComparisonResult(IntEnum):
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

class AssemblyContentType(IntEnum):
	Default = 0
	WindowsRuntime = 1

class AssemblyNameFlags(IntFlag):
	None_ = 0
	PublicKey = 1
	Retargetable = 256
	EnableJITcompileOptimizer = 16384
	EnableJITcompileTracking = 32768

class BindingFlags(IntFlag):
	Default = 0
	IgnoreCase = 1
	DeclaredOnly = 2
	Instance = 4
	Static = 8
	Public = 16
	NonPublic = 32
	FlattenHierarchy = 64

class CallingConventions(IntFlag):
	Standard = 1
	VarArgs = 2
	Any = 3
	HasThis = 32
	ExplicitThis = 64

class DllCharacteristics(IntFlag):
	HighEntropyVA = 32
	DynamicBase = 64
	NXCompat = 256
	NoSEH = 1024
	AppContainer = 4096
	TerminalServerAware = 32768

class EventAttributes(IntFlag):
	None_ = 0
	SpecialName = 512
	RTSpecialName = 1024
	ReservedMask = 1024

class ExceptionHandlingClauseOptions(IntFlag):
	Clause = 0
	Filter = 1
	Finally = 2
	Fault = 4

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

class GenericParameterAttributes(IntFlag):
	None_ = 0
	Covariant = 1
	Contravariant = 2
	VarianceMask = 3
	ReferenceTypeConstraint = 4
	NotNullableValueTypeConstraint = 8
	DefaultConstructorConstraint = 16
	SpecialConstraintMask = 28

class ImageFileMachine(IntEnum):
	I386 = 332
	ARM = 452
	IA64 = 512
	AMD64 = 34404

class ImplMapFlags(IntFlag):
	CharSetNotSpec = 0
	NoMangle = 1
	CharSetAnsi = 2
	CharSetUnicode = 4
	CharSetMask = 6
	CharSetAuto = 6
	BestFitOn = 16
	BestFitOff = 32
	SupportsLastError = 64
	CallConvWinapi = 256
	CallConvCdecl = 512
	CallConvStdcall = 768
	CallConvThiscall = 1024
	CallConvFastcall = 1280
	CallConvMask = 1792
	CharMapErrorOn = 4096
	CharMapErrorOff = 8192

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

class MethodAttributes(IntFlag):
	PrivateScope = 0
	ReuseSlot = 0
	Private = 1
	FamANDAssem = 2
	Assembly = 3
	Family = 4
	FamORAssem = 5
	Public = 6
	MemberAccessMask = 7
	UnmanagedExport = 8
	Static = 16
	Final = 32
	Virtual = 64
	HideBySig = 128
	VtableLayoutMask = 256
	NewSlot = 256
	CheckAccessOnOverride = 512
	Abstract = 1024
	SpecialName = 2048
	RTSpecialName = 4096
	PinvokeImpl = 8192
	HasSecurity = 16384
	RequireSecObject = 32768
	ReservedMask = 53248

class MethodImplAttributes(IntFlag):
	IL = 0
	Managed = 0
	Native = 1
	OPTIL = 2
	CodeTypeMask = 3
	Runtime = 3
	ManagedMask = 4
	Unmanaged = 4
	NoInlining = 8
	ForwardRef = 16
	Synchronized = 32
	NoOptimization = 64
	PreserveSig = 128
	AggressiveInlining = 256
	InternalCall = 4096
	MaxMethodImplVal = 65535

class ParameterAttributes(IntFlag):
	None_ = 0
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

class ParseAssemblyResult(IntEnum):
	OK = 0
	GenericError = 1
	DuplicateKey = 2

class PortableExecutableKinds(IntFlag):
	NotAPortableExecutableImage = 0
	ILOnly = 1
	Required32Bit = 2
	PE32Plus = 4
	Unmanaged32Bit = 8
	Preferred32Bit = 16

class ProcessorArchitecture(IntEnum):
	None_ = 0
	MSIL = 1
	X86 = 2
	IA64 = 3
	Amd64 = 4
	Arm = 5

class PropertyAttributes(IntFlag):
	None_ = 0
	SpecialName = 512
	RTSpecialName = 1024
	HasDefault = 4096

class ResourceAttributes(IntFlag):
	Public = 1
	Private = 2

class ResourceLocation(IntFlag):
	Embedded = 1
	ContainedInAnotherAssembly = 2
	ContainedInManifestFile = 4

class Type:
	class TypeFlags(IntFlag):
		ContainsMissingType_Unknown = 0
		IsGenericTypeDefinition = 1
		HasNestedTypes = 2
		Baked = 4
		ValueType = 8
		NotValueType = 16
		PotentialEnumOrValueType = 32
		EnumOrValueType = 64
		NotGenericTypeDefinition = 128
		ContainsMissingType_Pending = 256
		ContainsMissingType_Yes = 512
		ContainsMissingType_No = 768
		ContainsMissingType_Mask = 768
		PotentialBuiltIn = 1024
		BuiltIn = 2048

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

class UniverseOptions(IntFlag):
	None_ = 0
	EnableFunctionPointers = 1
	DisableFusion = 2
	DisablePseudoCustomAttributeRetrieval = 4
	DontProvideAutomaticDefaultConstructor = 8
	MetadataOnly = 16
	ResolveMissingMembers = 32
	DisableWindowsRuntimeProjection = 64
	DecodeVersionInfoAttributeBlobs = 128
	DeterministicOutput = 256

class WindowsRuntimeProjection:
	class ProjectionAssembly(IntEnum):
		System_Runtime = 0
		System_Runtime_InteropServices_WindowsRuntime = 1
		System_ObjectModel = 2
		System_Runtime_WindowsRuntime = 3
		System_Runtime_WindowsRuntime_UI_Xaml = 4
		Count = 5

