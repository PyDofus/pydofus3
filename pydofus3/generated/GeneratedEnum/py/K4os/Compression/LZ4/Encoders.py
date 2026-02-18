from enum import IntFlag

# K4os.Compression.LZ4.Encoders.EncoderAction
class EncoderAction(IntFlag):
    NONE = 0
    Loaded = 1
    Copied = 2
    Encoded = 3

