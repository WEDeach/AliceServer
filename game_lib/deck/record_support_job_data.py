from typing import Optional
from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class SupportJobDataRecord(BaseRecord):
    deckDataId: Optional[int] = field(default=0)
    position: Optional[int] = field(default=0)
    characterMstId: Optional[int] = field(default=0)
