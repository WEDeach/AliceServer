from dataclasses import dataclass, field

from ..res_base import BaseRes


@dataclass
class SubscriptionInfo(BaseRes):
    isSubscriptionRelease: bool = field(default=True)
    isSubscriptionValid: bool = field(default=False)
    dailyRemainingCount: int = field(default=0)
    remainingTimeInSecondToReset: int = field(default=-1)
    dailyRemainingMaxCount: int = field(default=10)
