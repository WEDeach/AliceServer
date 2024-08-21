from dataclasses import dataclass

from .special_background_dust_effect_info import SpecialBackgroundDustEffectInfo
from ..record_base import BaseRecord


@dataclass
class BackgroundInfo(BaseRecord):
    id: int
    specialBackgroundDustEffectInfo: SpecialBackgroundDustEffectInfo
