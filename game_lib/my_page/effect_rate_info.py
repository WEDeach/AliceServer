from typing import Optional
from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class EffectRateInfo(BaseRecord):
    numerator: Optional[int] = field(default=None)
    denominator: Optional[int] = field(default=None)
