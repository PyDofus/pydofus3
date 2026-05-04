from typing import Annotated

from pydantic import ConfigDict, Field, TypeAdapter
from pydantic.dataclasses import dataclass

from pydofus3.catalog.binary.CatalogBinaryReader import CatalogBinaryReader


@dataclass(config=ConfigDict(validate_by_name=True, validate_by_alias=True))
class AssetBundleRequestOptions:
    Hash: Annotated[str, Field(alias='m_Hash')]
    Crc: Annotated[int, Field(alias='m_Crc')]
    BundleName: Annotated[str, Field(alias='m_BundleName')]
    BundleSize: Annotated[int, Field(alias='m_BundleSize')]

    Timeout: Annotated[int, Field(alias='m_Timeout')]
    RedirectLimit: Annotated[int, Field(alias='m_RedirectLimit')]
    RetryCount: Annotated[int, Field(alias='m_RetryCount')]
    AssetLoadMode: Annotated[int, Field(alias='m_AssetLoadMode')] = 0
    ChunkedTransfer: Annotated[bool, Field(alias='m_ChunkedTransfer')] = False
    UseCrcForCachedBundle: Annotated[bool, Field(alias='m_UseCrcForCachedBundle')] = False
    UseUnityWebRequestForLocalBundles: Annotated[bool, Field(alias='m_UseUnityWebRequestForLocalBundles')] = False
    ClearOtherCachedVersionsWhenLoaded: Annotated[bool, Field(alias='m_ClearOtherCachedVersionsWhenLoaded')] = False

    @staticmethod
    def read(reader: CatalogBinaryReader, offset: int) -> 'AssetBundleRequestOptions':

        hash_o, bundle_name_o, crc, bundle_size, common_info_o = reader.offset(offset).read_u32_multiple(5)

        return AssetBundleRequestOptions(
            Hash=reader.offset(hash_o).read(16).hex(),
            BundleName=reader.read_encoded_string(bundle_name_o, '_'),
            Crc=crc,
            BundleSize=bundle_size,
            Timeout=reader.offset(common_info_o).i16(),
            RedirectLimit=reader.u8(),
            RetryCount=reader.u8(),
            AssetLoadMode=1 if ((flags := reader.i32()) & 1) != 0 else 0,
            ChunkedTransfer=(flags & 2) != 0,
            UseCrcForCachedBundle=(flags & 4) != 0,
            UseUnityWebRequestForLocalBundles=(flags & 8) != 0,
            ClearOtherCachedVersionsWhenLoaded=(flags & 16) != 0,
        )


AssetBundleRequestOptionsAdapter = TypeAdapter(AssetBundleRequestOptions)
