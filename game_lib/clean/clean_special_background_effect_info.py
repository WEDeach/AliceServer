from dataclasses import dataclass
from typing import Optional

from .effect_rate_info import EffectRateInfo
from ..res_base import BaseRes


@dataclass
class CleanSpecialBackgroundEffectInfo(BaseRes):
    assetBundleName: str
    resourceName: str
    effectRateInfo: Optional[EffectRateInfo]
