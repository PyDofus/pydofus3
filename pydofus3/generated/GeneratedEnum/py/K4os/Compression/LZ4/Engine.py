from enum import IntFlag

# K4os.Compression.LZ4.Engine.Algorithm
class Algorithm(IntFlag):
    X32 = 0
    X64 = 1

# K4os.Compression.LZ4.Engine.LL
class LL(IntFlag):
    notLimited = 0
    limitedOutput = 1
    fillOutput = 2

# K4os.Compression.LZ4.Engine.LL
class LL(IntFlag):
    clearedTable = 0
    byPtr = 1
    byU32 = 2
    byU16 = 3

# K4os.Compression.LZ4.Engine.LL
class LL(IntFlag):
    noDict = 0
    withPrefix64k = 1
    usingExtDict = 2
    usingDictCtx = 3

# K4os.Compression.LZ4.Engine.LL
class LL(IntFlag):
    noDictIssue = 0
    dictSmall = 1

# K4os.Compression.LZ4.Engine.LL
class LL(IntFlag):
    endOnOutputSize = 0
    endOnInputSize = 1

# K4os.Compression.LZ4.Engine.LL
class LL(IntFlag):
    full = 0
    partial = 1

# K4os.Compression.LZ4.Engine.LL
class LL(IntFlag):
    loop_error = -2
    initial_error = -1
    ok = 0

# K4os.Compression.LZ4.Engine.LL
class LL(IntFlag):
    noDictCtx = 0
    usingDictCtxHc = 1

# K4os.Compression.LZ4.Engine.LL
class LL(IntFlag):
    rep_untested = 0
    rep_not = 1
    rep_confirmed = 2

# K4os.Compression.LZ4.Engine.LL
class LL(IntFlag):
    favorCompressionRatio = 0
    favorDecompressionSpeed = 1

# K4os.Compression.LZ4.Engine.LL
class LL(IntFlag):
    lz4hc = 0
    lz4opt = 1

