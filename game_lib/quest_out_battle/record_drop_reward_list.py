from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class DropRewardListRecord(BaseRecord):
    objectType: int = field(default=0)
    objectId: int = field(default=0)
    num: int = field(default=0)
    rarity: int = field(default=0)
