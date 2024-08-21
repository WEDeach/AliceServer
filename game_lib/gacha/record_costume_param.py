from dataclasses import dataclass, field
from typing import Optional

from ..record_base import BaseRecord


@dataclass
class CostumeParamRecord(BaseRecord):
    gishinAssetBundleName: Optional[str] = field(default="gishin_character_spine/2")
    gishinResourceName: Optional[str] = field(default="002")
    ankiAssetBundleName: Optional[str] = field(default="anki_character_spine/1")
    ankiResourceName: Optional[str] = field(default="001")
    ankiHeadAssetBundleName: Optional[str] = field(
        default="anki_head_character_spine/7"
    )
    ankiHeadResourceName: Optional[str] = field(default="007")
