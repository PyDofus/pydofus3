from enum import StrEnum


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


class Language(StrEnum):
    python = 'py'
    javascript = 'js'
    typescript = 'ts'
