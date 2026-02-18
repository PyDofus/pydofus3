from enum import IntFlag

# XLua.GenFlag
class GenFlag(IntFlag):
    No = 0
    GCOptimize = 1

# XLua.HotfixFlag
class HotfixFlag(IntFlag):
    Stateless = 0
    Stateful = 1
    ValueTypeBoxing = 2
    IgnoreProperty = 4
    IgnoreNotPublic = 8
    Inline = 16
    IntKey = 32
    AdaptByDelegate = 64
    IgnoreCompilerGenerated = 128
    NoBaseProxy = 256

# XLua.LazyMemberTypes
class LazyMemberTypes(IntFlag):
    Method = 0
    FieldGet = 1
    FieldSet = 2
    PropertyGet = 3
    PropertySet = 4
    Event = 5

# XLua.LuaGCOptions
class LuaGCOptions(IntFlag):
    LUA_GCSTOP = 0
    LUA_GCRESTART = 1
    LUA_GCCOLLECT = 2
    LUA_GCCOUNT = 3
    LUA_GCCOUNTB = 4
    LUA_GCSTEP = 5
    LUA_GCSETPAUSE = 6
    LUA_GCSETSTEPMUL = 7

# XLua.LuaThreadStatus
class LuaThreadStatus(IntFlag):
    LUA_RESUME_ERROR = -1
    LUA_OK = 0
    LUA_YIELD = 1
    LUA_ERRRUN = 2
    LUA_ERRSYNTAX = 3
    LUA_ERRMEM = 4
    LUA_ERRERR = 5

# XLua.LuaTypes
class LuaTypes(IntFlag):
    LUA_TNONE = -1
    LUA_TNIL = 0
    LUA_TNUMBER = 3
    LUA_TSTRING = 4
    LUA_TBOOLEAN = 1
    LUA_TTABLE = 5
    LUA_TFUNCTION = 6
    LUA_TUSERDATA = 7
    LUA_TTHREAD = 8
    LUA_TLIGHTUSERDATA = 2

# XLua.ObjectTranslator
class ObjectTranslator(IntFlag):
    NO = 0
    INFO = 1
    WARN = 2
    ERROR = 3

# XLua.OptimizeFlag
class OptimizeFlag(IntFlag):
    Default = 0
    PackAsTable = 1

