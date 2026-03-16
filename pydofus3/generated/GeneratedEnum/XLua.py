from enum import IntEnum
from enum import IntFlag

class GenFlag(IntEnum):
	No = 0
	GCOptimize = 1

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

class LazyMemberTypes(IntEnum):
	Method = 0
	FieldGet = 1
	FieldSet = 2
	PropertyGet = 3
	PropertySet = 4
	Event = 5

class LuaGCOptions(IntEnum):
	LUA_GCSTOP = 0
	LUA_GCRESTART = 1
	LUA_GCCOLLECT = 2
	LUA_GCCOUNT = 3
	LUA_GCCOUNTB = 4
	LUA_GCSTEP = 5
	LUA_GCSETPAUSE = 6
	LUA_GCSETSTEPMUL = 7

class LuaThreadStatus(IntEnum):
	LUA_RESUME_ERROR = -1
	LUA_OK = 0
	LUA_YIELD = 1
	LUA_ERRRUN = 2
	LUA_ERRSYNTAX = 3
	LUA_ERRMEM = 4
	LUA_ERRERR = 5

class LuaTypes(IntEnum):
	LUA_TNONE = -1
	LUA_TNIL = 0
	LUA_TBOOLEAN = 1
	LUA_TLIGHTUSERDATA = 2
	LUA_TNUMBER = 3
	LUA_TSTRING = 4
	LUA_TTABLE = 5
	LUA_TFUNCTION = 6
	LUA_TUSERDATA = 7
	LUA_TTHREAD = 8

class ObjectTranslator:
	class LOGLEVEL(IntEnum):
		NO = 0
		INFO = 1
		WARN = 2
		ERROR = 3

class OptimizeFlag(IntFlag):
	Default = 0
	PackAsTable = 1

