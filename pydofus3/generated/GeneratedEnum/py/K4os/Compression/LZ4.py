from enum import IntFlag

# K4os.Compression.LZ4.LZ4Level
class LZ4Level(IntFlag):
    L00_FAST = 0
    L03_HC = 3
    L04_HC = 4
    L05_HC = 5
    L06_HC = 6
    L07_HC = 7
    L08_HC = 8
    L09_HC = 9
    L10_OPT = 10
    L11_OPT = 11
    L12_MAX = 12

