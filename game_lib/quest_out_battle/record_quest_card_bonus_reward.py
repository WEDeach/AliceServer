from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class QuestCardBonusRewardRecord(BaseRecord):
    objectType: int = field(default=0)
    objectId: int = field(default=0)
    num: int = field(default=0)
    originalNum: int = field(default=0)
    treasureImageType: int = field(default=0)
    isNew: bool = field(default=False)
    cardBonusRate: float = field(default=0.0)
