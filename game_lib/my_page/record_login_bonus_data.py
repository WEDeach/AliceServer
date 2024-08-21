from dataclasses import dataclass

from ..record_base import BaseRecord


@dataclass
class LoginBonusDataRecord(BaseRecord):
    loginBonusMstId: int
    loginBonusRewardMstId: int
    dayCount: int
    dayTotalCount: int
    lastRewardDate: int
    attentionText: str
