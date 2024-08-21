from typing import Optional
from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class WallBannerText(BaseRecord):
    bannerMstId: Optional[int] = field(default=None)
    text: Optional[str] = field(default=None)
    textA: Optional[str] = field(default=None)
    textB: Optional[str] = field(default=None)
    button: Optional[str] = field(default=None)
