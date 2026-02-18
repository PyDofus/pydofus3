from enum import IntFlag

# Ankama.AudioManagement.Playables.AudioEventPlayableStopMode
class AudioEventPlayableStopMode(IntFlag):
    NONE = 0
    Immediate = 1
    AllowFadeout = 2

