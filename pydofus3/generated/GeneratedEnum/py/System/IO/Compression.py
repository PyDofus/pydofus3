from enum import IntFlag

# System.IO.Compression.CompressionLevel
class CompressionLevel(IntFlag):
    Optimal = 0
    Fastest = 1
    NoCompression = 2

# System.IO.Compression.CompressionMode
class CompressionMode(IntFlag):
    Decompress = 0
    Compress = 1

