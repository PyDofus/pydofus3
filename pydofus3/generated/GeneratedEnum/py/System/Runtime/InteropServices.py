from enum import IntFlag

# System.Runtime.InteropServices.Architecture
class Architecture(IntFlag):
    X86 = 0
    X64 = 1
    Arm = 2
    Arm64 = 3

# System.Runtime.InteropServices.CallingConvention
class CallingConvention(IntFlag):
    Winapi = 1
    Cdecl = 2
    StdCall = 3
    ThisCall = 4
    FastCall = 5

# System.Runtime.InteropServices.CharSet
class CharSet(IntFlag):
    NONE = 1
    Ansi = 2
    Unicode = 3
    Auto = 4

# System.Runtime.InteropServices.ClassInterfaceType
class ClassInterfaceType(IntFlag):
    NONE = 0
    AutoDispatch = 1
    AutoDual = 2

# System.Runtime.InteropServices.ComInterfaceType
class ComInterfaceType(IntFlag):
    InterfaceIsDual = 0
    InterfaceIsIUnknown = 1
    InterfaceIsIDispatch = 2
    InterfaceIsIInspectable = 3

# System.Runtime.InteropServices.DllImportSearchPath
class DllImportSearchPath(IntFlag):
    UseDllDirectoryForDependencies = 256
    ApplicationDirectory = 512
    UserDirectories = 1024
    System32 = 2048
    SafeDirectories = 4096
    AssemblyDirectory = 2
    LegacyBehavior = 0

# System.Runtime.InteropServices.GCHandleType
class GCHandleType(IntFlag):
    Weak = 0
    WeakTrackResurrection = 1
    Normal = 2
    Pinned = 3

# System.Runtime.InteropServices.LayoutKind
class LayoutKind(IntFlag):
    Sequential = 0
    Explicit = 2
    Auto = 3

# System.Runtime.InteropServices.UnmanagedType
class UnmanagedType(IntFlag):
    Bool = 2
    I1 = 3
    U1 = 4
    I2 = 5
    U2 = 6
    I4 = 7
    U4 = 8
    I8 = 9
    U8 = 10
    R4 = 11
    R8 = 12
    Currency = 15
    BStr = 19
    LPStr = 20
    LPWStr = 21
    LPTStr = 22
    ByValTStr = 23
    IUnknown = 25
    IDispatch = 26
    Struct = 27
    Interface = 28
    SafeArray = 29
    ByValArray = 30
    SysInt = 31
    SysUInt = 32
    VBByRefStr = 34
    AnsiBStr = 35
    TBStr = 36
    VariantBool = 37
    FunctionPtr = 38
    AsAny = 40
    LPArray = 42
    LPStruct = 43
    CustomMarshaler = 44
    Error = 45
    IInspectable = 46
    HString = 47
    LPUTF8Str = 48

# System.Runtime.InteropServices.VarEnum
class VarEnum(IntFlag):
    VT_EMPTY = 0
    VT_NULL = 1
    VT_I2 = 2
    VT_I4 = 3
    VT_R4 = 4
    VT_R8 = 5
    VT_CY = 6
    VT_DATE = 7
    VT_BSTR = 8
    VT_DISPATCH = 9
    VT_ERROR = 10
    VT_BOOL = 11
    VT_VARIANT = 12
    VT_UNKNOWN = 13
    VT_DECIMAL = 14
    VT_I1 = 16
    VT_UI1 = 17
    VT_UI2 = 18
    VT_UI4 = 19
    VT_I8 = 20
    VT_UI8 = 21
    VT_INT = 22
    VT_UINT = 23
    VT_VOID = 24
    VT_HRESULT = 25
    VT_PTR = 26
    VT_SAFEARRAY = 27
    VT_CARRAY = 28
    VT_USERDEFINED = 29
    VT_LPSTR = 30
    VT_LPWSTR = 31
    VT_RECORD = 36
    VT_FILETIME = 64
    VT_BLOB = 65
    VT_STREAM = 66
    VT_STORAGE = 67
    VT_STREAMED_OBJECT = 68
    VT_STORED_OBJECT = 69
    VT_BLOB_OBJECT = 70
    VT_CF = 71
    VT_CLSID = 72
    VT_VECTOR = 4096
    VT_ARRAY = 8192
    VT_BYREF = 16384

