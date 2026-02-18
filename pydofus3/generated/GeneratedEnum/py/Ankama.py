from enum import IntFlag

# Ankama.SpinConnection
class SpinConnection(IntFlag):
    Disconnected = 0
    Connecting = 1
    Connected = 2
    Disposed = 3

