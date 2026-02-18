from enum import IntFlag

# Ankama.AudioManagement.Components.AudioEventContext
class AudioEventContext(IntFlag):
    NONE = 0
    Valid = 1
    OneShot = 2
    Restart = 4
    RespondsToMusicMarkers = 8

# Ankama.AudioManagement.Components.AudioEventLoader
class AudioEventLoader(IntFlag):
    NONE = 0
    Loading = 1
    Loaded = 2
    Error = 3

