from enum import IntFlag

# DotNetty.Common.ResourceLeakDetector
class ResourceLeakDetector(IntFlag):
    Disabled = 0
    Simple = 1
    Advanced = 2
    Paranoid = 3

