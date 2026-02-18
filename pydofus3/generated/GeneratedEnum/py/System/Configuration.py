from enum import IntFlag

# System.Configuration.ConfigurationSaveMode
class ConfigurationSaveMode(IntFlag):
    Full = 2
    Minimal = 1
    Modified = 0

