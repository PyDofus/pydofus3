from enum import IntFlag

# DotNetty.Codecs.Compression.JZlib
class JZlib(IntFlag):
    NONE = 0
    ZLIB = 1
    GZIP = 2
    ANY = 3

# DotNetty.Codecs.Compression.ZlibWrapper
class ZlibWrapper(IntFlag):
    Zlib = 0
    Gzip = 1
    NONE = 2
    ZlibOrNone = 3

