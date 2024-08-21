from typing import List, Optional
from dataclasses import dataclass, field

from .effect_rate_info import EffectRateInfo
from ..record_base import BaseRecord


@dataclass
class SpecialBackgroundDustEffectInfo(BaseRecord):
    backEffectResourceName: Optional[str] = field(default=None)
    backEffectAssetBundleName: Optional[str] = field(default=None)
    frontEffectResourceName: Optional[str] = field(default=None)
    frontEffectAssetBundleName: Optional[str] = field(default=None)
    displayType: Optional[int] = field(default=None)
    effectRateInfo: Optional[EffectRateInfo] = field(default=None)
