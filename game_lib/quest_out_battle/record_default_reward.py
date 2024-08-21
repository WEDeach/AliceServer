from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class DefaultRewardRecord(BaseRecord):
    exp: int = field(default=0)
    expBonus: int = field(default=0)
    expTotal: int = field(default=0)
    expBefore: int = field(default=0)
    expAfter: int = field(default=0)
    levelBefore: int = field(default=0)
    levelAfter: int = field(default=0)
    levelUpCount: int = field(default=0)
    jobExp: int = field(default=0)
    jobExpBonus: int = field(default=0)
    jobExpTotal: int = field(default=0)
    jobExpBefore: int = field(default=0)
    jobExpAfter: int = field(default=0)
    jobLevelBefore: int = field(default=0)
    jobLevelAfter: int = field(default=0)
    jobLevelUpCount: int = field(default=0)
    money: int = field(default=0)
    moneyBonus: int = field(default=0)
    moneyTotal: int = field(default=0)
    moneyBefore: int = field(default=0)
    moneyAfter: int = field(default=0)
