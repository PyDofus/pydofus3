from enum import IntFlag

# Zaap_CSharp_Client.ZaapClient
class ZaapClient(IntFlag):
    ENV_VARIABLES_FIRST = 0
    FILE_FIRST = 1
    ONLY_ENV_VARIABLES = 2
    ONLY_FILE = 3

