from enum import IntFlag

# Unity.Burst.Intrinsics.X86
class X86(IntFlag):
    EQ_OQ = 0
    LT_OS = 1
    LE_OS = 2
    UNORD_Q = 3
    NEQ_UQ = 4
    NLT_US = 5
    NLE_US = 6
    ORD_Q = 7
    EQ_UQ = 8
    NGE_US = 9
    NGT_US = 10
    FALSE_OQ = 11
    NEQ_OQ = 12
    GE_OS = 13
    GT_OS = 14
    TRUE_UQ = 15
    EQ_OS = 16
    LT_OQ = 17
    LE_OQ = 18
    UNORD_S = 19
    NEQ_US = 20
    NLT_UQ = 21
    NLE_UQ = 22
    ORD_S = 23
    EQ_US = 24
    NGE_UQ = 25
    NGT_UQ = 26
    FALSE_OS = 27
    NEQ_OS = 28
    GE_OQ = 29
    GT_OQ = 30
    TRUE_US = 31

# Unity.Burst.Intrinsics.X86
class X86(IntFlag):
    FlushToZero = 32768
    RoundingControlMask = 24576
    RoundToNearest = 0
    RoundDown = 8192
    RoundUp = 16384
    RoundTowardZero = 24576
    PrecisionMask = 4096
    UnderflowMask = 2048
    OverflowMask = 1024
    DivideByZeroMask = 512
    DenormalOperationMask = 256
    InvalidOperationMask = 128
    ExceptionMask = 8064
    DenormalsAreZeroes = 64
    PrecisionFlag = 32
    UnderflowFlag = 16
    OverflowFlag = 8
    DivideByZeroFlag = 4
    DenormalFlag = 2
    InvalidOperationFlag = 1
    FlagMask = 63

# Unity.Burst.Intrinsics.X86
class X86(IntFlag):
    FROUND_TO_NEAREST_INT = 0
    FROUND_TO_NEG_INF = 1
    FROUND_TO_POS_INF = 2
    FROUND_TO_ZERO = 3
    FROUND_CUR_DIRECTION = 4
    FROUND_RAISE_EXC = 0
    FROUND_NO_EXC = 8
    FROUND_NINT = 0
    FROUND_FLOOR = 1
    FROUND_CEIL = 2
    FROUND_TRUNC = 3
    FROUND_RINT = 4
    FROUND_NEARBYINT = 12
    FROUND_NINT_NOEXC = 8
    FROUND_FLOOR_NOEXC = 9
    FROUND_CEIL_NOEXC = 10
    FROUND_TRUNC_NOEXC = 11
    FROUND_RINT_NOEXC = 12

# Unity.Burst.Intrinsics.X86
class X86(IntFlag):
    UBYTE_OPS = 0
    UWORD_OPS = 1
    SBYTE_OPS = 2
    SWORD_OPS = 3
    CMP_EQUAL_ANY = 0
    CMP_RANGES = 4
    CMP_EQUAL_EACH = 8
    CMP_EQUAL_ORDERED = 12
    POSITIVE_POLARITY = 0
    NEGATIVE_POLARITY = 16
    MASKED_POSITIVE_POLARITY = 32
    MASKED_NEGATIVE_POLARITY = 48
    LEAST_SIGNIFICANT = 0
    MOST_SIGNIFICANT = 64
    BIT_MASK = 0
    UNIT_MASK = 64

