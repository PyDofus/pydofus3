from enum import IntFlag

# Ankama.Launcher.ZaapWorker
class ZaapWorker(IntFlag):
    Stopped = 0
    Starting = 1
    Stopping = 2
    Started = 3
    Failed = 4

