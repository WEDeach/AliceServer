from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class BoostItemRecord(BaseRecord):
    effectType: int = field(default=0)
    effectValue: int = field(default=0)
    effectItemMstId: int = field(default=0)
    startTime: int = field(default=0)
    endTime: int = field(default=0)
