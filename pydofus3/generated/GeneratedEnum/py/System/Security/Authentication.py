from enum import IntFlag

# System.Security.Authentication.SslProtocols
class SslProtocols(IntFlag):
    NONE = 0
    Ssl2 = 12
    Ssl3 = 48
    Tls = 192
    Tls11 = 768
    Tls12 = 3072
    Tls13 = 12288
    Default = 240

