from enum import IntFlag

# Ankama.SpinConnection.Network.Layers.TcpConnectionLayer
class TcpConnectionLayer(IntFlag):
    Disconnected = 0
    Connecting = 1
    Connected = 2
    Disposed = 3

