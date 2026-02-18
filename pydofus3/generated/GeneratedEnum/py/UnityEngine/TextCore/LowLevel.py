from enum import IntFlag

# UnityEngine.TextCore.LowLevel.FontEngineError
class FontEngineError(IntFlag):
    Success = 0
    Invalid_File_Path = 1
    Invalid_File_Format = 2
    Invalid_File_Structure = 3
    Invalid_File = 4
    Invalid_Table = 8
    Invalid_Glyph_Index = 16
    Invalid_Character_Code = 17
    Invalid_Pixel_Size = 23
    Invalid_Library = 33
    Invalid_Face = 35
    Invalid_Library_or_Face = 41
    Atlas_Generation_Cancelled = 100
    Invalid_SharedTextureData = 101
    OpenTypeLayoutLookup_Mismatch = 116

# UnityEngine.TextCore.LowLevel.FontFeatureLookupFlags
class FontFeatureLookupFlags(IntFlag):
    NONE = 0
    IgnoreLigatures = 4
    IgnoreSpacingAdjustments = 256

# UnityEngine.TextCore.LowLevel.GlyphLoadFlags
class GlyphLoadFlags(IntFlag):
    LOAD_DEFAULT = 0
    LOAD_NO_SCALE = 1
    LOAD_NO_HINTING = 2
    LOAD_RENDER = 4
    LOAD_NO_BITMAP = 8
    LOAD_FORCE_AUTOHINT = 32
    LOAD_MONOCHROME = 4096
    LOAD_NO_AUTOHINT = 32768
    LOAD_COLOR = 1048576
    LOAD_COMPUTE_METRICS = 2097152
    LOAD_BITMAP_METRICS_ONLY = 4194304

# UnityEngine.TextCore.LowLevel.GlyphPackingMode
class GlyphPackingMode(IntFlag):
    BestShortSideFit = 0
    BestLongSideFit = 1
    BestAreaFit = 2
    BottomLeftRule = 3
    ContactPointRule = 4

# UnityEngine.TextCore.LowLevel.GlyphRasterModes
class GlyphRasterModes(IntFlag):
    RASTER_MODE_8BIT = 1
    RASTER_MODE_MONO = 2
    RASTER_MODE_NO_HINTING = 4
    RASTER_MODE_HINTED = 8
    RASTER_MODE_BITMAP = 16
    RASTER_MODE_SDF = 32
    RASTER_MODE_SDFAA = 64
    RASTER_MODE_MSDF = 256
    RASTER_MODE_MSDFA = 512
    RASTER_MODE_1X = 4096
    RASTER_MODE_8X = 8192
    RASTER_MODE_16X = 16384
    RASTER_MODE_32X = 32768
    RASTER_MODE_COLOR = 65536

# UnityEngine.TextCore.LowLevel.GlyphRenderMode
class GlyphRenderMode(IntFlag):
    DEFAULT = 0
    SMOOTH_HINTED = 4121
    SMOOTH = 4117
    COLOR_HINTED = 69656
    COLOR = 69652
    RASTER_HINTED = 4122
    RASTER = 4118
    SDF = 4134
    SDF8 = 8230
    SDF16 = 16422
    SDF32 = 32806
    SDFAA_HINTED = 4169
    SDFAA = 4165

