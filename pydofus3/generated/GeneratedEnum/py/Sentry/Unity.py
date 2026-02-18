from enum import IntFlag

# Sentry.Unity.CompressionLevelWithAuto
class CompressionLevelWithAuto(IntFlag):
    Auto = -1
    Optimal = 0
    Fastest = 1
    NoCompression = 2

# Sentry.Unity.ScreenshotQuality
class ScreenshotQuality(IntFlag):
    Full = 0
    High = 1
    Medium = 2
    Low = 3

