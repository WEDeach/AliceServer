from dataclasses import dataclass

from ..res_base import BaseRes


@dataclass
class CleanInfoData(BaseRes):
    cleaningType: int
    cleanTicketItemMstId: int
    cleanTicketNum: int
    remainingSecond: int
    isRoyalUser: bool
    enemyExpBonusRate: int
    cleanButtonType: int
    isSubscription: bool
