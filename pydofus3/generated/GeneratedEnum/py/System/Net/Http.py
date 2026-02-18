from enum import IntFlag

# System.Net.Http.ClientCertificateOption
class ClientCertificateOption(IntFlag):
    Manual = 0
    Automatic = 1

# System.Net.Http.HttpCompletionOption
class HttpCompletionOption(IntFlag):
    ResponseContentRead = 0
    ResponseHeadersRead = 1

