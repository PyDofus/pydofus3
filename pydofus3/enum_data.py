from enum import StrEnum
from pathlib import Path

class TypeData(StrEnum):
    """
    Contains only data paths that include a catalog, as these are used for CLI auto-completion.
    For other data paths, use the `TypeDataOther` enum.
    """

    Map_Data = 'Dofus_Data/StreamingAssets/Content/Map/Data'
    Map_Textures1 = 'Dofus_Data/StreamingAssets/Content/Map/Textures/1x'
    Map_Textures2 = 'Dofus_Data/StreamingAssets/Content/Map/Textures/2x'
    Map_Textures4 = 'Dofus_Data/StreamingAssets/Content/Map/Textures/4x'
    Map_Textures_Effects = 'Dofus_Data/StreamingAssets/Content/Map/Textures/Effects'
    Data = 'Dofus_Data/StreamingAssets/Content/Data'
    Picto_Items = 'Dofus_Data/StreamingAssets/Content/Picto/Items'
    Picto_Monsters = 'Dofus_Data/StreamingAssets/Content/Picto/Monsters'
    Picto_Spells = 'Dofus_Data/StreamingAssets/Content/Picto/Spells'
    Picto_UI = 'Dofus_Data/StreamingAssets/Content/Picto/UI'
    Picto_Worldmaps = 'Dofus_Data/StreamingAssets/Content/Picto/Worldmaps'
    Animations = 'Dofus_Data/StreamingAssets/Content/Animations/Props'
    Skins = 'Dofus_Data/StreamingAssets/Content/Characters/Skins'
    Bones = 'Dofus_Data/StreamingAssets/Content/Characters/Bones'
    aa = 'Dofus_Data/StreamingAssets/aa'
    Dofus_Data = 'Dofus_Data'

class TypeDataOther(StrEnum):
    I18n = 'Dofus_Data/StreamingAssets/Content/I18n'
    Audio = 'Dofus_Data/StreamingAssets/Content/Audio/Banks/Desktop'
    Content = 'Dofus_Data/StreamingAssets/Content'
    Ornament = 'Dofus_Data/StreamingAssets/Content/Ornament'

class TypeDataMac(StrEnum):
    Map_Data = 'DofusContent/Content/Map/Data'
    Map_Textures1 = 'DofusContent/Content/Map/Textures/1x'
    Map_Textures2 = 'DofusContent/Content/Map/Textures/2x'
    Map_Textures4 = 'DofusContent/Content/Map/Textures/4x'
    Map_Textures_Effects = 'DofusContent/Content/Map/Textures/Effects'
    Data = 'DofusContent/Content/Data'
    Picto_Items = 'DofusContent/Content/Picto/Items'
    Picto_Monsters = 'DofusContent/Content/Picto/Monsters'
    Picto_Spells = 'DofusContent/Content/Picto/Spells'
    Picto_UI = 'DofusContent/Content/Picto/UI'
    Picto_Worldmaps = 'DofusContent/Content/Picto/Worldmaps'
    Animations = 'DofusContent/Content/Animations/Props'
    Skins = 'DofusContent/Content/Characters/Skins'
    Bones = 'DofusContent/Content/Characters/Bones'
    aa = 'Dofus.app/Contents/Resources/Data/StreamingAssets/aa'
    Dofus_Data = 'Dofus.app/Contents/Resources/Data'

class TypeDataOtherMac(StrEnum):
    I18n = 'DofusContent/Content/I18n'
    Audio = 'DofusContent/Content/Audio/Banks/Desktop'
    Content = 'DofusContent/Content'
    Ornament = 'Dofus_Data/StreamingAssets/Content/Ornament'

def get_data_path(game_path: Path, data_type: TypeData) -> Path:
    if (path:= (game_path / data_type)).exists():
        return path

    mac_path = game_path / TypeDataMac[data_type.name].value
    if mac_path.exists():
        return mac_path

    raise FileNotFoundError(f"Could not find '{data_type.name}' in either layout under {game_path}")

def get_data_other_path(game_path: Path, data_type: TypeDataOther) -> Path|None:
    if (path:= (game_path / data_type)).exists():
        return path

    mac_path = game_path / TypeDataOtherMac[data_type.name].value
    if mac_path.exists():
        return mac_path

    return None

def adapt_path(path: TypeData|TypeDataMac|str)-> str:
    value = str(path)
    if value in TypeData:
        return value
    elif value in TypeDataMac:
        return TypeData[TypeDataMac(value).name].value
    else:
        return value
