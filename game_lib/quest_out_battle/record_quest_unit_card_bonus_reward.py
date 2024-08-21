from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class QuestUnitCardBonusRewardRecord(BaseRecord):
    cardUniqueId: int = field(default=0)
    bonusType: int = field(default=0)
    itemMstId: int = field(default=0)
    addBonus: float = field(default=0.0)
    addWhenMaxLimitBreak: float = field(default=0.0)
    bonusTitle: str = field(default="")
    bonusItemName: str = field(default="")
    bonusItemNumName: str = field(default="")