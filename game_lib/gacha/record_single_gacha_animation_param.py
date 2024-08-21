from dataclasses import dataclass, field
from typing import Optional

from ..record_base import BaseRecord


@dataclass
class SingleGachaAnimationParamRecord(BaseRecord):
    isSS: Optional[bool] = field(default=False)
    isFallingHeadAnimation: Optional[bool] = field(default=False)
    serifType: Optional[int] = field(default=0)
